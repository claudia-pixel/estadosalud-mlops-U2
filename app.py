
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def diagnose(temperature, heart_rate, oxygen_saturation):
    if 36 <= temperature < 37.5 and 60 <= heart_rate <= 100 and oxygen_saturation >= 95:
        return "NO ENFERMO"
    elif 37.5 <= temperature < 38.5 and 100 < heart_rate <= 120 and oxygen_saturation >= 92:
        return "ENFERMO LEVE"
    elif temperature >= 38.5 and heart_rate > 120 and oxygen_saturation < 92:
        return "ENFERMEDAD AGUDA"
    elif 37 <= temperature < 38 and 60 <= heart_rate < 100 and oxygen_saturation < 90:
        return "ENFERMEDAD CRÓNICA"
    else:
        return "Valores fuera de rango, consulte a un médico."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose_route():
    data = request.json
    temperature = float(data['temperature'])
    heart_rate = int(data['heart_rate'])
    oxygen_saturation = int(data['oxygen_saturation'])
    
    result = diagnose(temperature, heart_rate, oxygen_saturation)
    return jsonify({'diagnosis': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
