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
# ... (tus importaciones y otras funciones como save_comment_to_csv, save_story_to_csv si las tienes) ...

# --- Funciones para Comentarios de NotiPatitas ---
NOTIPATITAS_COMMENTS_CSV = 'notipatitas_comments.csv'

def save_notipatitas_comment_to_csv(post_id, name, comment):
    """Guarda un comentario para una publicación específica de NotiPatitas en un CSV."""
    df = pd.DataFrame([[post_id, name, comment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                      columns=['post_id', 'Nombre', 'Comentario', 'Fecha'])
    if not os.path.isfile(NOTIPATITAS_COMMENTS_CSV):
        df.to_csv(NOTIPATITAS_COMMENTS_CSV, index=False)
    else:
        df.to_csv(NOTIPATITAS_COMMENTS_CSV, mode='a', header=False, index=False)

def load_notipatitas_comments_from_csv(post_id=None):
    """Carga los comentarios de NotiPatitas desde un CSV, opcionalmente filtrando por post_id."""
    if os.path.isfile(NOTIPATITAS_COMMENTS_CSV):
        df = pd.read_csv(NOTIPATITAS_COMMENTS_CSV)
        if post_id:
            return df[df['post_id'] == post_id]
        return df
    return pd.DataFrame(columns=['post_id', 'Nombre', 'Comentario', 'Fecha'])

# ... (el resto de tu script) ...
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

st.sidebar.markdown("<h1 style='color: #F9B872;'>Menú Principal 🐾</h1>", unsafe_allow_html=True) # Cambiado a Naranja vibrante (#FFA500)
st.sidebar.markdown("---")
st.sidebar.markdown("<h3 style='color: #5C4033;'>Explora el sitio:</h3>", unsafe_allow_html=True) # Cambiado a Café/Marrón (#5C4033)

# Estos botones de la barra lateral ahora también controlarán la sección_activa
if st.sidebar.button("Inicio 🏠", key="sb_inicio"):
    st.session_state.seccion_activa = "inicio"
if st.sidebar.button("Conoce a Lola 🐶", key="sb_conoce_lola_sb"):
    st.session_state.seccion_activa = "conoce_lola"
if st.sidebar.button("Notipaticas🐾", key="sb_nuiestros_amigos_sb"):
    st.session_state.seccion_activa = "nuestros_amigos"
if st.sidebar.button("Conoce nuestros peluditos 🐕🐈", key="sb_manada_peluditos_sb"):
    st.session_state.seccion_activa = "manada_peluditos"
if st.sidebar.button("Cuidado de Mascotas 🩺", key="sb_cuidado_mascotas_sb"):
    st.session_state.seccion_activa = "cuidado_mascotas"
if st.sidebar.button("Artículos Interesantes 📖", key="sb_articulos_sb"):
    st.session_state.seccion_activa = "articulos"
if st.sidebar.button("Comparte tu Historia 💌", key="sb_comparte_historia_sb"):
    st.session_state.seccion_activa = "comparte_historia"
if st.sidebar.button("Ver Historias Recibidas 🌟", key="sb_ver_historias_sb"):
    st.session_state.seccion_activa = "ver_historias"

# --- SECCIÓN: BARRA LATERAL (AUTOR DEL SITIO) ---
with st.sidebar:
    
    st.markdown("<h3 style='color: #F9B872;'>✍️ Autor del Sitio</h3>", unsafe_allow_html=True) # Cambiado a Naranja Suave (#F9B872)
    # Aquí puedes añadir tu foto. Asegúrate de que la ruta sea correcta.
    # Si tu foto se llama 'foto_autor.jpeg' y está en la misma carpeta:
    author_photo_path = "dic2024.jpg" # ¡CAMBIA ESTO POR LA RUTA REAL DE TU FOTO!

    try:
        author_photo = Image.open(author_photo_path)
        # Centrar la imagen en la barra lateral usando columnas
        col_img1, col_img2, col_img3 = st.columns([0.5, 2, 0.5]) # Ajusta las proporciones
        with col_img2:
            st.image(author_photo, width=120) # Ajusta el 'width' para el tamaño de la foto

    except FileNotFoundError:
        st.warning(f"No se encontró la imagen del autor en: {author_photo_path}")
    except Exception as e:
        st.error(f"Error al cargar la imagen del autor: {e}")

    # Expander para la descripción biográfica
    with st.expander("Danilo Alava"):
        st.write("""
        ¡Hola! Soy Danii, el creador detrás de "Amigos de LoLa".
        Mi pasión por los animales, especialmente por los perros y gatos,
        me impulsó a crear este espacio para compartir información,
        historias y recursos que promuevan el cuidado y bienestar de nuestras mascotas.
        Espero que disfrutes explorando y aprendiendo con nosotros.
        ¡Gracias por visitar!
        """)
        # Puedes añadir más información aquí si lo deseas:
        # st.write("Puedes contactarme en: tu_email@ejemplo.com")
# --- CONTENIDO PRINCIPAL ---
st.markdown("<h1 style='text-align: center; color: #FFA500;'>🐾 Amigos de Lola 🐾</h1>", unsafe_allow_html=True) # Naranja estánda  
# --- Añade estas dos líneas para tu logo ---
# --- INICIO DEL CÓDIGO MODIFICADO PARA EL LOGO ---
logo_path = "Lolit.jpg" # Asegúrate de que esta ruta sea correcta para tu logo

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
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns(5) # Ahora 5 columnas

with col_nav1:
    if st.button("🐶 Conoce a Lola", use_container_width=True):
        st.session_state.seccion_activa = "conoce_lola"
with col_nav2:
    if st.button("🐾 La Manada ", use_container_width=True):
        st.session_state.seccion_activa = "manada_peluditos"
with col_nav3:  
    if st.button("📖 Artículos Interesantes", use_container_width=True):
        st.session_state.seccion_activa = "articulos"
with col_nav4:
    if st.button("💌 Historias ", use_container_width=True):
        st.session_state.seccion_activa = "comparte_historia" # Irá a la sección de compartir historia
with col_nav5: # NUEVO BOTÓN
    if st.button("🌟 Eventos Destacados", use_container_width=True):
        st.session_state.seccion_activa = "eventos_destacados" # Nueva clave de sesión

st.markdown("---")

# ... (tus importaciones y logo_path, etc. aquí) ...

# --- DATOS DE NOTIPATITAS ---
# Lista para almacenar las noticias/eventos de NotiPatitas
# Cada diccionario representa una publicación con su imagen, título y descripción.
# Asegúrate de que las rutas de las imágenes sean correctas (por ejemplo, 'img/mural.png')
noti_patitas_data = [
    {
        "id": "manada_semana_1", # ID único para enlazar comentarios
        "titulo": "🐾 La Manada de la Semana: ¡Nuestros Pequeños Héroes! 🐾",
        "imagen": "ManadaBlue.jpg", # CAMBIA ESTO: Ruta de tu foto de la manada
        "descripcion": """
        Esta semana, queremos presentarles a la increíble manada que ha llenado de alegría
        nuestros corazones. Son un ejemplo de amistad y resiliencia. Conoce a Blue,
        Hanna, Roma , Brisa y Sacha. Estos peluditos se integran en las tardes para disfrutar
        de un paseo y recreacion. ¡Su energía es contagiosa!
        """
    },
    {
        "id": "aviso_rifa_1", # ID único
        "titulo": "🎉 ¡Gran Rifa Solidaria por Nuestros Peluditos! 🎉",
        "imagen": "notipatitas.png", # CAMBIA ESTO: Ruta de tu foto de la rifa
        "descripcion": """
        ¡Participa en nuestra rifa solidaria y ayuda a los peluditos en necesidad!
        Tenemos premios increíbles. Cada boleta es un ladrillo más en la construcción
        de un futuro mejor para ellos. ¡No te quedes sin la tuya! Más información
        sobre cómo participar y los premios en juego.
        """
    },
    {
        "id": "mascota_perdida_1", # ID único
        "titulo": "🚨 ¡Ayúdanos a Encontrar a Luna! Perra Perdida en [Tu Ciudad/Barrio] 🚨",
        "imagen": "Luna.jpg", # CAMBIA ESTO: Ruta de la foto de la mascota perdida
        "descripcion": """
        Luna, una [raza/descripción], se perdió el [fecha] cerca de [lugar].
        Es muy amigable y [características distintivas]. Si la has visto o tienes
        alguna información, por favor contáctanos al [número de contacto].
        ¡Su familia la extraña mucho!
        """
    },
    {
        "id": "denuncia_maltrato_1", # ID único
        "titulo": "⚖️ ¡No al Maltrato Animal! Unidos por la Justicia ⚖️",
        "imagen": "mural de encabezado.png", # CAMBIA ESTO: Imagen que ilustre la campaña (NO fotos explícitas de maltrato)
        "descripcion": """
        Recientemente, hemos recibido un reporte preocupante sobre un caso de maltrato
        animal en [ubicación general, si es relevante y seguro]. Queremos recordarles
        la importancia de denunciar y actuar. Si eres testigo de maltrato,
        contacta a las autoridades locales o a organizaciones de protección animal.
        ¡Su voz es la nuestra!
        """
    }
]

# ... (el resto de tu script) ...

# --- Renderizado Condicional de Secciones ---
# Solo se muestra la sección activa
if st.session_state.seccion_activa == "inicio":
    # Centramos y coloreamos el texto de bienvenida
    st.markdown("<p style='text-align: center; color: #FAE7A5; font-size: 20px;'>Selecciona una opción de arriba o desde el menú lateral para empezar a explorar.</p>", unsafe_allow_html=True)

    # Centramos la imagen de inicio y ajustamos el tamaño
    imagen_inicio_path = "mural de encabezado.png" # Asegúrate de que esta ruta sea correcta
    try:
        col_img_inicio1, col_img_inicio2, col_img_inicio3 = st.columns([1, 2, 1]) # Ajusta proporciones para centrar
        with col_img_inicio2:
            st.image(imagen_inicio_path, caption="🐾🔊¡Mural de noti paticas!🎬🐾", width=400) # Ajusta el 'width'
    except FileNotFoundError:
        st.warning(f"La imagen '{imagen_inicio_path}' para la sección de inicio no se encontró.")
        # Opción alternativa si la imagen no se encuentra
        col_img_inicio1, col_img_inicio2, col_img_inicio3 = st.columns([1 , 2, 1])
        with col_img_inicio2:
            st.image("https://placehold.co/400x300/99775C/EAE7DD?text=Mural+No+Encontrado",
                     caption="Imagen no encontrada", width=50)
    except Exception as e:
        st.error(f"Error al cargar la imagen de inicio: {e}")

if st.session_state.seccion_activa == "conoce_lola":
    # --- Sección de Conoce a Lola (Expander Centrado y Estilizado) ---
    # --- Sección de Conoce a Lola ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>Conoce a Lola 🐶</h2>", unsafe_allow_html=True) # Marrón Café Oscuro

    lola_imagen_path = "BEAGLE LOLI.jpg"

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.expander("  🐾   LA JEFA   🐾   "):
            st.markdown("""
                <div style="text-align: center; color: #8A2BE2; font-family: 'Comic Sans MS', cursive; font-size: 2em; font-weight: bold;">
                    LOLA
                </div>
                """, unsafe_allow_html=True)
            st.markdown("---")
            try:
                st.image(lola_imagen_path, caption="  La jefa   ", use_container_width=True)
            except FileNotFoundError:
                st.error(f"Error: La imagen de Lola '{lola_imagen_path}' no se encontró. Asegúrate de que el archivo esté en la misma carpeta que el script o que la ruta sea correcta.")
                st.image("https://placehold.co/600x400/FFD700/000000?text=Imagen no encontrada",
                         caption="",
                         use_container_width=True)
            st.write("Es nuestra Beagle, y la inspiración de este sitio. Con su actitud siempre empoderada se ha ganado el apodo de alias la jefa. Es una Beagle amigable, curiosa y muy sociable, ideales para su liderasgo. Requiere bastante ejercicio y estimulación mental para evitar que se enoje. jeje¡¡. Su ladrido característico y aullido son notables.")

if st.session_state.seccion_activa == "nuestros_amigos":
    # --- Sección de Imagen (Mural de Encabezado) ---
    # --- NUEVA SECCIÓN: NOTIPATITAS (Publicaciones de Noticias/Eventos) ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>📰 NotiPatitas: ¡Lo Último de Nuestra Manada! 🐾</h2>", unsafe_allow_html=True)

# Iterar sobre los datos de NotiPatitas para mostrar cada publicación
for post in noti_patitas_data:
    with st.expander(f"✨ {post['titulo']}"): # Título de la publicación en el expander
        # Centrar la imagen dentro del expander
        col_img_np1, col_img_np2, col_img_np3 = st.columns([1, 4, 1]) # Ajusta si necesitas más espacio
        with col_img_np2:
            try:
                # Cargar imagen usando PIL.Image.open si necesitas más control o si es JPG
                # Si es PNG y siempre el mismo nombre, st.image(post['imagen']) también sirve
                st.image(post['imagen'], caption=post['titulo'], use_container_width=True)
            except FileNotFoundError:
                st.error(f"Error: La imagen '{post['imagen']}' para '{post['titulo']}' no se encontró.")
                st.image("https://placehold.co/600x400/99775C/EAE7DD?text=Imagen+No+Encontrada",
                                 caption="Imagen no encontrada",
                                 use_container_width=True)
            except Exception as e:
                st.error(f"Error al cargar la imagen para '{post['titulo']}': {e}")

        st.markdown(post['descripcion'])
        st.write("---") # Separador visual

        st.markdown(f"#### Comentarios sobre '{post['titulo']}'")
        comments_df = load_notipatitas_comments_from_csv(post_id=post['id'])
        if not comments_df.empty:
            # Mostrar los comentarios, puedes ajustar el formato
            for index, row in comments_df.iterrows():
                st.markdown(f"**{row['Nombre']}** ({row['Fecha']}): {row['Comentario']}")
        else:
            st.info("Sé el primero en comentar esta publicación.")

        # Formulario para agregar un comentario
        with st.form(key=f"comment_form_{post['id']}"): # Key único para cada formulario de comentario
            comment_name = st.text_input("Tu Nombre", key=f"comment_name_{post['id']}")
            comment_text = st.text_area("Tu Comentario", key=f"comment_text_{post['id']}")
            comment_submit = st.form_submit_button("Enviar Comentario")

            if comment_submit:
                if comment_name and comment_text:
                    save_notipatitas_comment_to_csv(post['id'], comment_name, comment_text)
                    st.success("¡Gracias por tu comentario!")
                    st.rerun() # Para recargar los comentarios
                else:
                    st.warning("Por favor, ingresa tu nombre y un comentario.")
        st.write("---") # Separador al final de cada expander

if st.session_state.seccion_activa == "manada_peluditos":
    # --- NUEVA SECCIÓN: Cualidades de la Manada de Perros (Interactiva) ---
    st.markdown("<h2 style='text-align: center; color: #F9B872;'>🐾 Nuestra Manada🐾 </h2>", unsafe_allow_html=True) # Marrón Café Oscuro

    st.write("Haz clic en el nombre de cada perrito para ver su foto y sus cualidades.")

    manada_perros = [
        {
            "nombre": "ROMA",
            "imagen": "Romijul.jpg",
            "cualidades": "ROMA es una Sabueso (Bloodhound) muy curiosa por su olfato insuperable. Su temperamento con la gente es  sereno y analitico , le encanta jugar con sus amigos y siempre está lista para un reto. Es muy leal y protectora con su manada."
        },
        {
            "nombre": "TIGRE y Filipa",
            "imagen": "tigre_filip.jpg",
            "cualidades": "Tigre y Filipa representan una gran manada que pronto conoceran ¡¡ Tigre es el más tranquilo y comelon ¡¡ de la manada y Filipa prefiere dominar y ser la  consentidad de sus humanos. Su curiosidad se refleja en su mirada."
        },
        {
            "nombre": "LOLA",
            "imagen": "lolitexplorer.jpg",
            "cualidades": "LOLA es la Beagle con el  olfato excepcionalmente más desarrollado. Siempre busca nuevas exploraciones con su manada y es increíblemente terca ¡¡ jeje. Su energía es contagiosa."
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
        st.subheader("Recomendaciones básicas")
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
        with st.expander("Cuidados básicos"):
            st.write("""
            - **Higiene:** Baños regulares, cepillado de pelo, limpieza de orejas y corte de uñas.
            - **Identificación:** Microchip y placa con datos de contacto.
            - **Hidratación:** Agua fresca y limpia siempre disponible.
            """)

    with tab_gatos:
        st.subheader("Recomendaciones")
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
        with st.expander("Cuidados Básicos "):
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

        # --- PIE DE PÁGINA (DERECHOS DE AUTOR) ---
st.markdown("---") # Una línea divisoria antes del pie de página
st.markdown(
    "<p style='text-align: center; color: #8C8C8C; font-size: small;'>© 2025 Amigos de LoLa. Todos los derechos reservados.</p>",
    unsafe_allow_html=True
)
# Puedes ajustar el color y el tamaño de la fuente si lo deseas