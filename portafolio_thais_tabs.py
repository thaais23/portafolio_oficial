
import streamlit as st

# Configuración
st.set_page_config(page_title="Portafolio de Thais Choque", layout="wide")

# Estilo limpio, suave y moderno
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9fb;
    }
    .stApp {
        background-color: #ffffff;
    }
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
        color: #1e1e2f;
    }
    h1, h2, h3 {
        color: #3b3b58;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1 style='text-align: center;'>Portafolio de Thais Choque</h1>", unsafe_allow_html=True)
st.write("Estudiante de Comunicación Audiovisual en la PUCP")
st.write("Este portafolio reúne aspectos de mi formación, intereses creativos y sensibilidad estética en desarrollo.")

# Tabs
tabs = st.tabs([
    "INICIO", "RESUME", "EXPLORACIONES CREATIVAS", "RESEARCH", "ACHIEVEMENTS", "HOBBIES", "CONTACTO"
])

with tabs[0]:
    st.image("https://i.imgur.com/sDaRtnt.jpg", caption="Referencias visuales · atmósfera cálida y estética limpia", use_column_width=True)
    st.subheader("Bienvenida")
    st.markdown("""
Este espacio contiene:

- RESUME · Perfil académico
- EXPLORACIONES CREATIVAS · Prácticas y aprendizajes
- RESEARCH · Intereses en desarrollo
- ACHIEVEMENTS · Participaciones formativas
- HOBBIES · Gustos personales con valor creativo
- CONTACTO · Información de contacto

Gracias por visitar este espacio.
    """)

with tabs[1]:
    st.subheader("RESUME · Perfil académico")
    st.markdown("""
**Formación**  
- Comunicación Audiovisual en la PUCP (5to ciclo)  
- Cursos enfocados en narrativa visual, lenguaje audiovisual, fotografía y edición  

**Habilidades**  
- Edición básica de video  
- Fotografía y composición  
- Trabajo colaborativo y planificación  
- Interés por nuevas herramientas digitales  

**Idiomas**  
- Español (nativo)  
- Inglés (avanzado)  

Me encuentro en formación, con interés en aplicar estos aprendizajes en proyectos creativos y colaborativos.
    """)

with tabs[2]:
    st.image("https://i.imgur.com/XCE9PBR.jpg", caption="Exploraciones visuales", use_column_width=True)
    st.subheader("EXPLORACIONES CREATIVAS")
    st.markdown("""
**Ejercicios fotográficos**  
Exploración con luz natural, retratos y composición. Me interesa cómo la imagen puede sugerir atmósferas sutiles.

**Análisis de escenas visuales**  
Observación de planos, ritmo narrativo y silencios. Herramientas valiosas para comprender la estructura cinematográfica.

**Creación audiovisual en grupo**  
He participado en la escritura y planificación de escenas. Valoro el trabajo colaborativo y la construcción narrativa colectiva.
    """)

with tabs[3]:
    st.subheader("RESEARCH · Intereses en desarrollo")
    st.markdown("""
Actualmente me interesa explorar temas como:

- Representación de lo cotidiano en el cine y las series  
- Personajes femeninos en narrativas visuales  
- Estética visual en redes sociales  
- Impacto emocional de las historias audiovisuales  
- Colores, texturas y silencios como generadores de atmósfera  

Estas áreas reflejan mi búsqueda personal y posibles caminos profesionales.
    """)

with tabs[4]:
    st.subheader("ACHIEVEMENTS · Participaciones formativas")
    st.markdown("""
- Participación en el curso de Narrativa Audiovisual (PUCP)  
- Aprobación de cursos clave en lenguaje visual, guion y fotografía  

Estas experiencias fortalecen mis herramientas expresivas como comunicadora audiovisual.
    """)

with tabs[5]:
    st.image("https://i.imgur.com/0X6n0xJ.jpg", caption="Maya · compañía e inspiración", use_column_width=True)
    st.subheader("HOBBIES · Referencias personales")
    st.markdown("""
- Escuchar música (K-pop, Taylor Swift, playlists lo-fi)  
- Ver series con cuidado estético, como k-dramas  
- Disfrutar de una taza de té en momentos tranquilos  
- Compartir tiempo con mi mascota, Maya, fuente de compañía e inspiración  

Estas referencias personales alimentan mi mirada creativa.
    """)

with tabs[6]:
    st.subheader("CONTACTO")
    st.markdown("""
Puedes escribirme a:  
**thaisgchoque@gmail.com**

Estoy abierta a seguir aprendiendo, creando y compartiendo.
    """)
```
