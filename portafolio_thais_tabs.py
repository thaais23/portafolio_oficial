
import streamlit as st

# ConfiguraciÃ³n general
st.set_page_config(page_title="Portafolio de Thais Choque", layout="wide")

# Estilos personalizados
st.markdown(
    """
    <style>
    body {
        background-color: #fffaf0 !important;
        color: #2e2e2e !important;
    }
    .stApp {
        background-color: #ffffff !important;
    }
    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
        color: #2e2e2e !important;
    }
    h1, h2, h3 {
        color: #772f40 !important;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TÃ­tulo principal e imagen circular
st.markdown("<h1 style='text-align: center;'>Portafolio de Thais Choque</h1>", unsafe_allow_html=True)
st.image("P1020006.jpg.png", caption="Thais Choque", width=200)

st.write("Estudiante de ComunicaciÃ³n Audiovisual en la PUCP")
st.write("Este portafolio reÃºne aspectos de mi formaciÃ³n, intereses creativos y sensibilidad estÃ©tica en desarrollo.")

# Tabs principales
tabs = st.tabs([
    "INICIO", "RESUME", "EXPLORACIONES CREATIVAS", "RESEARCH", "ACHIEVEMENTS", "HOBBIES", "CONTACTO"
])

with tabs[0]:
    st.subheader("Bienvenida")
    st.markdown("""
Este espacio contiene:

- RESUME Â· Perfil acadÃ©mico
- EXPLORACIONES CREATIVAS Â· PrÃ¡cticas y aprendizajes
- RESEARCH Â· Intereses en desarrollo
- ACHIEVEMENTS Â· Participaciones formativas
- HOBBIES Â· Gustos personales con valor creativo
- CONTACTO Â· InformaciÃ³n de contacto

Gracias por visitar este espacio.
    """)

with tabs[1]:
    st.subheader("RESUME Â· Perfil acadÃ©mico")
    st.markdown("""
**FormaciÃ³n**  
- ComunicaciÃ³n Audiovisual en la PUCP (5to ciclo)  
- Cursos enfocados en narrativa visual, lenguaje audiovisual, fotografÃ­a y ediciÃ³n  

**Habilidades**  
- EdiciÃ³n bÃ¡sica de video  
- FotografÃ­a y composiciÃ³n  
- Trabajo colaborativo y planificaciÃ³n  
- InterÃ©s por nuevas herramientas digitales  

**Idiomas**  
- EspaÃ±ol (nativo)  
- InglÃ©s (avanzado)  

Me encuentro en formaciÃ³n, con interÃ©s en aplicar estos aprendizajes en proyectos creativos y colaborativos.
    """)

with tabs[2]:
    st.subheader("EXPLORACIONES CREATIVAS")
    st.image("IMG-20250624-WA0019.jpg.jpg", caption="ExploraciÃ³n visual", use_column_width=True)
    st.markdown("""
**Ejercicios fotogrÃ¡ficos**  
ExploraciÃ³n con luz natural, retratos y composiciÃ³n. Me interesa cÃ³mo la imagen puede sugerir atmÃ³sferas sutiles.

**AnÃ¡lisis de escenas visuales**  
ObservaciÃ³n de planos, ritmo narrativo y silencios. Herramientas valiosas para comprender la estructura cinematogrÃ¡fica.

**CreaciÃ³n audiovisual en grupo**  
He participado en la escritura y planificaciÃ³n de escenas. Valoro el trabajo colaborativo y la construcciÃ³n narrativa colectiva.
    """)

with tabs[3]:
    st.subheader("RESEARCH Â· Intereses en desarrollo")
    st.markdown("""
Actualmente me interesa explorar temas como:

- RepresentaciÃ³n de lo cotidiano en el cine y las series  
- Personajes femeninos en narrativas visuales  
- EstÃ©tica visual en redes sociales  
- Impacto emocional de las historias audiovisuales  
- Colores, texturas y silencios como generadores de atmÃ³sfera  

Estas Ã¡reas reflejan mi bÃºsqueda personal y posibles caminos profesionales.
    """)

with tabs[4]:
    st.subheader("ACHIEVEMENTS Â· Participaciones formativas")
    st.markdown("""
- ParticipaciÃ³n en el curso de Narrativa Audiovisual (PUCP)  
- AprobaciÃ³n de cursos clave en lenguaje visual, guion y fotografÃ­a  

Estas experiencias fortalecen mis herramientas expresivas como comunicadora audiovisual.
    """)

with tabs[5]:
    st.subheader("HOBBIES Â· Referencias personales")
    st.image("IMG_2856.JPG", caption="Maya Â· compaÃ±Ã­a e inspiraciÃ³n", use_column_width=True)
    st.markdown("""
- Escuchar mÃºsica (K-pop, Taylor Swift, playlists lo-fi)  
- Ver series con cuidado estÃ©tico, como k-dramas  
- Disfrutar de una taza de tÃ© en momentos tranquilos  
- Compartir tiempo con mi mascota, Maya, fuente de compaÃ±Ã­a e inspiraciÃ³n  

Estas referencias personales alimentan mi mirada creativa.
    """)

with tabs[6]:
    st.subheader("CONTACTO")
    st.markdown("""
Puedes escribirme a:  
**thaisgchoque@gmail.com**

Estoy abierta a seguir aprendiendo, creando y compartiendo.
    """)
