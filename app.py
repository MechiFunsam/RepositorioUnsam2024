import streamlit as st
import os

st.title("Repositorio ComUnsam")
st.write("Bienvenidx :student: a nuestro repositorio de textos y apuntes de la carrera de Estudios de la Comunicación de la EH. Desde acá vas poder podrás subir y descargar textos de las distintas materias. Además te brindamos una herramienta de análisis de textos.")

# Definimos las carpetas de categorías
carpetas = ['Metodologías de la investigación', 'Metodologías cualitativas', 'Estudios de recepción y audiencias']
directorio_base = 'subidas'

# Creamos las carpetas si no existen
os.makedirs(directorio_base, exist_ok=True)
for carpeta in carpetas:
    os.makedirs(os.path.join(directorio_base, carpeta), exist_ok=True)

# Función para subir archivos
def upload_file(uploaded_file, categoria_seleccionada):
    if uploaded_file is not None:
        ruta_destino = os.path.join(directorio_base, categoria_seleccionada, uploaded_file.name)
        with open(ruta_destino, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("¡Archivo subido con éxito!")
    else:
        st.warning("No has seleccionado ningún archivo.")

# Función para listar archivos y permitir la descarga
def list_files(categoria_seleccionada):
    ruta_categoria = os.path.join(directorio_base, categoria_seleccionada)
    if os.path.exists(ruta_categoria):
        archivos = os.listdir(ruta_categoria)
        return archivos
    else:
        return []

# Subida de archivos
st.subheader("Empezar a subir textos :page_facing_up:")
categoria_seleccionada = st.selectbox("Selecciona una materia", carpetas)
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt', 'csv', 'jpg', 'png', 'pdf'])

if st.button("Subir el archivo seleccionado :heavy_check_mark:"):
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