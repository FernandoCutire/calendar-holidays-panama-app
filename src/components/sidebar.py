# sidebar.py
import streamlit as st


def create_sidebar():
    # Crear un sidebar
    sidebar = st.sidebar

    # Agregar un título al sidebar
    sidebar.title("Calendario Feriados Panamá 2024 🇵🇦")

    st.sidebar.caption("Hecho por [Fernando Cutire](https://www.linkedin.com/in/fernandocutire/)")

    with sidebar.expander("Contacto"):
        st.caption(
            "LinkedIn: [Fernando Cutire](https://www.linkedin.com/in/fernandocutire/) 📝")
        st.caption("Github: [Github](https://github.com/FernandoCutire) 🐙")
        st.caption("Página web: [Página](https://fernandocutire.com) 🌐")

    with sidebar.expander("Otros proyectos"):
        st.caption(
            "Grow Youtube: [Grow](https://www.youtube.com/@IniciativaGrow) 🛫")
        st.caption(
            "Online CV: [CV](https://fernandocutire.resoume.com/) 📝")
        st.caption(
            "Create your CV with code: [CV with Code](https://github.com/FernandoCutire/online-resume-as-code) 🤖")

    with sidebar.expander("Fuentes y Recursos"):
        st.caption(
            "Feriados Panamá 2024 por Telemetro Reporta: [Telemetro Reporta](https://www.telemetro.com/nacionales/calendario-feriados-panama-2024-todos-los-dias-no-laborables-y-festivos-n5953115) 🎈")

    st.sidebar.info("""
      Nota: Los datos de los feriados son correspondientes al año 2024 para Panamá. 
      Estos datos son actualizados periódicamente por lo que no podrá ver datos para el año 2025 en adelante. 
      Así cómo para años anteriores.
        """)
