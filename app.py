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
@@ -40,24 +46,55 @@ def list_files(categoria_seleccionada):

# Función para analizar texto con Voyant Tools
def analizar_texto_con_voyant(texto):
    url = "https://voyant-tools.org/tool/Cirrus/"
    url = "https://voyant-tools.org/"
    params = {
        'input': texto
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        st.write("Análisis completado con Voyant Tools")
        st.write(response.url)
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
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt'])
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt', 'pdf', 'jpg', 'png'])

if st.button("Subir el archivo seleccionado :heavy_check_mark:"):
    upload_file(uploaded_file, categoria_seleccionada)
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
