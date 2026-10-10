# Engineering of Reason 3.5, §33.C.1 (pp. 109-111): the printed listing with its indentation
# restored from the PDF text. Nothing else is changed (scripts/check_listings.py verifies this).
"""Finite diagnostic controller; standard Python, no LLM or open-world claims."""
from dataclasses import dataclass, field
import json

CAUSES = ('D', 'A', 'S')


@dataclass(frozen=True)
class Probe:
    name: str
    cost: int
    outcomes: tuple


PROBES = (
    Probe('read_main_again', 1, (0, 0, 0)),
    Probe('receipt', 1, (0, 1, 1)),
    Probe('independent_motion', 2, (0, 0, 1)),
)


@dataclass
class Memory:
    claims: list = field(default_factory=list)
    methods: dict = field(default_factory=dict)


class World:
    def __init__(self, cause, *, receipt_valid=True, unexpected=False):
        self._cause = cause
        self.receipt_valid = receipt_valid
        self.unexpected = unexpected

    def observe(self, probe):
        # Receipt provenance is observed, not inferred from its plausible value.
        if probe.name == 'receipt' and not self.receipt_valid:
            return None, False
        if self.unexpected:
            return 9, True  # Unmodelled observation; do not force a diagnosis.
        return probe.outcomes[CAUSES.index(self._cause)], True

    def apply(self, action):
        return action == 'REPAIR_' + self._cause


def partition(hypotheses, probe):
    groups = {}
    for h in hypotheses:
        groups.setdefault(probe.outcomes[CAUSES.index(h)], []).append(h)
    return [tuple(g) for g in groups.values()]


def terminal(hypotheses):
    # Equal priors, 12 units for a wrong targeted repair, 4 for deferral.
    if len(hypotheses) == 1:
        return 0.0, 'REPAIR_' + hypotheses[0]
    return 4.0, 'DEFER'


def plan(hypotheses, probes, budget, memory, counters):
    """Optimal finite plan for supplied likelihoods; cost includes delay."""
    key = (hypotheses, tuple(probes), budget)
    if key in memory.methods:
        counters['method_hits'] += 1
        return memory.methods[key]
    counters['evaluated_states'] += 1
    best_loss, action = terminal(hypotheses)
    chosen = None
    for probe in probes:
        if probe.cost > budget:
            continue
        groups = partition(hypotheses, probe)
        if len(groups) == 1:
            continue
        rest = tuple(q for q in probes if q != probe)
        expected = probe.cost + sum(
            len(g) / len(hypotheses) * plan(
                g, rest, budget - probe.cost, memory, counters
            )[0] for g in groups
        )
        if expected < best_loss - 1e-12:
            best_loss, chosen = expected, probe
    result = (best_loss, chosen, action)
    # A solved, model-scoped plan is retained; this is not a discovered theory.
    memory.methods[key] = result
    return result


def run_episode(world, memory, *, probes=PROBES, budget=3, trigger='mismatch'):
    assert trigger in ('mismatch', 'coverage_gap')
    hypotheses = CAUSES
    remaining = tuple(probes)
    trace = [{'trigger': trigger, 'hypotheses': hypotheses, 'budget': budget}]
    counts = {'method_hits': 0, 'evaluated_states': 0}
    spent = 0
    status = 'OPEN'
    while True:
        _, probe, action = plan(hypotheses, remaining, budget, memory, counts)
        if probe is None:
            status = 'LOCAL_SUFFICIENT' if action != 'DEFER' else 'OPEN'
            break
        value, valid_source = world.observe(probe)
        budget -= probe.cost
        spent += probe.cost
        remaining = tuple(p for p in remaining if p != probe)
        trace.append({'probe': probe.name, 'value': value,
                      'source_valid': valid_source, 'budget': budget})
        if not valid_source:
            continue
        updated = tuple(h for h in hypotheses
                        if probe.outcomes[CAUSES.index(h)] == value)
        if not updated:
            action, status = 'DEFER', 'MODEL_MISMATCH'
            break
        hypotheses = updated
    if action != 'DEFER':
        success = world.apply(action)
        trace.append({'action': action, 'success': success})
        if not success:
            status = 'MODEL_MISMATCH'
            memory.methods.clear()
    claim = {'status': status, 'hypotheses': hypotheses,
             'action': action, 'spent': spent, 'evidence': trace,
             'scope': 'one episode; given deterministic probe models'}
    memory.claims.append(claim)
    return {**claim, **counts}


def verify():
    results = []
    for cause in CAUSES:
        memory = Memory()
        first = run_episode(World(cause), memory)
        second = run_episode(World(cause), memory, trigger='coverage_gap')
        assert first['action'] == second['action'] == 'REPAIR_' + cause
        assert first['spent'] <= 3 and second['evaluated_states'] == 0
        assert second['method_hits'] > 0 and len(memory.claims) == 2
        assert all(e.get('probe') != 'read_main_again' for e in first['evidence'])
        results.extend((first, second))
    # Information cannot be manufactured from an uninformative channel.
    r = run_episode(World('D'), Memory(), probes=PROBES[:1])
    assert r['action'] == 'DEFER' and r['spent'] == 0
    results.append(r)
    r = run_episode(World('S'), Memory(), budget=0)
    assert r['status'] == 'OPEN' and r['spent'] == 0
    results.append(r)
    r = run_episode(World('A', receipt_valid=False), Memory())
    assert r['action'] == 'DEFER' and set(('D', 'A')) <= set(r['hypotheses'])
    results.append(r)
    r = run_episode(World('S', unexpected=True), Memory())
    assert r['status'] == 'MODEL_MISMATCH' and r['action'] == 'DEFER'
    results.append(r)
    # Changed causal structure must invalidate a cached plan automatically.
    memory = Memory()
    run_episode(World('S'), memory)
    changed = (Probe('receipt', 1, (0, 0, 0)),)
    r = run_episode(World('D'), memory, probes=changed)
    assert r['action'] == 'DEFER' and r['evaluated_states'] > 0
    results.append(r)
    # Increased observation/delay cost can make deferral preferable.
    expensive = tuple(Probe(p.name, 8, p.outcomes) for p in PROBES)
    r = run_episode(World('D'), Memory(), probes=expensive, budget=20)
    assert r['action'] == 'DEFER' and r['spent'] == 0
    results.append(r)
    print(json.dumps({'checks': 'PASS', 'episodes': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    verify()
