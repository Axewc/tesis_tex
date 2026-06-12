# Tesis — Sesgo socioeconómico en clasificadores de texto

Plantilla LaTeX para la tesis de licenciatura.

## Estructura

```
tesis/
├── tesis.tex                 ← archivo principal (compilar este)
├── preamble.tex              ← paquetes, fuentes, geometría, comandos
├── portada.tex               ← portada institucional
├── frontmatter/
│   ├── dedicatoria.tex
│   ├── agradecimientos.tex
│   └── resumen.tex           ← resumen en español + abstract en inglés
├── capitulos/
│   ├── 01_introduccion.tex   ← redactado a partir del plan del proyecto
│   ├── 02_marco_teorico.tex
│   ├── 03_metodologia.tex
│   ├── 04_resultados.tex
│   ├── 05_indice_ins.tex     ← incluye formalización preliminar del INS
│   ├── 06_discusion.tex
│   └── 07_conclusiones.tex
├── apendices/
│   ├── A_encuesta.tex
│   └── B_corpus_controlado.tex
├── imagenes/                 ← coloca aquí logos, diagramas, gráficos
└── referencias.bib           ← bibliografía en formato BibTeX
```

## Compilación

### Con `bibtex` (configuración por defecto)

```bash
pdflatex tesis.tex
bibtex   tesis
pdflatex tesis.tex
pdflatex tesis.tex
```

### Con `latexmk` (recomendado)

```bash
latexmk -pdf tesis.tex
```

Para limpiar archivos auxiliares:
```bash
latexmk -c
```

### Con `biber` (más moderno, requiere ajuste)

En `preamble.tex`, en la línea
```latex
\usepackage[backend=bibtex, ...]{biblatex}
```
cambia `backend=bibtex` por `backend=biber`. Luego:

```bash
pdflatex tesis.tex
biber    tesis
pdflatex tesis.tex
pdflatex tesis.tex
```

## Personalización rápida

- **Portada**: edita `portada.tex` con tu universidad, facultad, año y logos.
- **Asesor**: el nombre está en `portada.tex` y en `tesis.tex` (metadatos).
- **Margen de encuadernación**: ajusta `inner` y `outer` en `preamble.tex`.
- **Color institucional**: edita `\definecolor{azulUNAM}` en `preamble.tex`.
- **Idioma del documento**: ya configurado como español
  (`\usepackage[spanish,es-tabla,es-nodecimaldot]{babel}`).

## Convenciones de redacción

- `\cite{clave}` para citas bibliográficas (las entradas viven en `referencias.bib`).
- `\label{cap:nombre}`, `\label{sec:nombre}`, `\label{fig:nombre}`,
  `\label{tab:nombre}` para etiquetas, con prefijo según el tipo.
- `\ref{etiqueta}` para referencias cruzadas.
- Comandos personalizados: `\INS`, `\PLN`, `\NLP`.
- Entornos de teorema en español: `definicion`, `teorema`, `proposicion`,
  `lema`, `corolario`, `ejemplo`, `observacion`.
- Código fuente: usa el entorno `lstlisting` (estilo `python` ya configurado).
