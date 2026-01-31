# Makefile for DANDI citations collection pipeline
#
# Usage:
#   make all          - Run full pipeline (discover → detect-merges → fetch-pdfs)
#   make discover     - Discover citations only
#   make merge        - Detect and merge preprints only
#   make pdfs         - Fetch PDFs only
#   make clean        - Remove generated TSV and PDFs
#
# Designed to be run with datalad run for reproducibility

COLLECTION := dandi-full.yaml
TSV := dandi-full-citations.tsv
PDF_DIR := pdfs

# Path to citations-collector (adjust if needed)
CC := citations-collector

.PHONY: all discover merge pdfs clean help

all: discover merge pdfs

help:
	@echo "DANDI Citations Collection Pipeline"
	@echo ""
	@echo "Targets:"
	@echo "  all          - Run full pipeline (discover → detect-merges → fetch-pdfs)"
	@echo "  discover     - Discover citations from all sources"
	@echo "  merge        - Detect and mark preprints that have published versions"
	@echo "  pdfs         - Fetch open-access PDFs for all citations"
	@echo "  clean        - Remove generated TSV and PDFs"
	@echo ""
	@echo "Files:"
	@echo "  Input:  $(COLLECTION)"
	@echo "  Output: $(TSV)"
	@echo "  PDFs:   $(PDF_DIR)/"

# Discover citations from all configured sources
discover: $(COLLECTION)
	@echo "=== Step 1: Discovering citations ==="
	$(CC) discover $(COLLECTION)
	@echo ""
	@echo "Citations saved to: $(TSV)"
	@wc -l $(TSV) | awk '{print "Total rows:", $$1-1, "citations"}'

# Detect and merge preprints with published versions
merge: $(TSV)
	@echo ""
	@echo "=== Step 2: Detecting and merging preprints ==="
	$(CC) detect-merges --config $(COLLECTION)
	@echo ""
	@grep -c "merged" $(TSV) | awk '{print "Merged preprints:", $$1}' || echo "Merged preprints: 0"

# Fetch open-access PDFs
pdfs: $(TSV)
	@echo ""
	@echo "=== Step 3: Fetching PDFs ==="
	mkdir -p $(PDF_DIR)
	$(CC) fetch-pdfs $(COLLECTION) --output-dir $(PDF_DIR)
	@echo ""
	@echo "PDFs saved to: $(PDF_DIR)/"
	@find $(PDF_DIR) -name "*.pdf" | wc -l | awk '{print "Total PDFs:", $$1}'

# Clean generated files
clean:
	@echo "Removing generated files..."
	rm -f $(TSV)
	rm -rf $(PDF_DIR)
	@echo "Cleaned: $(TSV) and $(PDF_DIR)/"

# Show current status
status:
	@echo "=== Current Status ==="
	@if [ -f $(TSV) ]; then \
		echo "Citations TSV: $(TSV)"; \
		wc -l $(TSV) | awk '{print "  Total rows:", $$1}'; \
		tail -n +2 $(TSV) | grep -c "active" | awk '{print "  Active:", $$1}' || echo "  Active: 0"; \
		tail -n +2 $(TSV) | grep -c "merged" | awk '{print "  Merged:", $$1}' || echo "  Merged: 0"; \
	else \
		echo "Citations TSV: Not found"; \
	fi
	@echo ""
	@if [ -d $(PDF_DIR) ]; then \
		echo "PDF directory: $(PDF_DIR)/"; \
		find $(PDF_DIR) -name "*.pdf" | wc -l | awk '{print "  Total PDFs:", $$1}'; \
	else \
		echo "PDF directory: Not found"; \
	fi
