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
st.write("Haz clic en 'Iniciar' para comenzar a generar palabras. Cada 5 segundos aparecerá una nueva palabra en pantalla.")

# Espacio donde se mostrará la palabra
palabra_display = st.empty()

# Control de inicio y detención
if 'running' not in st.session_state:
    st.session_state.running = False

# Función para controlar el estado de la generación
def iniciar():
    st.session_state.running = True

def detener():
    st.session_state.running = False

# Botones de iniciar y detener
col1, col2 = st.columns(2)

with col1:
    if st.button('Iniciar'):
        iniciar()

with col2:
    if st.button('Detener'):
        detener()

# Bucle para cambiar la palabra cada 5 segundos si está en modo "iniciar"
while st.session_state.running:
    palabra = generar_palabra()
    # Mostrar la palabra en un tamaño mucho mayor (tamaño 72px)
    palabra_display.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{palabra}</h1>", unsafe_allow_html=True)
    time.sleep(5)






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
