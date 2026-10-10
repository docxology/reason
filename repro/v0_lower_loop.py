# Engineering of Reason 3.5, §33.B (pp. 105-106): the printed listing with its indentation
# restored from the PDF text. Nothing else is changed (scripts/check_listings.py verifies this).
# Run it from the directory that should receive v0_results/ (make verify uses $TMPDIR).
"""Lower-loop demonstration: learning, frozen evaluation, replay and reset.
No model receives the world's transition table or held-out answers.
"""
import copy
import hashlib
import json
import random
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    states: int = 32
    actions: int = 6
    train_steps: int = 1200
    test_steps: int = 400
    environments: int = 12
    alpha: float = 1.0


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()


class World:
    """Closed simulator; snapshot restores only this laboratory world."""
    def __init__(self, cfg, world_seed):
        self.cfg = cfg
        rng = random.Random(world_seed)
        self.transitions = [
            [rng.randrange(cfg.states) for _ in range(cfg.actions)]
            for _ in range(cfg.states)
        ]
        self.state = 0
        self.tick = 0

    def reset(self, episode_seed):
        self.state = random.Random(episode_seed).randrange(self.cfg.states)
        self.tick = 0
        return self.state

    def step(self, action):
        if action not in range(self.cfg.actions):
            raise ValueError("action outside declared simulator interface")
        self.state = self.transitions[self.state][action]
        self.tick += 1
        return self.state

    def snapshot(self):
        return copy.deepcopy((self.transitions, self.state, self.tick))

    def restore(self, snapshot):
        self.transitions, self.state, self.tick = copy.deepcopy(snapshot)


class Model:
    def __init__(self, cfg):
        self.cfg = cfg
        self.counts = defaultdict(lambda: [0] * cfg.states)
        self.version = 0

    def predict(self, state, action):
        counts = self.counts.get((state, action), [0] * self.cfg.states)
        total = sum(counts) + self.cfg.alpha * self.cfg.states
        probabilities = [(n + self.cfg.alpha) / total for n in counts]
        prediction = max(range(self.cfg.states), key=probabilities.__getitem__)
        return prediction, probabilities

    def update(self, state, action, actual):
        self.counts[(state, action)][actual] += 1
        self.version += 1


def episode(world, model, *, episode_seed, policy_seed, steps, learn):
    state = world.reset(episode_seed)
    rng = random.Random(policy_seed)
    records = []
    for index in range(steps):
        # The same probing policy is used in both conditions.
        action = rng.randrange(model.cfg.actions)
        version_before = model.version
        prediction, probabilities = model.predict(state, action)
        actual = world.step(action)
        error = int(prediction != actual)
        brier = sum((p - int(i == actual)) ** 2
                    for i, p in enumerate(probabilities))
        if learn:
            model.update(state, action, actual)
        records.append({
            "step": index, "state": state, "action": action,
            "predicted_state": prediction, "actual_state": actual,
            "probabilities": probabilities, "error": error, "brier": brier,
            "prediction_model_version": version_before,
            "model_version_after": model.version, "update_enabled": learn,
        })
        state = actual
    return records


def mean(records, field):
    return sum(row[field] for row in records) / len(records)


def paired_interval(values):
    # Resample independent worlds, not correlated transitions within a world.
    rng = random.Random(991)
    samples = sorted(sum(rng.choices(values, k=len(values))) / len(values)
                     for _ in range(2000))
    return [samples[49], samples[1949]]


def run(output_dir="v0_results"):
    cfg = Config()
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    results = []
    with (output / "trace.jsonl").open("w") as log:
        for world_seed in range(cfg.environments):
            adaptive, frozen = Model(cfg), Model(cfg)
            seeds = dict(episode_seed=1000 + world_seed,
                         policy_seed=2000 + world_seed, steps=cfg.train_steps)
            train = episode(World(cfg, world_seed), adaptive, learn=True, **seeds)
            control_train = episode(World(cfg, world_seed), frozen, learn=False, **seeds)
            # Both models experienced identical external transitions.
            keys = lambda rows: [(r["state"], r["action"], r["actual_state"]) for r in rows]
            assert keys(train) == keys(control_train)
            held = dict(episode_seed=3000 + world_seed,
                        policy_seed=4000 + world_seed, steps=cfg.test_steps)
            version = adaptive.version
            test = episode(World(cfg, world_seed), adaptive, learn=False, **held)
            control = episode(World(cfg, world_seed), frozen, learn=False, **held)
            assert adaptive.version == version
            assert keys(test) == keys(control)
            replay = episode(World(cfg, world_seed), adaptive, learn=False, **held)
            assert digest(test) == digest(replay)
            # Persistence after a model checkpoint; reset removes acquired knowledge.
            checkpoint = copy.deepcopy(adaptive)
            restored = episode(World(cfg, world_seed), checkpoint, learn=False, **held)
            reset = episode(World(cfg, world_seed), Model(cfg), learn=False, **held)
            assert digest(restored) == digest(test)
            assert digest(reset) == digest(control)
            world = World(cfg, world_seed)
            world.reset(7000 + world_seed)
            snapshot = world.snapshot()
            first = world.step(0)
            world.restore(snapshot)
            assert first == world.step(0)
            covered = sum((r["state"], r["action"]) in adaptive.counts for r in test)
            results.append({
                "world_seed": world_seed,
                "adaptive_error": mean(test, "error"),
                "frozen_error": mean(control, "error"),
                "adaptation_gain": mean(control, "error") - mean(test, "error"),
                "adaptive_brier": mean(test, "brier"),
                "frozen_brier": mean(control, "brier"),
                "test_transition_coverage": covered / len(test),
                "replay_equal": True, "checkpoint_equal": True,
                "reset_equals_control": True,
            })
            for condition, rows in [("train", train), ("control_train", control_train),
                                    ("test", test), ("control", control)]:
                for row in rows:
                    log.write(json.dumps({"world_seed": world_seed,
                                          "condition": condition, **row}) + "\n")
    gains = [row["adaptation_gain"] for row in results]
    report = {"config": asdict(cfg), "config_hash": digest(asdict(cfg)),
              "worlds": results, "mean_gain": sum(gains) / len(gains),
              "world_bootstrap_95_interval": paired_interval(gains),
              "scope": "retained transition learning in known finite worlds"}
    (output / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["mean_gain", "world_bootstrap_95_interval", "scope"]}))
    return report


if __name__ == "__main__":
    run()
