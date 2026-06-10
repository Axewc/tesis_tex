"""
Script de ejemplo para generar figuras para la tesis.
Ejecutar: python scripts/generate_figures.py
Las figuras se guardan en el directorio figures/
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Directorio de salida
OUTPUT_DIR = Path(__file__).parent.parent / "figures"
OUTPUT_DIR.mkdir(exist_ok=True)


def example_plot():
    """Genera una figura de ejemplo."""
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, label=r"$\sin(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Figura de ejemplo")
    ax.legend()
    ax.grid(True)

    output_path = OUTPUT_DIR / "example_plot.pdf"
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Figura guardada en: {output_path}")


if __name__ == "__main__":
    example_plot()
