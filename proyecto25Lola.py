import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime
from PIL import Image # ¡Añade esta línea!

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Amigos de LoLa",
    page_icon="🐾🐶",
    layout="wide"
)

# --- RUTAS DE ARCHIVOS CSV ---
CSV_HISTORIAS = "historias_peluditos.csv"
CSV_COMENTARIOS_PERROS = "comentarios_articulos_perros.csv"
CSV_COMENTARIOS_GATOS = "comentarios_articulos_gatos.csv"


# --- FUNCIONES DE ALMACENAMIENTO ---
def save_story_to_csv(nombre, email, mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_story_df = pd.DataFrame([{"Fecha": timestamp, "Nombre": nombre, "Email": email, "Mensaje": mensaje}])

    if os.path.exists(CSV_HISTORIAS):
        existing_df = pd.read_csv(CSV_HISTORIAS)
        updated_df = pd.concat([existing_df, new_story_df], ignore_index=True)
    else:
        updated_df = new_story_df

    updated_df.to_csv(CSV_HISTORIAS, index=False)
    st.success("¡Tu historia ha sido guardada con éxito!")

def save_comment_to_csv(csv_file_path, nombre, email, comentario):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_comment_df = pd.DataFrame([{"Fecha": timestamp, "Nombre": nombre, "Email": email, "Comentario": comentario}])

    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
        updated_df = pd.concat([existing_df, new_comment_df], ignore_index=True)
    else:
        updated_df = new_comment_df

    updated_df.to_csv(csv_file_path, index=False)
    st.success("¡Tu comentario ha sido guardado!")


# --- BARRA LATERAL PARA NAVEGACIÓN ---
st.sidebar.title("Menú Principal 🐾")
st.sidebar.markdown("---")
st.sidebar.subheader("Explora el sitio:")

# Estos botones de la barra lateral ahora también controlarán la sección_activa
if st.sidebar.button("Inicio 🏠", key="sb_inicio"):
    st.session_state.seccion_activa = "inicio"
if st.sidebar.button("Conoce a Lola 🐶", key="sb_conoce_lola_sb"):
    st.session_state.seccion_activa = "conoce_lola"
if st.sidebar.button("Nuestros Amigos Peludos 🐾", key="sb_nuestros_amigos_sb"):
    st.session_state.seccion_activa = "nuestros_amigos"
if st.sidebar.button("Manada de Peluditos 🐕🐈", key="sb_manada_peluditos_sb"):
    st.session_state.seccion_activa = "manada_peluditos"
if st.sidebar.button("Cuidado de Mascotas 🩺", key="sb_cuidado_mascotas_sb"):
    st.session_state.seccion_activa = "cuidado_mascotas"
if st.sidebar.button("Artículos Interesantes 📖", key="sb_articulos_sb"):
    st.session_state.seccion_activa = "articulos"
if st.sidebar.button("Comparte tu Historia 💌", key="sb_comparte_historia_sb"):
    st.session_state.seccion_activa = "comparte_historia"
if st.sidebar.button("Ver Historias Recibidas 🌟", key="sb_ver_historias_sb"):
    st.session_state.seccion_activa = "ver_historias"


# --- CONTENIDO PRINCIPAL ---
st.markdown("<h1 style='text-align: center; color: #FFA500;'>🐾 Amigos de Lola 🐾</h1>", unsafe_allow_html=True) # Naranja estánda  
# --- Añade estas dos líneas para tu logo ---
# --- INICIO DEL CÓDIGO MODIFICADO PARA EL LOGO ---
logo_path = "notipatitas.png" # Asegúrate de que esta ruta sea correcta para tu logo

# Creamos 3 columnas: una vacía a la izquierda, una para el logo, una vacía a la derecha
# Ajusta los números [1, 1, 1] si quieres más espacio a los lados, por ejemplo [2, 1, 2]
col1, col2, col3 = st.columns([2, 1, 2])

with col2: # Colocamos el logo en la columna central
    st.image(logo_path, width=125) # Reducimos el 'width' al 50% de 250, que es 125.
# --- FIN DEL CÓDIGO MODIFICADO PARA EL LOGO ---
st.markdown("<h2 style='text-align: center; color: #F9B872;'>Un lugar para crear conciencia en el cuidado de nuestros peluditos</h2>", unsafe_allow_html=True) # Naranja muy pálido


st.markdown("<h3 style='text-align: center; color: #FAF5E9;'>Descubre consejos, historias y mucho más sobre perros y gatos.</h3>", unsafe_allow_html=True) # Marfil




# --- MENSAJE DE BIENVENIDA ESTILIZADO Y BOTONES DE NAVEGACIÓN PRINCIPAL ---
st.markdown("---")
# Nuevo mensaje de bienvenida
# --- MENSAJE DE BIENVENIDA ESTILIZADO Y BOTONES DE NAVEGACIÓN PRINCIPAL ---
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #F9B872; font-family: sans-serif;'>🐶 Bienvenidos 🐱</h3>", unsafe_allow_html=True) # Naranja medio

st.markdown("<h4 style='text-align: center; color: #FAF5E9;'>Explora las categorías principales:</h4>", unsafe_allow_html=True) # Marfil

# Inicializar la sección_activa si no existe
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "inicio" # Puedes elegir qué sección se muestra al inicio



# Botones de navegación al inicio
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)

with col_nav1:
    if st.button("🐶 Conoce a Lola", use_container_width=True):
        st.session_state.seccion_activa = "conoce_lola"
with col_nav2:
    if st.button("🐾 Manada de Peluditos", use_container_width=True):
        st.session_state.seccion_activa = "manada_peluditos"
with col_nav3:
    if st.button("📖 Artículos Interesantes", use_container_width=True):
        st.session_state.seccion_activa = "articulos"
with col_nav4:
    if st.button("💌 Historias y Contacto", use_container_width=True):
        st.session_state.seccion_activa = "comparte_historia" # Irá a la sección de compartir historia

st.markdown("---")

# --- Renderizado Condicional de Secciones ---
# Solo se muestra la sección activa
if st.session_state.seccion_activa == "inicio":
    st.write("Selecciona una opción de arriba o desde el menú lateral para empezar a explorar.")
    # Opcional: mostrar un contenido de inicio específico aquí
    st.image("mural de encabezado.png", caption="🐾🔊¡Mural de noti paticas!🎬🐾", use_container_width=True) # Puedes poner una imagen representativa

if st.session_state.seccion_activa == "conoce_lola":
    # --- Sección de Conoce a Lola (Expander Centrado y Estilizado) ---
    # --- Sección de Conoce a Lola ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>Conoce a Lola 🐶</h2>", unsafe_allow_html=True) # Marrón Café Oscuro

    lola_imagen_path = "BEAGLE LOLI.jpg"

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.expander(" 🐶     LA JEFA LOLA     🐶"):
            st.markdown("""
                <div style="text-align: center; color: #8A2BE2; font-family: 'Comic Sans MS', cursive; font-size: 2em; font-weight: bold;">
                    LOLA
                </div>
                """, unsafe_allow_html=True)
            st.markdown("---")
            try:
                st.image(lola_imagen_path, caption="🐶   La jefa   🐶", use_container_width=True)
            except FileNotFoundError:
                st.error(f"Error: La imagen de Lola '{lola_imagen_path}' no se encontró. Asegúrate de que el archivo esté en la misma carpeta que el script o que la ruta sea correcta.")
                st.image("https://placehold.co/600x400/FFD700/000000?text=Imagen no encontrada",
                         caption="",
                         use_container_width=True)
            st.write("Es nuestra Beagle, y la inspiración de este sitio. Con su actitud siempre empoderada, alias la jefa. Los beagle son amigables, curiosos y muy sociables, ideales para familias. Requieren bastante ejercicio y estimulación mental para evitar que se aburran y sean destructivos. Su ladrido característico y aullido son notables.")

if st.session_state.seccion_activa == "nuestros_amigos":
    # --- Sección de Imagen (Mural de Encabezado) ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>Nuestros Amigos Peludos</h2>", unsafe_allow_html=True) # Marrón Café Oscuro


    with st.expander("🌼 ¡Ver Mural de Increíbles Historias! 🐾"):
        st.markdown("🌼Increibles historias🐾")
        imagen_local_path = "mural de encabezado.png"
        try:
            st.image(imagen_local_path, caption="🐾🔊¡Mural de noti paticas!🎬🐾", use_container_width=True)
        except FileNotFoundError:
            st.error(f"Error: La imagen '{imagen_local_path}' no se encontró. Asegúrate de que el archivo esté en la misma carpeta que el script o que la ruta sea correcta.")
            st.image("https://placehold.co/600x400/FFD700/000000?text=Imagen no encontrada",
                         caption="",
                         use_container_width=True)

if st.session_state.seccion_activa == "manada_peluditos":
    # --- NUEVA SECCIÓN: Cualidades de la Manada de Perros (Interactiva) ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>🐶 Nuestra Manada de Peluditos 🐶</h2>", unsafe_allow_html=True) # Marrón Café Oscuro

    st.write("Haz clic en el nombre de cada perrito para ver su foto y sus cualidades.")

    manada_perros = [
        {
            "nombre": "ROMA",
            "imagen": "sabueso_roma.jpg",
            "cualidades": "ROMA es una perrita muy juguetona y cariñosa. Le encanta correr en el parque y siempre está lista para un abrazo. Es muy leal y protectora con su familia."
        },
        {
            "nombre": "TIGRE",
            "imagen": "tigre_luky.jpeg",
            "cualidades": "TIGRE es el más tranquilo de la manada. Disfruta de largas siestas al sol y es muy paciente con los cachorros. Su sabiduría se refleja en su mirada."
        },
        {
            "nombre": "LOLA",
            "imagen": "BEAGLE LOLI.jpg",
            "cualidades": "LOLA es una aventurera nata. Siempre busca nuevas exploraciones en el jardín y es increíblemente curiosa. Su energía es contagiosa."
        }
    ]

    num_columnas = 3
    i = 0
    while i < len(manada_perros):
        cols = st.columns(num_columnas)
        for j in range(num_columnas):
            if i + j < len(manada_perros):
                perro = manada_perros[i + j]
                with cols[j]:
                    with st.expander(f"**{perro['nombre']}**"):
                        try:
                            st.image(perro['imagen'], caption=f"¡{perro['nombre']}!", use_container_width=True)
                        except FileNotFoundError:
                            st.warning(f"La imagen para {perro['nombre']} ('{perro['imagen']}') no se encontró. Asegúrate de que el archivo esté en la misma carpeta.")
                            st.image("https://placehold.co/400x300/FF0000/FFFFFF?text=Imagen no encontrada",
                                     caption=f"Imagen de {perro['nombre']} no encontrada",
                                     use_container_width=True)
                        st.write(perro['cualidades'])
        i += num_columnas

if st.session_state.seccion_activa == "cuidado_mascotas":
    # --- SECCIÓN: Información Esencial para el Cuidado de tu Mascota ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>Información Esencial para el Cuidado de tu Mascota</h2>", unsafe_allow_html=True) # Marrón Café Oscuro

    tab_perros, tab_gatos = st.tabs(["🐶 Perros", "🐱 Gatos"])

    with tab_perros:
        st.subheader("Consejos para Perros")
        with st.expander("Salud Canina"):
            st.write("""
            - **Vacunación:** Mantén al día el calendario de vacunas (parvovirus, moquillo, rabia, etc.).
            - **Desparasitación:** Regularmente contra parásitos internos y externos.
            - **Visitas al veterinario:** Chequeos anuales y ante cualquier síntoma inusual.
            - **Alimentación:** Dieta balanceada y adecuada a su edad, raza y nivel de actividad.
            """)
        with st.expander("Bienestar Canino"):
            st.write("""
            - **Ejercicio:** Paseos diarios y juegos para liberar energía y mantenerlos en forma.
            - **Socialización:** Exposición temprana a personas, otros perros y entornos.
            - **Entrenamiento:** Refuerzo positivo para obediencia básica y trucos.
            - **Espacio:** Un lugar cómodo y seguro para descansar.
            """)
        with st.expander("Cuidados Básicos para Perros"):
            st.write("""
            - **Higiene:** Baños regulares, cepillado de pelo, limpieza de orejas y corte de uñas.
            - **Identificación:** Microchip y placa con datos de contacto.
            - **Hidratación:** Agua fresca y limpia siempre disponible.
            """)

    with tab_gatos:
        st.subheader("Consejos para Gatos")
        with st.expander("Salud Felina"):
            st.write("""
            - **Vacunación:** Protege contra enfermedades como la panleucopenia, rinotraqueítis, calicivirus y rabia.
            - **Desparasitación:** Esencial incluso para gatos de interior.
            - **Visitas al veterinario:** Chequeos periódicos y atención a cambios en el comportamiento.
            - **Alimentación:** Piensos de calidad, adaptados a su edad y si es esterilizado.
            """)
        with st.expander("Bienestar Felino"):
            st.write("""
            - **Enriquecimiento ambiental:** Rascadores, juguetes, espacios elevados para trepar.
            - **Juego:** Interacciones diarias para estimular su mente y cuerpo.
            - **Privacidad:** Lugares tranquilos para esconderse y descansar.
            - **Limpieza:** Arenero siempre limpio para evitar problemas de comportamiento.
            """)
        with st.expander("Cuidados Básicos para Gatos"):
            st.write("""
            - **Higiene:** Cepillado regular, especialmente en razas de pelo largo.
            - **Hidratación:** Agua fresca y limpia, considera fuentes de agua para estimular el consumo.
            - **Identificación:** Microchip, incluso para gatos de interior.
            """)

if st.session_state.seccion_activa == "articulos":
    # --- SECCIÓN: ARTÍCULOS INTERESANTES ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>📖 Artículos Interesantes sobre Mascotas 🐾</h2>", unsafe_allow_html=True) # Marrón Café Oscuro


    st.write("Explora nuestros artículos y aprende más sobre el cuidado y bienestar de tus compañeros peludos.")

    tab_articulos_perros, tab_articulos_gatos = st.tabs(["🐶 Artículos para Perros", "🐱 Artículos para Gatos"])

    with tab_articulos_perros:
        st.subheader("Artículos Dedicados a Nuestros Amigos Caninos")

        # Artículo 1 para perros
        with st.expander("🐶 Guía Completa de Alimentación para Perros"):
            st.write("""
            Una dieta balanceada es crucial para la salud de tu perro. Aprende sobre los tipos de alimentos, las porciones adecuadas según la edad y el tamaño, y qué ingredientes debes evitar.
            """)
            with open("guia_alimentacion_perros.pdf", "rb") as file:
                st.download_button(
                    label="Descargar Guía de Alimentación (PDF)",
                    data=file,
                    file_name="guia_alimentacion_perros.pdf",
                    mime="application/pdf"
                )
            st.markdown("---")
            st.subheader("Comentarios sobre este artículo:")
            with st.form("comentarios_guia_perros"):
                nombre_c = st.text_input("Tu Nombre", key="nombre_c_perros_1")
                email_c = st.text_input("Tu Correo Electrónico", key="email_c_perros_1")
                comentario_c = st.text_area("Tu Comentario", key="comentario_c_perros_1")
                submitted_c = st.form_submit_button("Enviar Comentario")
                if submitted_c:
                    if nombre_c and email_c and comentario_c:
                        save_comment_to_csv(CSV_COMENTARIOS_PERROS, nombre_c, email_c, comentario_c)
                    else:
                        st.error("Por favor, completa todos los campos para enviar tu comentario.")
            st.markdown("#### Comentarios Anteriores:")
            if os.path.exists(CSV_COMENTARIOS_PERROS):
                df_comentarios = pd.read_csv(CSV_COMENTARIOS_PERROS)
                if not df_comentarios.empty:
                    for index, row in df_comentarios.iterrows():
                        st.markdown(f"**{row['Nombre']}** ({row['Fecha']}): {row['Comentario']}")
                        st.markdown("---")
                else:
                    st.info("Aún no hay comentarios para este artículo.")
            else:
                st.info("Sé el primero en comentar este artículo.")


        # Artículo 2 para perros (ejemplo)
        with st.expander("🐶 Entrenamiento Positivo para Cachorros"):
            st.write("""
            Descubre los principios del entrenamiento con refuerzo positivo para cachorros. Establece una base sólida de obediencia y crea un vínculo fuerte con tu nuevo compañero.
            """)
            with open("entrenamiento_cachorros.pdf", "rb") as file:
                st.download_button(
                    label="Descargar Guía de Entrenamiento (PDF)",
                    data=file,
                    file_name="entrenamiento_cachorros.pdf",
                    mime="application/pdf"
                )
            st.markdown("---")
            st.subheader("Comentarios sobre este artículo:")
            with st.form("comentarios_entrenamiento_perros"):
                nombre_c = st.text_input("Tu Nombre", key="nombre_c_perros_2")
                email_c = st.text_input("Tu Correo Electrónico", key="email_c_perros_2")
                comentario_c = st.text_area("Tu Comentario", key="comentario_c_perros_2")
                submitted_c = st.form_submit_button("Enviar Comentario")
                if submitted_c:
                    if nombre_c and email_c and comentario_c:
                        save_comment_to_csv(CSV_COMENTARIOS_PERROS, nombre_c, email_c, comentario_c)
                    else:
                        st.error("Por favor, completa todos los campos para enviar tu comentario.")
            st.markdown("#### Comentarios Anteriores:")
            if os.path.exists(CSV_COMENTARIOS_PERROS):
                df_comentarios = pd.read_csv(CSV_COMENTARIOS_PERROS)
                if not df_comentarios.empty:
                    for index, row in df_comentarios.iterrows():
                        st.markdown(f"**{row['Nombre']}** ({row['Fecha']}): {row['Comentario']}")
                        st.markdown("---")
                else:
                    st.info("Aún no hay comentarios para este artículo.")
            else:
                st.info("Sé el primero en comentar este artículo.")


    with tab_articulos_gatos:
        st.subheader("Artículos para Nuestros Amigos Felinos")

        # Artículo 1 para gatos
        with st.expander("🐱 Comprendiendo el Comportamiento Felino"):
            st.write("""
            Los gatos son criaturas fascinantes. Entiende sus señales, su necesidad de rascado y su comportamiento social para mejorar la convivencia en casa.
            """)
            with open("comportamiento_felino.pdf", "rb") as file:
                st.download_button(
                    label="Descargar Artículo (PDF)",
                    data=file,
                    file_name="comportamiento_felino.pdf",
                    mime="application/pdf"
                )
            st.markdown("---")
            st.subheader("Comentarios sobre este artículo:")
            with st.form("comentarios_comportamiento_gatos"):
                nombre_c = st.text_input("Tu Nombre", key="nombre_c_gatos_1")
                email_c = st.text_input("Tu Correo Electrónico", key="email_c_gatos_1")
                comentario_c = st.text_area("Tu Comentario", key="comentario_c_gatos_1")
                submitted_c = st.form_submit_button("Enviar Comentario")
                if submitted_c:
                    if nombre_c and email_c and comentario_c:
                        save_comment_to_csv(CSV_COMENTARIOS_GATOS, nombre_c, email_c, comentario_c)
                    else:
                        st.error("Por favor, completa todos los campos para enviar tu comentario.")
            st.markdown("#### Comentarios Anteriores:")
            if os.path.exists(CSV_COMENTARIOS_GATOS):
                df_comentarios = pd.read_csv(CSV_COMENTARIOS_GATOS)
                if not df_comentarios.empty:
                    for index, row in df_comentarios.iterrows():
                        st.markdown(f"**{row['Nombre']}** ({row['Fecha']}): {row['Comentario']}")
                        st.markdown("---")
                else:
                    st.info("Aún no hay comentarios para este artículo.")
            else:
                st.info("Sé el primero en comentar este artículo.")

if st.session_state.seccion_activa == "comparte_historia":
    # --- SECCIÓN: Formulario para Compartir Historia ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>¡Queremos escuchar tu historia!</h2>", unsafe_allow_html=True) # Marrón Café Oscuro



    st.write("¿Tienes alguna historia de tu peludito que quieras compartir o alguna pregunta?")

    with st.form("contact_form"):
        nombre = st.text_input("Tu Nombre")
        email = st.text_input("Tu Correo Electrónico")
        mensaje = st.text_area("Tu Mensaje o Historia")

        submitted = st.form_submit_button("Enviar Historia")
        if submitted:
            if nombre and email and mensaje:
                save_story_to_csv(nombre, email, mensaje)
            else:
                st.error("Por favor, completa todos los campos para enviar tu mensaje.")

if st.session_state.seccion_activa == "ver_historias":
    # --- SECCIÓN: Ver Historias Recibidas desde CSV ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>Historias de Nuestros Peluditos</h2>", unsafe_allow_html=True) # Marrón Café Oscuro
    st.write("Aquí puedes ver las historias que nuestros visitantes han compartido.")

    if os.path.exists(CSV_HISTORIAS):
        try:
            df_historias = pd.read_csv(CSV_HISTORIAS)
            if not df_historias.empty:
                for index, row in df_historias.iloc[::-1].iterrows():
                    st.markdown(f"**Nombre:** {row['Nombre']}")
                    st.markdown(f"**Correo:** {row['Email']}")
                    st.markdown(f"**Fecha de Envío:** {row['Fecha']}")
                    st.write(f"**Historia:** {row['Mensaje']}")
                    st.markdown("---")
            else:
                st.info("Aún no hay historias compartidas. ¡Sé el primero!")
        except Exception as e:
            st.error(f"Error al leer las historias: {e}")
    else:
        st.info("Aún no se ha creado el archivo de historias. ¡Envía una historia para empezar!")