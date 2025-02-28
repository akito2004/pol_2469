from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

# Inicializa la aplicación Flask
app = Flask(__name__)

# Ejercicio 1: Crear un DataFrame de Pandas
@app.route('/dataframe', methods=['GET', 'POST'])
def create_dataframe():
    """
    Crea un DataFrame de Pandas con información de personas y lo muestra en una tabla HTML.
    - Si la solicitud es POST, se genera el DataFrame y se renderiza en la plantilla.
    - Si la solicitud es GET, simplemente se muestra la página con el formulario.
    """
    if request.method == 'POST':
        data = {
            "Nombre": ["Ana", "Juan", "Luis", "Maria"],
            "Edad": [23, 34, 45, 29],
            "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
        }
        df = pd.DataFrame(data)
        return render_template('dataframe.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('dataframe.html')

# Ejercicio 2: Operaciones NumPy - Sumar dos matrices
@app.route('/sumar_matrices', methods=['GET', 'POST'])
def sumar_matrices():
    """
    Suma dos matrices de NumPy y muestra el resultado en la plantilla.
    - Si la solicitud es POST, se suman dos matrices predefinidas.
    - Si la solicitud es GET, se muestra la página con el formulario.
    """
    if request.method == 'POST':
        matriz1 = np.array([[1, 2], [3, 4]])
        matriz2 = np.array([[5, 6], [7, 8]])
        suma = np.add(matriz1, matriz2)
        return render_template('sumar_matrices.html', resultado=suma.tolist())
    return render_template('sumar_matrices.html')

# Ejercicio 3: Promedio de una columna en Pandas
@app.route('/promedio_edad', methods=['GET', 'POST'])
def promedio_edad():
    """
    Calcula el promedio de una lista de edades con NumPy.
    - Si la solicitud es POST, se calcula el promedio y se muestra.
    - Si la solicitud es GET, se muestra la página con el formulario.
    """
    if request.method == 'POST':
        edades = np.array([23, 34, 45, 29])
        promedio = np.mean(edades)
        return render_template('promedio_edad.html', promedio=promedio)
    return render_template('promedio_edad.html')

# Ejercicio 4: Generar números aleatorios con NumPy
@app.route('/numeros_aleatorios', methods=['GET', 'POST'])
def numeros_aleatorios():
    """
    Genera una lista de 5 números aleatorios entre 1 y 100 con NumPy.
    - Si la solicitud es POST, se generan los números y se muestran en la plantilla.
    - Si la solicitud es GET, se muestra la página con el formulario.
    """
    if request.method == 'POST':
        numeros = np.random.randint(1, 100, size=5)
        return render_template('numeros_aleatorios.html', numeros=numeros.tolist())
    return render_template('numeros_aleatorios.html')

# Ejecuta la aplicación en modo depuración si este script se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
