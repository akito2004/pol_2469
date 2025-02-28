from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def analizar_datos(filepath):
    df = pd.read_csv(filepath)

    # Estadísticas básicas
    stats = df.describe().to_dict()

    # Detección de valores atípicos usando el rango intercuartil
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum().to_dict()

    return {"stats": stats, "outliers": outliers}


def simulacion_montecarlo(retornos, num_simulaciones=1000, dias=30):
    media = np.mean(retornos)
    desviacion = np.std(retornos)
    simulaciones = np.random.normal(media, desviacion, (num_simulaciones, dias))
    return simulaciones.tolist()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)
    result = analizar_datos(filepath)

    # Simulación de Monte Carlo sobre la primera columna numérica
    columna_numerica = df.select_dtypes(include=[np.number]).columns[0]
    simulaciones = simulacion_montecarlo(df[columna_numerica].dropna())

    result["montecarlo"] = simulaciones
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
