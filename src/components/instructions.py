import streamlit as st


def instructions():
    with st.expander("**📖 ¿Cómo usar este calendario?**"):
        st.markdown("""
                            Este calendario ofrece tres vistas diferentes: mensual, semanal y una lista que incluye todos los eventos del año. 

                            Puedes cambiar entre estas vistas utilizando el menú desplegable que se encuentra en la parte superior de la página. 

                            En una sesión de trabajo típica, puedes encontrar útil cambiar entre estas vistas dependiendo de tus necesidades. Por ejemplo, la vista mensual puede ser útil para obtener una visión general de los eventos del mes, mientras que la vista semanal puede ser útil para planificar tu semana. La vista de lista te proporciona una lista completa de todos los eventos del año.

                            """)

        st.info("""**Nota:** Los eventos mostrados en este calendario son correspondientes al año 2024 para Panamá. 
                    Estos datos son actualizados periódicamente por lo que no podrás ver datos para el año 2025 en adelante. Así cómo para años anteriores.
                            """)

        st.markdown("""
                            Si encuentras que falta algún evento o tienes alguna sugerencia para mejorar el calendario, no dudes en contactarme directamente [aquí](https://www.linkedin.com/in/fernandocutire/)

                            Además, te invito a que eches un vistazo a mis otros proyectos que puedes encontrar en la barra lateral. 

                            ¡Ahora, disfruta utilizando el calendario! 🚀

                    """)
