 if os.path.exists('textos.json'):  
 with open('textos.json', 'r') as f:  
 return json.load(f)  
 return []  

# Función para guardar textos en un archivodef guardar_textos(textos):  
 with open('textos.json', 'w') as f:  
 json.dump(textos, f)  

# Cargar textos al iniciotextos = cargar_textos()  

# Interfaz de usuariost.title("Repositorio de Textos")  
nuevo_texto = st.text_area("Escribe tu texto aquí:")  
if st.button("Guardar"):  
 if nuevo_texto:  
 textos.append(nuevo_texto)  
 guardar_textos(textos)  
 st.success("Texto guardado!")  

# Mostrar textos guardadosif textos:  
 st.write("Textos guardados:")  
 for texto in textos:  
 st.write(texto)  
###2. Uso de una base de datos

Si planeas hacer más cosas en el futuro o almacenar muchos textos, es posible que quieras usar una base de datos. Puedes usar SQLite para una solución ligera o PostgreSQL si necesitas algo más robusto.

Aquí tienes un ejemplo usando SQLite:

pythonimport
c = conn.cursor()  

# Crear la tabla si no existec.execute('CREATE TABLE IF NOT EXISTS textos (texto TEXT)')  

# Funciones para guardar y cargar textosdef guardar_texto(nuevo_texto):  
 c.execute('INSERT INTO textos (texto) VALUES (?)', (nuevo_texto,))  
 conn.commit()  

def cargar_textos():  
 c.execute('SELECT texto FROM textos')  
 return c.fetchall()  

# Interfaz de usuariost.title("Repositorio de Textos")  
nuevo_texto = st.text_area("Escribe tu texto aquí:")  
if st.button("Guardar"):  
 if nuevo_texto:  
 guardar_texto(nuevo_texto)  
 st.success("Texto guardado!")  

# Mostrar textos guardadostextos = cargar_textos()  
if textos:  
 st.write("Textos guardados:")  
 for texto in textos:  
 st.write(texto[0])  
###3. Almacenar en GitHub

Si realmente quieres que los textos se almacenan en GitHub, tendrías que implementar una lógica para hacer push a tu repo cada vez que cambie el contenido. Esto podría complicarse un poco, ya que necesitarías configurar autenticación y manejar errores.

###4. Uso de servicios de backend

Si prefieres no manejar la persistencia tú mismo, puedes utilizar servicios de backend como Firebase, Supabase, o Zapier, que te permitirán almacenar datos y acceder a ellos fácilmente.

ConclusionesDependiendo de tus necesidades y la complejidad de tu app, puedes elegir entre estas soluciones. Para algo sencillo, el uso de archivos es una buena opción, mientras que para aplicaciones más complejas, una base de datos sería mejor. ¡Espero que esto te ayude a avanzar en tu proyecto! Si tienes más preguntas, no dudes en preguntar.
te puedo pasar el codigo que tengo y que agregues lo edites?
GPT-4o mini
¡Claro! Por favor, comparte el código que tienes hasta ahora y estaré encantado de ayudarte a editarlo para que los textos se guarden adecuadamente.

1 2345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091 importar iluminado por el sol como calle importar sistema operativo importar solicitudes calle.título("Repositorio ComUnsam") calle.escribir("Bienvenidx :student: a nuestro repositorio de textos y apuntes de la carrera de Estudios de la Comunicación de la EH. Desde acá vas poder subir y descargar textos de las distintas materias. Además te brindamos una herramienta de análisis de textos.") # Definimos las carpetas de categorías carpetas =['Metodologías de la investigación','Metodologías cualitativas','Estudios de recepción y audiencias'] directorio_base = 'subidas' # Creamos las carpetas si no existen sistema operativo.hacerdirectores(directorio_base,existe_ok=Verdadero) para carpeta en carpetas: sistema operativo.hacerdirectores(sistema operativo.camino.unirse(directorio_base,carpeta),existe_ok=Verdadero) # Diccionario para mantener el registro de textos subidos registro_textos ={categoria:0 para categoria en carpetas} # Función para subir archivos definición subir_archivo(archivo cargado,categoria_seleccionada): si archivo cargado es no Ninguno: ruta_destino = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada,archivo cargado.nombre) con abierto(ruta_destino,"blanco y negro")como F: F.escribir(archivo cargado.obtener búfer()) calle.éxito("¡Archivo subido con éxito!") # Actualizar el registro de textos subidos registro_textos[categoria_seleccionada]+= 1 demás: calle.advertencia("No has seleccionado ningún archivo.") # Función para listar archivos y permitir la descarga definición lista_archivos(categoria_seleccionada): ruta_categoria = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada) si sistema operativo.camino.existe(ruta_categoria): archivos = sistema operativo.directorio de lista(ruta_categoria) devolver[archivo para archivo en archivos si archivo.termina con('.TXT')] demás: devolver[] # Función para analizar texto con Voyant Tools definición analizar_texto_con_voyant(texto): dirección URL = "https://voyant-tools.org/tool/Cirrus/" parámetros ={ 'aporte':texto } respuesta = solicitudes.correo(dirección URL,datos=parámetros) si respuesta.código de estado == 200: calle.escribir("Análisis completado con Voyant Tools") calle.escribir(respuesta.dirección URL) demás: calle.error("Error al analizar el texto con Voyant Tools") # Subida de archivos calle.subtítulo("Empezar a subir textos :page_facing_up:") categoria_seleccionada = calle.cuadro de selección("Selecciona una materia",carpetas) archivo cargado = calle.cargador de archivos("Selecciona el texto de la materia seleccionada",tipo=['TXT']) si calle.botón("Subir el archivo seleccionado :heavy_check_mark:"): subir_archivo(archivo cargado,categoria_seleccionada) # Descarga de archivos calle.subtítulo("Ver textos:bookmark_tabs:") para carpeta en carpetas: calle.subtítulo(f"Textos de{carpeta}") archivos_seleccionados = lista_archivos(carpeta) si archivos_seleccionados: para archivo en archivos_seleccionados: ruta_archivo = sistema operativo.camino.unirse(directorio_base,carpeta,archivo) con abierto(ruta_archivo,'rb')como archivo: calle.botón de descarga(f"Descargar{archivo}",datos=archivo,Nombre del archivo=archivo) demás: calle.advertencia(f"No hay archivos en la categoría{carpeta}.") # Análisis de archivos calle.subtítulo("Analizar textos con Voyant Tools :bar_chart:") archivo_para_analizar = calle.cuadro de selección("Selecciona un archivo para analizar",lista_archivos(categoria_seleccionada)) si calle.botón("Analizar el archivo seleccionado :mag:"): si archivo_para_analizar: ruta_archivo = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada,archivo_para_analizar) con abierto(ruta_archivo,'o',codificación='utf-8')como archivo: texto = archivo.leer() analizar_texto_con_voyant(texto) demás: calle.advertencia("No ha seleccionado ningún archivo para analizar.") # Mostrar el registro de textos subidos calle.subtítulo("Registro de textos subidos :clipboard:") para categoria,cantidad en registro_textos.elementos(): calle.escribir(F"{categoria}:{cantidad}"textos subidos")
1 2345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091 importar iluminado por el sol como calle importar sistema operativo importar solicitudes calle.título("Repositorio ComUnsam") calle.escribir("Bienvenidx :student: a nuestro repositorio de textos y apuntes de la carrera de Estudios de la Comunicación de la EH. Desde acá vas poder subir y descargar textos de las distintas materias. Además te brindamos una herramienta de análisis de textos.") # Definimos las carpetas de categorías carpetas =['Metodologías de la investigación','Metodologías cualitativas','Estudios de recepción y audiencias'] directorio_base = 'subidas' # Creamos las carpetas si no existen sistema operativo.hacerdirectores(directorio_base,existe_ok=Verdadero) para carpeta en carpetas: sistema operativo.hacerdirectores(sistema operativo.camino.unirse(directorio_base,carpeta),existe_ok=Verdadero) # Diccionario para mantener el registro de textos subidos registro_textos ={categoria:0 para categoria en carpetas} # Función para subir archivos definición subir_archivo(archivo cargado,categoria_seleccionada): si archivo cargado es no Ninguno: ruta_destino = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada,archivo cargado.nombre) con abierto(ruta_destino,"blanco y negro")como F: F.escribir(archivo cargado.obtener búfer()) calle.éxito("¡Archivo subido con éxito!") # Actualizar el registro de textos subidos registro_textos[categoria_seleccionada]+= 1 demás: calle.advertencia("No has seleccionado ningún archivo.") # Función para listar archivos y permitir la descarga definición lista_archivos(categoria_seleccionada): ruta_categoria = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada) si sistema operativo.camino.existe(ruta_categoria): archivos = sistema operativo.directorio de lista(ruta_categoria) devolver[archivo para archivo en archivos si archivo.termina con('.TXT')] demás: devolver[] # Función para analizar texto con Voyant Tools definición analizar_texto_con_voyant(texto): dirección URL = "https://voyant-tools.org/tool/Cirrus/" parámetros ={ 'aporte':texto } respuesta = solicitudes.correo(dirección URL,datos=parámetros) si respuesta.código de estado == 200: calle.escribir("Análisis completado con Voyant Tools") calle.escribir(respuesta.dirección URL) demás: calle.error("Error al analizar el texto con Voyant Tools") # Subida de archivos calle.subtítulo("Empezar a subir textos :page_facing_up:") categoria_seleccionada = calle.cuadro de selección("Selecciona una materia",carpetas) archivo cargado = calle.cargador de archivos("Selecciona el texto de la materia seleccionada",tipo=['TXT']) si calle.botón("Subir el archivo seleccionado :heavy_check_mark:"): subir_archivo(archivo cargado,categoria_seleccionada) # Descarga de archivos calle.subtítulo("Ver textos:bookmark_tabs:") para carpeta en carpetas: calle.subtítulo(f"Textos de{carpeta}") archivos_seleccionados = lista_archivos(carpeta) si archivos_seleccionados: para archivo en archivos_seleccionados: ruta_archivo = sistema operativo.camino.unirse(directorio_base,carpeta,archivo) con abierto(ruta_archivo,'rb')como archivo: calle.botón de descarga(f"Descargar{archivo}",datos=archivo,Nombre del archivo=archivo) demás: calle.advertencia(f"No hay archivos en la categoría{carpeta}.") # Análisis de archivos calle.subtítulo("Analizar textos con Voyant Tools :bar_chart:") archivo_para_analizar = calle.cuadro de selección("Selecciona un archivo para analizar",lista_archivos(categoria_seleccionada)) si calle.botón("Analizar el archivo seleccionado :mag:"): si archivo_para_analizar: ruta_archivo = sistema operativo.camino.unirse(directorio_base,categoria_seleccionada,archivo_para_analizar) con abierto(ruta_archivo,'o',codificación='utf-8')como archivo: texto = archivo.leer() analizar_texto_con_voyant(texto) demás: calle.advertencia("No ha seleccionado ningún archivo para analizar.") # Mostrar el registro de textos subidos calle.subtítulo("Registro de textos subidos :clipboard:") para categoria,cantidad en registro_textos.elementos(): calle.escribir(F"{categoria}:{cantidad}"textos subidos")
import streamlit as st
import os
import requests

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
    url = "https://voyant-tools.org/tool/Cirrus/"
    params = {
        'input': texto
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        st.write("Análisis completado con Voyant Tools")
        st.write(response.url)
    else:
        st.error("Error al analizar el texto con Voyant Tools")

# Subida de archivos
st.subheader("Empezar a subir textos :page_facing_up:")
categoria_seleccionada = st.selectbox("Selecciona una materia", carpetas)
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt'])

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
GPT-4o mini
Entiendo que quieres incorporar la funcionalidad de guardar los textos subidos en tu aplicación de Streamlit. A continuación, he modificado tu código para que funcione correctamente, además de incorporar la funcionalidad de guardar registros de los textos subidos en un archivo JSON que se actualizará cada vez que se suba un nuevo texto.

Aquí está tu código editado:

pythonimport
st.write("Bienvenidx :student: a nuestro repositorio de textos y apuntes de la carrera de Estudios de la Comunicación de la EH. Desde acá vas poder subir y descargar textos de las distintas materias. Además te brindamos una herramienta de análisis de textos.")  

# Definimos las carpetas de categoríascarpetas = ['Metodologías de la investigación', 'Metodologías cualitativas', 'Estudios de recepción y audiencias']  
directorio_base = 'subidas'  

# Creamos las carpetas si no existenos.makedirs(directorio_base, exist_ok=True)  
for carpeta in carpetas:  
 os.makedirs(os.path.join(directorio_base, carpeta), exist_ok=True)  

# Diccionario para mantener el registro de textos subidosdef cargar_registro():  
 if os.path.exists('registro_textos.json'):  
 with open('registro_textos.json', 'r') as f:  
 return json.load(f)  
 return {categoria:0 for categoria in carpetas}  

def guardar_registro(registro):  
 with open('registro_textos.json', 'w') as f:  
 json.dump(registro, f)  

registro_textos = cargar_registro()  

# Función para subir archivosdef upload_file(uploaded_file, categoria_seleccionada):  
 if uploaded_file is not None:  
 ruta_destino = os.path.join(directorio_base, categoria_seleccionada, uploaded_file.name)  
 with open(ruta_destino, "wb") as f:  
 f.write(uploaded_file.getbuffer())  
 st.success("¡Archivo subido con éxito!")  
 # Actualizar el registro de textos subidos registro_textos[categoria_seleccionada] +=1 guardar_registro(registro_textos)  
 else:  
 st.warning("No has seleccionado ningún archivo.")  

# Función para listar archivos y permitir la descargadef list_files(categoria_seleccionada):  
 ruta_categoria = os.path.join(directorio_base, categoria_seleccionada)  
 if os.path.exists(ruta_categoria):  
 archivos = os.listdir(ruta_categoria)  
 return [archivo for archivo in archivos if archivo.endswith('.txt')]  
 else:  
 return []  

# Función para analizar texto con Voyant Toolsdef analizar_texto_con_voyant(texto):  
 url = "https://voyant-tools.org/tool/Cirrus/"  
 params = {'input': texto}  
 response = requests.post(url, data=params)  
 if response.status_code ==200:  
 st.write("Análisis completado con Voyant Tools")  
 st.write(response.url)  
 else:  
 st.error("Error al analizar el texto con Voyant Tools")  

# Subida de archivosst.subheader("Empezar a subir textos :page_facing_up:")  
categoria_seleccionada = st.selectbox("Selecciona una materia", carpetas)  
uploaded_file = st.file_uploader("Selecciona el texto de la materia seleccionada", type=['txt'])  

if st.button("Subir el archivo seleccionado :heavy_check_mark:"):  
 upload_file(uploaded_file, categoria_seleccionada)  

# Descarga de archivosst.subheader("Ver textos:bookmark_tabs:")  
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

# Análisis de archivosst.subheader("Analizar textos con Voyant Tools :bar_chart:")  
archivo_para_analizar = st.selectbox("Selecciona un archivo para analizar", list_files(categoria_seleccionada))  
if st.button("Analizar el archivo seleccionado :mag:"):  
 if archivo_para_analizar:  
 ruta_archivo = os.path.join(directorio_base, categoria_seleccionada, archivo_para_analizar)  
 with open(ruta_archivo, 'r', encoding='utf-8') as file:  
 texto = file.read()  
 analizar
17
Mejora
