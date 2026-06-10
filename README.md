# tesis_tex

Repositorio para la tesis escrita en LaTeX con scripts de análisis en Python.

## Estructura del proyecto

```
.
├── main.tex                 # Documento principal LaTeX
├── references.bib           # Referencias bibliográficas (BibLaTeX)
├── chapters/                # Capítulos de la tesis
│   ├── introduction.tex
│   ├── methodology.tex
│   ├── results.tex
│   └── conclusions.tex
├── figures/                 # Figuras generadas por Python
├── scripts/                 # Scripts de Python para análisis y gráficas
│   └── generate_figures.py
├── requirements.txt         # Dependencias de Python
└── Makefile                 # Automatización de compilación
```

## Requisitos

### LaTeX
- TeX Live o MiKTeX con los paquetes: `babel`, `biblatex`, `graphicx`, `amsmath`, `hyperref`
- `biber` para la bibliografía

### Python
- Python 3.10+
- Dependencias: `pip install -r requirements.txt`

## Uso

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# Generar figuras con Python
make figures

# Compilar el PDF completo (figuras + LaTeX)
make all

# Solo compilar LaTeX
make pdf

# Limpiar archivos auxiliares
make clean
```