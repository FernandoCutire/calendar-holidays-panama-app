import streamlit as st
from streamlit_calendar import calendar

# Adding custom components
from src.components.sidebar import create_sidebar
from src.components.calendar import create_calendar
from src.components.instructions import instructions

# Adding data
from data.holidays_panama import events

st.set_page_config(page_title="Calendario de feriados Panamá"
                   , page_icon="🇵🇦"
                   )

# Sidebar Component
create_sidebar()

st.markdown(
    "## Calendario de Feriados Panamá 2024 📅 "
)

st.info(
    "Calendario de Feriados de Panamá en el año 2024. Puedes cambiar la vista del calendario en el menú desplegable.")

instructions()

mode = st.selectbox(
    "Calendario:",
    (
        "Mensual",
        "Semanal",
        "Lista"
    ),
)

state = create_calendar(events, mode)
