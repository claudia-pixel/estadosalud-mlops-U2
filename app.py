from flask import Flask, render_template, request, jsonify, Response
import datetime
import os
import json
import csv
from io import StringIO

app = Flask(__name__)
LOG_FILE = 'diagnostics.log'

def diagnose(temperature, heart_rate, oxygen_saturation):
    """
    Funciona como sistema de diagnostico simple basado en tres valores.
    """
    if temperature < 35 or temperature > 42 or heart_rate < 40 or heart_rate > 140 or oxygen_saturation < 85:
        return "ENFERMEDAD TERMINAL"
    elif 36 <= temperature < 37.5 and 60 <= heart_rate <= 100 and oxygen_saturation >= 95:
        return "NO ENFERMO"
    elif 37.5 <= temperature < 38.5 and 100 < heart_rate <= 120 and oxygen_saturation >= 92:
        return "ENFERMO LEVE"
    elif temperature >= 38.5 and heart_rate > 120 and oxygen_saturation < 92:
        return "ENFERMEDAD AGUDA"
    elif 37 <= temperature < 38 and 60 <= heart_rate < 100 and oxygen_saturation < 90:
        return "ENFERMEDAD CRÓNICA"
    else:
        return "Valores fuera de rango, consulte a un médico."

def log_diagnosis(temperature, heart_rate, oxygen_saturation, diagnosis):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = {
        'temperatura': temperature,
        'latidos': heart_rate,
        'saturacion': oxygen_saturation,
        'diagnostico': diagnosis,
        'fecha_hora': timestamp
    }
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose_route():
    data = request.get_json()
    temperature = float(data['temperature'])
    heart_rate = int(data['heart_rate'])
    oxygen_saturation = int(data['oxygen_saturation'])

    diagnosis = diagnose(temperature, heart_rate, oxygen_saturation)
    log_diagnosis(temperature, heart_rate, oxygen_saturation, diagnosis)
    return jsonify({'diagnosis': diagnosis})

@app.route('/report')
def report():
    log_data = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            for line in f:
                try:
                    log_data.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    pass

    diagnosis_counts = {}
    for entry in log_data:
        diagnosis = entry['diagnostico']
        diagnosis_counts[diagnosis] = diagnosis_counts.get(diagnosis, 0) + 1

    last_5_predictions = sorted(log_data, key=lambda x: x['fecha_hora'], reverse=True)[:5]
    last_prediction_date = last_5_predictions[0]['fecha_hora'] if last_5_predictions else 'No hay predicciones'

    return render_template('report.html',
                           diagnosis_counts=diagnosis_counts,
                           last_5_predictions=last_5_predictions,
                           last_prediction_date=last_prediction_date)

@app.route('/export_log')
def export_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            log_data = []
            for line in f:
                try:
                    log_data.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    continue

        if log_data:
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(['Fecha y Hora', 'Temperatura', 'Latidos', 'Saturación', 'Diagnóstico'])
            for entry in log_data:
                writer.writerow([entry['fecha_hora'], entry['temperatura'], entry['latidos'], entry['saturacion'], entry['diagnostico']])

            csv_content = output.getvalue()
            response = Response(csv_content, mimetype='text/csv')
            response.headers['Content-Disposition'] = 'attachment; filename=diagnostics.csv'
            return response

    return "No hay registros para exportar."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')