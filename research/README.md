# research/ — lado técnico de la tesis

Código, datos y experimentos. La tesis (LaTeX) vive en `../tesis/`.

## Estructura
- `scripts/` — código de producción (limpio, probado)
  - `ins_calculator.py` — calculador del INS (Cap. 5 de la tesis)
- `tests/` — pruebas unitarias (`python3 -m pytest research/tests/ -v`)
- `data/` — datos crudos y procesados (**no se versiona**: ver .gitignore raíz)
- `notebooks/` — exploración en Jupyter
- `results/` — salidas, figuras, benchmarks calculados

## Entorno
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Regla de oro
`data/` queda fuera de Git por diseño: contiene respuestas de encuesta.
Aunque son anónimas, no se publican datos crudos de participantes
(ver Sección 3.6 de la tesis). Respaldar `data/` por separado.
