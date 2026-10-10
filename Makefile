PY := python3 -I
OUT := $(or $(TMPDIR),/tmp)/reason-verify
ZENODO := $(or $(TMPDIR),/tmp)/reason-zenodo
RAW := notes/audit-raw

.PHONY: verify listings repro numbers audit quotes sha text zenodo

## verify: check the restored listings against the PDF, run them and the duplicate check, then
## check every quoted number and quotation, the audit register, the triage and the PDF checksums
verify: listings repro numbers audit quotes sha

listings:
	$(PY) scripts/check_listings.py

# The §33.B listing writes v0_results/ (including a 27 MB trace) to the current directory,
# so it is run from $(OUT).
repro:
	@mkdir -p $(OUT)
	cd $(OUT) && $(PY) $(CURDIR)/repro/v0_lower_loop.py > $(OUT)/v0_summary.json
	$(PY) repro/diagnostic_cycle.py > $(OUT)/diagnostic_cycle.json
	$(PY) repro/dup_paragraphs.py text/foundations-8.0.txt text/engineering-3.5.txt > $(OUT)/dup_paragraphs.txt
	@echo "outputs in $(OUT)"

numbers: repro
	$(PY) scripts/check_numbers.py $(OUT)

audit:
	$(PY) scripts/audit_index.py --check
	$(PY) scripts/triage.py --check

quotes:
	$(PY) scripts/check_audit_quotes.py
	$(PY) scripts/check_raw_quotes.py $(RAW)/V1A.md $(RAW)/V1B.md $(RAW)/V2A.md $(RAW)/V2B.md $(RAW)/V2C.md

sha:
	shasum -a 256 -c sources/SHA256SUMS

## text: regenerate the extracted text from the PDFs (needs poppler's pdftotext)
text:
	pdftotext -layout sources/foundations-8.0/Foundations_of_Reason_8.0_EN.pdf text/foundations-8.0.txt
	pdftotext -layout sources/engineering-3.5/Engineering_of_Reason_3.5_EN.pdf text/engineering-3.5.txt
	pdftotext sources/foundations-8.0/Foundations_of_Reason_8.0_EN.pdf text/foundations-8.0.raw.txt
	pdftotext sources/engineering-3.5/Engineering_of_Reason_3.5_EN.pdf text/engineering-3.5.raw.txt

## zenodo: refresh notes/zenodo-history.md from the Zenodo API (needs network)
zenodo:
	@mkdir -p $(ZENODO)
	for c in 17957561 22975036; do for p in 1 2; do \
	  curl -sS --max-time 60 -o $(ZENODO)/c$${c}_p$${p}.json \
	    "https://zenodo.org/api/records?q=conceptrecid:$$c&all_versions=true&size=25&page=$$p&sort=mostrecent"; \
	done; done
	$(PY) scripts/zenodo_history.py $(ZENODO) > notes/zenodo-history.md
