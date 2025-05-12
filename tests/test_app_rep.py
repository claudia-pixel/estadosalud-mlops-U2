import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, LOG_FILE
import json

# Define un nombre de archivo de log de prueba
TEST_LOG_FILE = 'test_diagnostics.log'

# Función para crear un archivo de log de prueba con datos específicos
def create_test_log(data):
    with open(TEST_LOG_FILE, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry) + '\n')

# Limpiar el archivo de log de prueba después de cada prueba que lo use
@pytest.fixture(autouse=True)
def cleanup_log_file():
    yield
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)

def test_report_diagnosis_counts(monkeypatch):
    monkeypatch.setattr('app.LOG_FILE', TEST_LOG_FILE)
    test_data = [
        {'diagnostico': 'NO ENFERMO', 'fecha_hora': '2025-05-10T10:00:00'},
        {'diagnostico': 'ENFERMO LEVE', 'fecha_hora': '2025-05-10T10:05:00'},
        {'diagnostico': 'NO ENFERMO', 'fecha_hora': '2025-05-10T10:10:00'},
        {'diagnostico': 'ENFERMEDAD AGUDA', 'fecha_hora': '2025-05-10T10:15:00'},
    ]
    create_test_log(test_data)
    with app.test_client() as client:
        response = client.get('/report')
        assert response.status_code == 200
        response_text = response.data.decode('utf-8')
        assert 'Número de Diagnósticos por Resultado' in response_text
        assert 'NO ENFERMO: 2' in response_text
        assert 'ENFERMO LEVE: 1' in response_text
        assert 'ENFERMEDAD AGUDA: 1' in response_text

def test_report_last_5_predictions(monkeypatch):
    monkeypatch.setattr('app.LOG_FILE', TEST_LOG_FILE)
    test_data = [
        {'diagnostico': 'D1', 'fecha_hora': '2025-05-10T10:01:00', 'temperatura': 36.5, 'latidos': 80, 'saturacion': 98},
        {'diagnostico': 'D2', 'fecha_hora': '2025-05-10T10:02:00', 'temperatura': 37.8, 'latidos': 110, 'saturacion': 93},
        {'diagnostico': 'D3', 'fecha_hora': '2025-05-10T10:03:00', 'temperatura': 39.0, 'latidos': 130, 'saturacion': 88},
        {'diagnostico': 'D4', 'fecha_hora': '2025-05-10T10:04:00', 'temperatura': 37.2, 'latidos': 75, 'saturacion': 88},
        {'diagnostico': 'D5', 'fecha_hora': '2025-05-10T10:05:00', 'temperatura': 34.0, 'latidos': 70, 'saturacion': 95},
        {'diagnostico': 'D6', 'fecha_hora': '2025-05-10T10:06:00', 'temperatura': 43.0, 'latidos': 70, 'saturacion': 95},
    ]
    create_test_log(test_data)
    with app.test_client() as client:
        response = client.get('/report')
        assert response.status_code == 200
        response_text = response.data.decode('utf-8')
        assert 'Últimas 5 Predicciones' in response_text
        assert 'D6' in response_text
        assert 'D5' in response_text
        assert 'D4' in response_text
        assert 'D3' in response_text
        assert 'D2' in response_text
        # Cambiado de 'D1' en cualquier parte del texto a '<td>D1</td>' en la tabla
        assert '<td>D1</td>' not in response_text  # Asegura que D1 no esté en las últimas 5 predicciones

def test_report_last_prediction_date(monkeypatch):
    monkeypatch.setattr('app.LOG_FILE', TEST_LOG_FILE)
    test_data = [
        {'diagnostico': 'A', 'fecha_hora': '2025-05-10T09:59:00'},
        {'diagnostico': 'B', 'fecha_hora': '2025-05-10T10:01:00'},
    ]
    create_test_log(test_data)
    with app.test_client() as client:
        response = client.get('/report')
        assert response.status_code == 200
