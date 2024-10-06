import streamlit as st
import time
import random

# Lista de palabras para freestyle
palabras = [
    'ritmo', 'verso', 'micrófono', 'calle', 'flow', 'estilo', 'sonido', 
    'música', 'improvisación', 'letras', 'batalla', 'rima', 'compás', 
    'melodía', 'arte', 'escenario', 'público', 'vibración', 'sentimiento'
]

# Función para generar una palabra aleatoria
def generar_palabra():
    return random.choice(palabras)

# Configuración de la página
st.title("Generador de palabras para Freestyle")

# Texto de introducción
st.write("Cada 5 segundos aparecerá una nueva palabra para que puedas improvisar.")

# Espacio donde se mostrará la palabra
palabra_display = st.empty()

# Bucle para cambiar la palabra cada 5 segundos
while True:
    palabra = generar_palabra()
    palabra_display.write(f"Palabra: **{palabra}**")
    time.sleep(5)
