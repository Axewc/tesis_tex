"""
Calculador del Índice de Neutralidad Sociolectal (INS).

Implementación de referencia descrita en el Capítulo 5 de la tesis
(Código 5.1). Las funciones de cálculo están separadas de la evaluación
del modelo: reciben salidas ya computadas, lo que permite probarlas
unitariamente y recalcular el índice sin repetir las 2N invocaciones.

Uso típico:
    from ins_calculator import calcular_ins_dec, calcular_ins_prob

    pares_dec = [("apto", "apto"), ("apto", "no apto")]
    ins = calcular_ins_dec(pares_dec)
"""

import numpy as np

__all__ = [
    "divergencia_js",
    "calcular_ins_dec",
    "calcular_ins_prob",
    "ins_por_variacion",
]


def divergencia_js(p, q, base=2.0):
    """Divergencia de Jensen-Shannon entre dos distribuciones discretas.

    Con base 2, el resultado queda acotado en [0, 1]: vale 0 para
    distribuciones idénticas y 1 para soportes disjuntos.
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p = p / p.sum()
    q = q / q.sum()
    m = 0.5 * (p + q)

    def kl(a, b):
        mascara = a > 0  # m > 0 donde a > 0: el cociente es seguro
        return float(
            np.sum(a[mascara] * (np.log(a[mascara] / b[mascara]) / np.log(base)))
        )

    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def calcular_ins_dec(pares):
    """INS de decisión (Definición 5.2 de la tesis).

    `pares` es una lista de tuplas (y, y_prima) con las decisiones del
    modelo para cada par controlado. Devuelve la proporción de pares con
    decisión coincidente, en [0, 1].
    """
    if not pares:
        raise ValueError("Benchmark vacío: el INS no está definido.")
    return sum(int(y == yp) for y, yp in pares) / len(pares)


def calcular_ins_prob(pares, base=2.0):
    """INS probabilístico (Definición 5.3 de la tesis).

    `pares` es una lista de tuplas (p, p_prima) con las distribuciones
    posteriores del modelo para cada par controlado.
    """
    if not pares:
        raise ValueError("Benchmark vacío: el INS no está definido.")
    total = sum(divergencia_js(p, q, base) for p, q in pares)
    return 1.0 - total / len(pares)


def ins_por_variacion(registros):
    """INS de decisión desagregado por tipo de variación lingüística.

    `registros` es un iterable de tuplas (tipo, y, y_prima). Devuelve un
    diccionario {tipo: INS_dec del subconjunto}.
    """
    grupos = {}
    for tipo, y, yp in registros:
        grupos.setdefault(tipo, []).append((y, yp))
    return {t: calcular_ins_dec(ps) for t, ps in grupos.items()}
