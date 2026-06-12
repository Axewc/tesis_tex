# =============================================================================
# Makefile para compilar la tesis (LaTeX) y ejecutar scripts (Python)
# =============================================================================

TESIS_DIR = tesis
MAIN = $(TESIS_DIR)/tesis
LATEX = pdflatex
BIBTEX = bibtex
PYTHON = python3

# --- Targets principales ---

.PHONY: all pdf figures clean help

all: figures pdf  ## Genera figuras y compila el PDF

pdf: $(MAIN).pdf  ## Compila el documento LaTeX

figures:  ## Ejecuta los scripts de Python para generar figuras
	$(PYTHON) scripts/generate_figures.py

$(MAIN).pdf: $(MAIN).tex $(TESIS_DIR)/referencias.bib $(TESIS_DIR)/capitulos/*.tex
	cd $(TESIS_DIR) && $(LATEX) tesis
	cd $(TESIS_DIR) && $(BIBTEX) tesis
	cd $(TESIS_DIR) && $(LATEX) tesis
	cd $(TESIS_DIR) && $(LATEX) tesis

clean:  ## Limpia archivos auxiliares de LaTeX y Python
	cd $(TESIS_DIR) && rm -f *.aux *.bbl *.blg *.brf *.fdb_latexmk *.fls *.idx *.ilg *.ind
	cd $(TESIS_DIR) && rm -f *.lof *.log *.lot *.nav *.out *.snm *.synctex.gz *.toc *.vrb
	cd $(TESIS_DIR) && rm -f *.bcf *.run.xml *.xdv
	rm -rf __pycache__ scripts/__pycache__

help:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
