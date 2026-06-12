"""Pruebas unitarias del calculador del INS.

Ejecutar con:  python3 -m pytest research/tests/  (o python3 research/tests/test_ins.py)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import pytest
from ins_calculator import (
    divergencia_js, calcular_ins_dec, calcular_ins_prob, ins_por_variacion,
)


def test_consistencia_perfecta_da_uno():
    assert calcular_ins_dec([("a", "a"), ("b", "b")]) == 1.0


def test_inversion_total_da_cero():
    assert calcular_ins_dec([("a", "b"), ("b", "a")]) == 0.0


def test_ejemplo_de_la_tesis():
    # Tabla 5.x: 3 de 4 pares coinciden
    pares = [("apto", "apto"), ("apto", "no apto"),
             ("no apto", "no apto"), ("apto", "apto")]
    assert calcular_ins_dec(pares) == 0.75


def test_jsd_acotada_base2():
    assert divergencia_js([0.5, 0.5], [0.5, 0.5]) == pytest.approx(0.0)
    assert divergencia_js([1, 0], [0, 1]) == pytest.approx(1.0)


def test_jsd_ejemplo_probabilistico_de_la_tesis():
    # (0.91, 0.09) vs (0.62, 0.38) -> ~0.089
    assert divergencia_js([0.91, 0.09], [0.62, 0.38]) == pytest.approx(0.0894, abs=1e-3)


def test_ins_prob_perfecto():
    assert calcular_ins_prob([([0.9, 0.1], [0.9, 0.1])]) == pytest.approx(1.0)


def test_desagregado_por_variacion():
    regs = [("ortografia", "a", "b"), ("ortografia", "a", "a"),
            ("anglicismos", "a", "a")]
    out = ins_por_variacion(regs)
    assert out == {"ortografia": 0.5, "anglicismos": 1.0}


def test_benchmark_vacio_falla_explicitamente():
    with pytest.raises(ValueError):
        calcular_ins_dec([])
    with pytest.raises(ValueError):
        calcular_ins_prob([])


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
