import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import diagnose

def test_no_enfermo():
    assert diagnose(36.5, 80, 98) == "NO ENFERMO"

def test_enfermo_leve():
    assert diagnose(37.8, 110, 93) == "ENFERMO LEVE"

def test_enfermedad_aguda():
    assert diagnose(39.0, 130, 88) == "ENFERMEDAD AGUDA"

def test_enfermedad_cronica():
    assert diagnose(37.2, 75, 88) == "ENFERMEDAD CRÓNICA"

def test_enfermedad_terminal_temperatura_baja():
    assert diagnose(34.0, 70, 95) == "ENFERMEDAD TERMINAL"

def test_enfermedad_terminal_temperatura_alta():
    assert diagnose(43.0, 70, 95) == "ENFERMEDAD TERMINAL"

def test_enfermedad_terminal_ritmo_cardiaco_bajo():
    assert diagnose(37.0, 35, 95) == "ENFERMEDAD TERMINAL"

def test_enfermedad_terminal_ritmo_cardiaco_alto():
    assert diagnose(37.0, 150, 95) == "ENFERMEDAD TERMINAL"

def test_enfermedad_terminal_saturacion_baja():
    assert diagnose(37.0, 80, 80) == "ENFERMEDAD TERMINAL"

def test_fuera_de_rango():
    assert diagnose(35.5, 55, 90) == "Valores fuera de rango, consulte a un médico."