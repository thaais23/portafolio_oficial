
import streamlit as st

# 🎨 Estilo Gilmore Girls
st.markdown(
    """<style>
    .stApp {
        background-color: #fdf6f0;
    }
    html, body, [class*="css"] {
        color: #3c2a2a;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #8b1e3f;
    }
    .css-1d391kg {
        background-color: #f5e8dd !important;
    }
    </style>""",
    unsafe_allow_html=True
)

st.set_page_config(page_title="Portafolio de Thais", layout="wide")

# Título principal
st.markdown("<h1 style='text-align: center; color: #e07a9b;'>🌸 Portafolio de Thais Choque 🌸</h1>", unsafe_allow_html=True)
st.write("Estudiante de Comunicación Audiovisual en la PUCP ☕📚")
st.write("Este portafolio es una muestra personal y profesional de mi formación, intereses y estilo visual. Aquí comparto parte de mi proceso, desde lo que estoy aprendiendo hasta lo que me inspira en el camino audiovisual. 🌿✨")

# Tabs
tabs = st.tabs([
    "🏠 Inicio", "📄 Resume", "🌱 Exploraciones creativas", "🔍 Research", "🏅 Achievements", "🎧 Hobbies", "✉️ Contact"
])

with tabs[0]:
    st.image("https://i.imgur.com/sDaRtnt.jpg", caption="Mood visual · cozy, cálido, suave", use_column_width=True)
    st.subheader("🗂️ Aquí puedes encontrar:")
    st.markdown("""
- 📄 Resume · Perfil académico  
- 🌱 Exploraciones creativas · Prácticas y aprendizajes  
- 🔍 Research · Intereses en desarrollo  
- 🏅 Achievements · Participaciones formativas  
- 🎧 Hobbies · Gustos personales que inspiran mi mirada  
- ✉️ Contact · Información de contacto

Gracias por visitar este espacio creativo 🍂
    """)

with tabs[1]:
    st.subheader("📄 Resume · Perfil académico")
    st.markdown("""
**🎓 Educación**  
- Comunicación Audiovisual en la PUCP (5to ciclo)  
- Cursos centrados en narrativa visual, lenguaje audiovisual, fotografía y edición  

**🛠️ Habilidades**  
- Edición básica de video  
- Fotografía y composición visual  
- Trabajo en equipo y planificación  
- Interés constante por nuevas herramientas digitales  

**🌐 Idiomas**  
- Español (nativo)  
- Inglés (avanzado)

Me encuentro en formación, con interés en aplicar estos aprendizajes en proyectos creativos y colaborativos.
    """)

with tabs[2]:
    st.image("https://i.imgur.com/XCE9PBR.jpg", caption="Inspiración visual 🎥", use_column_width=True)
    st.subheader("🌱 Exploraciones creativas · Prácticas y aprendizajes")
    st.markdown("""
📷 **Ejercicios fotográficos**  
Durante los cursos he trabajado con luz natural, retratos y composición. Me interesa explorar cómo una imagen puede transmitir atmósferas sutiles y emocionales.  

🎬 **Análisis de escenas visuales**  
He desarrollado habilidades para observar planos, ritmos narrativos y silencios significativos en obras audiovisuales. Esta observación enriquece mi comprensión de la narración cinematográfica.  

📝 **Creación de historias audiovisuales (trabajo en grupo)**  
He participado en procesos colaborativos de escritura y planificación visual de escenas. Valoro el trabajo en equipo y la posibilidad de construir relatos desde distintas perspectivas.  
    """)

with tabs[3]:
    st.subheader("🔍 Research · Intereses en desarrollo")
    st.markdown("""
Actualmente me encuentro explorando temas que podrían convertirse en líneas de investigación o creación a futuro:

- 🌆 La representación de lo cotidiano en el cine y las series  
- 🎭 Personajes femeninos en narrativas visuales  
- 💻 Estética visual en redes sociales y plataformas digitales  
- 🧠 Cómo las historias afectan nuestras emociones y memoria  
- 🍂 El uso de colores, texturas y silencios en la construcción de atmósferas  

Estos intereses reflejan tanto una búsqueda personal como una posible línea de desarrollo profesional a futuro.
    """)

with tabs[4]:
    st.subheader("🏅 Achievements · Participaciones formativas")
    st.markdown("""
- 📝 Participación en el curso de Narrativa Audiovisual en la PUCP  
- 🎓 Aprobación de cursos clave en lenguaje visual, guion y fotografía  

Estas experiencias han contribuido a fortalecer mis bases narrativas y visuales como comunicadora audiovisual.
    """)

with tabs[5]:
    st.image("https://i.imgur.com/0X6n0xJ.jpg", caption="Con mi mascota, Maya 🐾✨", use_column_width=True)
    st.subheader("🎧 Hobbies · Gustos personales que inspiran mi mirada")
    st.markdown("""
- 🎶 Escuchar música: K-pop, Taylor Swift y playlists suaves  
- 📺 Ver k-dramas y series con cuidado estético  
- 🍵 Disfrutar una taza de té mientras escucho música o veo algo inspirador  
- 🐾 Pasar tiempo con mi mascota, Maya, que me acompaña en muchos momentos creativos  

Estas actividades, aunque personales, nutren la sensibilidad con la que miro el mundo audiovisual.  
    """)

with tabs[6]:
    st.subheader("✉️ Contact · Información de contacto")
    st.markdown("""
Si quieres contactarme, puedes escribirme a:  
📬 **thaisgchoque@gmail.com**

Gracias por visitar este espacio. Me encantaría seguir aprendiendo, creando y compartiendo. 🎥📩
    """)
