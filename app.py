import streamlit as st
import os
import requests
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

st.title("Repositorio ComUnsam")
st.write("Bienvenidx :student: a nuestro repositorio de textos y apuntes de la carrera de Estudios de la Comunicación de la EH. Desde acá vas poder podrás subir y descargar textos de las distintas materias. Además te brindamos una herramienta de análisis de textos.")

# Definimos las carpetas de categorías
carpetas = ['Metodologías de la investigación', 'Metodologías cualitativas', 'Estudios de recepción y audiencias']
directorio_base = 'subidas'

# Creamos las carpetas si no existen
os.makedirs(directorio_base, exist_ok=True)
for carpeta in carpetas:
    os.makedirs(os.path.join(directorio_base, carpeta), exist_ok=True)

# Diccionario para mantener el registro de textos subidos
registro_textos = {categoria: 0 for categoria in carpetas}

# Función para subir archivos
def upload_file(uploaded_file, categoria_seleccionada):
    if uploaded_file is not None:
        ruta_destino = os.path.join(directorio_base, categoria_seleccionada, uploaded_file.name)
        with open(ruta_destino, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("¡Archivo subido con éxito!")
        # Actualizar el registro de textos subidos
        registro_textos[categoria_seleccionada] += 1
    else:
        st.warning("No has seleccionado ningún archivo.")

# Función para listar archivos y permitir la descarga
def list_files(categoria_seleccionada):
    ruta_categoria = os.path.join(directorio_base, categoria_seleccionada)
    if os.path.exists(ruta_categoria):
        archivos = os.listdir(ruta_categoria)
        return [archivo for archivo in archivos if archivo.endswith('.txt')]
    else:
        return []

# Función para analizar texto con Voyant Tools
def analizar_texto_con_voyant(texto):
    url = "https://voyant-tools.org/"
    params = {
        'input': texto
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        st.write("Análisis completado con Voyant Tools")
        analysis_url = f"https://voyant-tools.org/?corpus={response.text}"
        st.write(f"[Ver análisis completo]({analysis_url})")
        st.components.v1.iframe(analysis_url, height=600, scrolling=True)
    else:
        st.error("Error al analizar el texto con Voyant Tools")

# Función para convertir PDF a texto
def convertir_pdf_a_texto(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    texto = ""
    for page in doc:
        texto += page.get_text()
    return texto

# Función para convertir imagen a texto usando Tesseract
def convertir_imagen_a_texto(uploaded_file):
    image = Image.open(uploaded_file)
    texto = pytesseract.image_to_string(image)
    return texto

# Subida de archivos
st.subheader("Empezar a subir textos :page_facing_up:")
categoria_seleccionada = st.selectbox("Selecciona una materia", carpetas)
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt', 'pdf', 'jpg', 'png'])

if st.button("Subir el archivo seleccionado :heavy_check_mark:"):
    if uploaded_file.type == "application/pdf":
        texto_convertido = convertir_pdf_a_texto(uploaded_file)
        ruta_destino = os.path.join(directorio_base, categoria_seleccionada, uploaded_file.name.replace('.pdf', '.txt'))
        with open(ruta_destino, "w", encoding='utf-8') as f:
            f.write(texto_convertido)
        st.success("¡Archivo PDF convertido y subido con éxito!")
        registro_textos[categoria_seleccionada] += 1
    elif uploaded_file.type in ["image/jpeg", "image/png"]:
        texto_convertido = convertir_imagen_a_texto(uploaded_file)
        ruta_destino = os.path.join(directorio_base, categoria_seleccionada, uploaded_file.name.replace('.jpg', '.txt').replace('.png', '.txt'))
        with open(ruta_destino, "w", encoding='utf-8') as f:
            f.write(texto_convertido)
        st.success("¡Imagen convertida y subida con éxito!")
        registro_textos[categoria_seleccionada] += 1
    else:
        upload_file(uploaded_file, categoria_seleccionada)

# Descarga de archivos
st.subheader("Ver textos:bookmark_tabs:")

for carpeta in carpetas:
    st.caption(f"Textos de {carpeta}")
    archivos_seleccionados = list_files(carpeta)
    if archivos_seleccionados:
        for archivo in archivos_seleccionados:
            ruta_archivo = os.path.join(directorio_base, carpeta, archivo)
            with open(ruta_archivo, 'rb') as file:
                st.download_button(f"Descargar {archivo}", data=file, file_name=archivo)
    else:
        st.warning(f"No hay archivos en la categoría {carpeta}.")

# Análisis de archivos
st.subheader("Analizar textos con Voyant Tools :bar_chart:")
archivo_para_analizar = st.selectbox("Selecciona un archivo para analizar", list_files(categoria_seleccionada))
if st.button("Analizar el archivo seleccionado :mag:"):
    if archivo_para_analizar:
        ruta_archivo = os.path.join(directorio_base, categoria_seleccionada, archivo_para_analizar)
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            texto = file.read()
            analizar_texto_con_voyant(texto)
    else:
        st.warning("No has seleccionado ningún archivo para analizar.")

# Mostrar el registro de textos subidos
st.subheader("Registro de textos subidos :clipboard:")
for categoria, cantidad in registro_textos.items():
    st.write(f"{categoria}: {cantidad} textos subidos")
