# tesis_tex

Repositorio para la tesis escrita en LaTeX con scripts de análisis en Python.

## Flujo de trabajo

1. **Edita** los archivos `.tex` y `.bib` localmente
2. **Haz push** a `main`
3. **GitHub Actions** compila automáticamente el PDF
4. **Descarga** el PDF desde la pestaña [Actions](../../actions) (artefacto) o desde [Releases](../../releases)

> No necesitas tener LaTeX instalado localmente. Solo edita los `.tex` y el CI se encarga del resto.

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
├── Makefile                 # Compilación local (opcional)
└── .github/workflows/       # GitHub Actions (compilación automática)
    └── build-thesis.yml
```

## Compilación automática (GitHub Actions)

Cada vez que haces push a `main` con cambios en archivos `.tex`, `.bib`, `figures/` o `scripts/`:

1. Se instalan las dependencias Python
2. Se ejecutan los scripts para generar figuras
3. Se compila `main.tex` → `main.pdf` con latexmk
4. El PDF queda disponible como **artefacto** (30 días) y como **release**

También puedes lanzar la compilación manualmente desde Actions → "Compilar Tesis" → "Run workflow".

## Compilación local (opcional)

Si prefieres compilar localmente también puedes hacerlo:

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# Generar figuras y compilar
make all

# Solo compilar LaTeX
make pdf

# Limpiar archivos auxiliares
make clean
```