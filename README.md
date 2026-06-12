# Sesgo socioeconómico en modelos de clasificación automática de texto

Tesis de Licenciatura en Ciencias de la Computación · UNAM, Facultad de Ciencias
**Autor:** Axel Casas Espinosa · **Asesor:** M. en C.I.C. Manuel Soto Romero

Proyecto técnico documentado: se construye un *benchmark* de pares controlados
(mismo contenido, distinto registro lingüístico), se evalúan clasificadores de
texto en español y se propone el **Índice de Neutralidad Sociolectal (INS)**.

## Estructura

```
tesis_tex/
├── tesis/      ← documento LaTeX (compilar tesis/tesis.tex)
└── research/   ← código, datos y experimentos (Python)
```

Cada rama tiene su propio README con instrucciones.

## Flujo de trabajo

- **Redacción** (`tesis/`): se edita en Prism (workspace LaTeX en nube).
  Periódicamente se descarga el proyecto y se commitea aquí como respaldo
  y registro de versiones.
- **Código** (`research/`): se edita localmente (VS Code / Claude Code) y
  se commitea directamente. Correr pruebas antes de cada commit:
  `python3 -m pytest research/tests/ -v`
- **Roadmap**: tablero Kanban en Notion ("Tesis — Roadmap (Sesgo Sociolectal)"),
  30+ tareas en 7 fases con dependencias.

## Estado

- [x] Plantilla LaTeX completa (compila; ver `tesis/README.md`)
- [x] Cap. 1 redactado · Cap. 2 redactado (pendiente verificación de fuentes)
- [x] Cap. 3: secciones 3.3 y 3.6 redactadas · Cap. 5: 5.1–5.3 y 5.5 redactadas
- [x] Instrumento de encuesta diseñado (Apéndice A) + calculador del INS probado
- [ ] Encuesta (validación con asesor → piloto → aplicación)
- [ ] Benchmark de pares controlados → evaluación → INS sobre datos reales
- [ ] Caps. 4, 6, 7 (esperan resultados)

Las marcas `[DECIDIR]`, `[PENDIENTE]`, `[VERIFICAR]` y `[FUENTE MX]` dentro de
los `.tex` señalan trabajo abierto; buscarlas todas antes de la entrega.
