# Makefile for DANDI citations collection pipeline
#
# Usage:
#   make all             - Run full pipeline (discover → merge → pdfs → extract-contexts)
#   make discover        - Discover citations only
#   make merge           - Detect and merge preprints only
#   make pdfs            - Fetch PDFs only
#   make extract-contexts - Extract citation contexts from PDFs
#   make clean           - Remove generated TSV and PDFs
#
# Designed to be run with datalad run for reproducibility

COLLECTION := dandi-full.yaml
TSV := dandi-full-citations.tsv
PDF_DIR := pdfs

# Path to citations-collector (adjust if needed)
CC := citations-collector

# LLM classification settings (override via environment or command line)
BACKEND ?= dartmouth
MODEL ?= google.gemma-3-27b-it
THRESHOLD ?= 0.7

.PHONY: all discover merge pdfs extract-contexts classify zotero clean help status

all: discover merge pdfs extract-contexts classify

help:
	@echo "DANDI Citations Collection Pipeline"
	@echo ""
	@echo "Targets:"
	@echo "  all             - Run full pipeline (discover → merge → pdfs → extract → classify)"
	@echo "  discover        - Discover citations from all sources"
	@echo "  merge           - Detect and mark preprints that have published versions"
	@echo "  pdfs            - Fetch open-access PDFs for all citations"
	@echo "  extract-contexts - Extract citation contexts from PDFs/HTMLs"
	@echo "  classify        - Classify unclassified citations with LLM"
	@echo "  zotero          - Sync citations to Zotero (requires ZOTERO_API_KEY)"
	@echo "  status          - Show current status (citations, PDFs, contexts, classifications)"
	@echo "  clean           - Remove generated TSV and PDFs"
	@echo ""
	@echo "Files:"
	@echo "  Input:  $(COLLECTION)"
	@echo "  Output: $(TSV)"
	@echo "  PDFs:   $(PDF_DIR)/"
	@echo ""
	@echo "LLM Classification:"
	@echo "  BACKEND=$(BACKEND)   (ollama|dartmouth|openrouter|openai)"
	@echo "  MODEL=$(MODEL)"
	@echo "  THRESHOLD=$(THRESHOLD)"
	@echo "  Example: make classify BACKEND=ollama MODEL=qwen2:7b"
	@echo ""
	@echo "Environment Variables:"
	@echo "  OPENAI_API_KEY or DARTMOUTH_API_TOKEN - For LLM backends (not needed for Ollama)"
	@echo "  ZOTERO_API_KEY - API key for Zotero sync (required for 'make zotero')"

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

# Extract citation contexts from PDFs/HTMLs
extract-contexts: $(TSV)
	@echo ""
	@echo "=== Step 4: Extracting citation contexts ==="
	$(CC) extract-contexts $(COLLECTION) --git-annex --overwrite
	@echo ""
	@echo "Contexts extracted to: $(PDF_DIR)/*/extracted_citations.json"
	@find $(PDF_DIR) -name "extracted_citations.json" | wc -l | awk '{print "Papers with extracted contexts:", $$1}'

# Classify citation relationships using LLM
# Only processes citations where classification_method is empty
# Requires API keys in environment (OPENAI_API_KEY or DARTMOUTH_API_TOKEN)
classify: $(TSV)
	@echo ""
	@echo "=== Step 5: Classifying citation relationships ==="
	@echo "Backend: $(BACKEND), Model: $(MODEL), Threshold: $(THRESHOLD)"
	$(CC) classify $(COLLECTION) --backend $(BACKEND) --model $(MODEL) --confidence-threshold $(THRESHOLD)
	@echo ""
	@echo "Classifications saved to: $(PDF_DIR)/*/classifications.json"
	@tail -n +2 $(TSV) | awk -F'\t' '$$23 != ""' | wc -l | awk '{print "Classified citations:", $$1}'
	@tail -n +2 $(TSV) | awk -F'\t' '$$23 == ""' | wc -l | awk '{print "Unclassified citations:", $$1}'

# Sync to Zotero
zotero: $(TSV)
	@echo ""
	@echo "=== Step 5: Syncing to Zotero ==="
	@if [ -z "$$ZOTERO_API_KEY" ]; then \
		echo "ERROR: ZOTERO_API_KEY environment variable not set"; \
		echo "Usage: ZOTERO_API_KEY=your_key make zotero"; \
		exit 1; \
	fi
	$(CC) sync-zotero $(COLLECTION) --api-key $$ZOTERO_API_KEY
	@echo ""
	@echo "Synced to: https://www.zotero.org/groups/5774211/dandi/collections/UHK47FKX"

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
		find $(PDF_DIR) -name "extracted_citations.json" | wc -l | awk '{print "  Extracted contexts:", $$1}'; \
		find $(PDF_DIR) -name "classifications.json" | wc -l | awk '{print "  Classifications:", $$1}'; \
	else \
		echo "PDF directory: Not found"; \
	fi
	@echo ""
	@if [ -f $(TSV) ]; then \
		echo "Classification Status:"; \
		tail -n +2 $(TSV) | awk -F'\t' '$$23 != ""' | wc -l | awk '{print "  Classified:", $$1}'; \
		tail -n +2 $(TSV) | awk -F'\t' '$$23 == ""' | wc -l | awk '{print "  Unclassified:", $$1}'; \
		echo "  Methods:"; \
		tail -n +2 $(TSV) | awk -F'\t' '$$23 != "" {print $$23}' | sort | uniq -c | awk '{printf "    %-10s: %d\n", $$2, $$1}' || true; \
		echo "  Relationship Types:"; \
		tail -n +2 $(TSV) | awk -F'\t' '$$16 != "" {print $$16}' | sort | uniq -c | awk '{printf "    %-20s: %d\n", $$2, $$1}' || true; \
	fi
