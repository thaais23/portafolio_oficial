import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portafolio de Thais Choque", layout="wide")

# Estilo personalizado: fondo crema-rosado, fuente Georgia
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        background-color: #fff2f2;
        color: #2e2e2e;
        font-family: 'Georgia', serif;
    }
    .stApp {
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #772f40;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Encabezado e imagen de presentación
st.markdown("<h1 style='text-align: center;'>Portafolio de Thais Choque</h1>", unsafe_allow_html=True)
st.image("mi_foto_circular.png", caption="Thais Choque", width=200)

st.markdown("### Estudiante de Comunicación Audiovisual · PUCP")
st.write("Este portafolio reúne aspectos de mi formación, intereses creativos y sensibilidad visual en desarrollo.")

# Navegación por pestañas
tabs = st.tabs([
    "Inicio", "Resume", "Exploraciones Creativas", "Research", "Achievements", "Hobbies", "Contacto"
])

with tabs[0]:
    st.subheader("Inicio")
    st.markdown("""
Bienvenida a mi portafolio personal.  
Aquí comparto mi proceso como estudiante de Comunicación Audiovisual, desde lo académico hasta lo que me inspira creativamente.

Cada sección refleja una parte distinta de mi formación y mis intereses.  
Gracias por estar aquí.
    """)

with tabs[1]:
    st.subheader("Perfil Académico")
    st.markdown("""
**Formación**  
- Comunicación Audiovisual en la PUCP (5to ciclo)  
- Enfoque en narrativa visual, lenguaje audiovisual, fotografía y edición  

**Habilidades**  
- Edición básica de video  
- Fotografía y composición  
- Trabajo en equipo y planificación  
- Interés por nuevas herramientas digitales  

**Idiomas**  
- Español (nativo)  
- Inglés (avanzado)  
    """)

with tabs[2]:
    st.subheader("Exploraciones Creativas")
    st.markdown("""
**Ejercicios fotográficos**  
He trabajado con luz natural, retratos y composición. Me interesa cómo una imagen puede transmitir atmósferas sutiles.

**Análisis visual**  
Observar planos, ritmo narrativo y silencios significativos ha sido clave para enriquecer mi comprensión del lenguaje cinematográfico.

**Trabajo colaborativo**  
He participado en procesos grupales de escritura y planificación visual. Valoro la creación colectiva desde distintas perspectivas.
    """)

with tabs[3]:
    st.subheader("Líneas de Interés")
    st.markdown("""
Actualmente me interesan los siguientes temas:

- Representación de lo cotidiano en el cine y las series  
- Personajes femeninos en narrativas visuales  
- Estética digital en redes sociales  
- Impacto emocional del lenguaje audiovisual  
- Colores, texturas y silencios como construcción de atmósferas  
    """)

with tabs[4]:
    st.subheader("Participaciones Formativas")
    st.markdown("""
- Curso de Narrativa Audiovisual (PUCP)  
- Cursos clave en guion, lenguaje visual y fotografía  
Estas experiencias han sido fundamentales en mi formación.
    """)

with tabs[5]:
    st.subheader("Gustos e Inspiraciones")
    st.markdown("""
- Escuchar música (K-pop, Taylor Swift, playlists suaves)  
- Ver series y k-dramas con una estética cuidada  
- Disfrutar del té como ritual creativo  
- Pasar tiempo con mi mascota Maya, que siempre acompaña mis momentos de inspiración  
    """)

with tabs[6]:
    st.subheader("Contacto")
    st.markdown("""
Si deseas comunicarte conmigo, puedes escribirme a:  
**thaisgchoque@gmail.com**

Gracias por visitar este espacio.
    """)
