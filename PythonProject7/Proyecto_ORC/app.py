
from flask import Flask, render_template, Response, jsonify
import cv2
import pytesseract
import pyttsx3
import re
from textblob import TextBlob
import threading

app = Flask(__name__)

# Configurar Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Alumno.LAB102-02\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe'

# Inicializar la cámara
camera = cv2.VideoCapture(0)

# Configurar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de lectura

# Variable global para almacenar el texto extraído
texto_extraido = ""


def limpiar_texto(texto):
    """ Limpia el texto eliminando caracteres especiales y corrige errores. """
    texto = re.sub(r'[^A-Za-z0-9áéíóúüñÁÉÍÓÚÜÑ ]+', '', texto)  # Elimina caracteres extraños
    texto = str(TextBlob(texto).correct())  # Corrige errores ortográficos (opcional)
    return texto.strip()


def reproducir_audio(texto):
    """ Reproduce el texto extraído en voz alta en un hilo separado. """
    engine.say(texto)
    engine.runAndWait()


def generar_frames():
    global texto_extraido
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, binarizada = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY)
            nuevo_texto = pytesseract.image_to_string(binarizada, lang='eng')
            texto_limpio = limpiar_texto(nuevo_texto)

            if texto_limpio and texto_limpio != texto_extraido:  # Evitar repetir la misma lectura
                texto_extraido = texto_limpio
                print("Texto detectado:", texto_extraido)
                threading.Thread(target=reproducir_audio, args=(texto_extraido,)).start()

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generar_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/detener_audio')
def detener_audio():
    engine.stop()
    return jsonify({"mensaje": "Lectura detenida"})


@app.route('/get_text')
def get_text():
    return jsonify({"texto": texto_extraido})


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
