# =============================================================================
# Makefile para compilar la tesis (LaTeX) y ejecutar scripts (Python)
# =============================================================================

MAIN = main
LATEX = pdflatex
BIBER = biber
PYTHON = python3

# --- Targets principales ---

.PHONY: all pdf figures clean help

all: figures pdf  ## Genera figuras y compila el PDF

pdf: $(MAIN).pdf  ## Compila el documento LaTeX

figures:  ## Ejecuta los scripts de Python para generar figuras
	$(PYTHON) scripts/generate_figures.py

$(MAIN).pdf: $(MAIN).tex references.bib chapters/*.tex
	$(LATEX) $(MAIN)
	$(BIBER) $(MAIN)
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

clean:  ## Limpia archivos auxiliares de LaTeX y Python
	rm -f *.aux *.bbl *.blg *.brf *.fdb_latexmk *.fls *.idx *.ilg *.ind
	rm -f *.lof *.log *.lot *.nav *.out *.snm *.synctex.gz *.toc *.vrb
	rm -f *.bcf *.run.xml *.xdv
	rm -rf __pycache__ scripts/__pycache__

help:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
