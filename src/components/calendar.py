# calendar.py
import streamlit as st
from streamlit_calendar import calendar

def create_calendar(events, mode):
    calendar_options = {
        "editable": "true",
        "navLinks": "true",
        "selectable": "true",
    }

    if "resource" in mode:
        if mode == "resource-daygrid":
            calendar_options = {
                **calendar_options,
                "initialDate": "2024-01-01",
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            }
    else:
        if mode == "Semanal":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": "2024-01-01",
                "initialView": "dayGridWeek",
            }


        elif mode == "Lista":
            calendar_options = {
                **calendar_options,
                "initialDate": "2024-01-01",
                "initialView": "listYear",
            }
        elif mode == "Mensual":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "",  # Disable the left navigation buttons
                    "center": "title",
                    "right": "",
                },
                "initialDate": "2024-01-01",
                "initialView": "multiMonthYear",
            }

    state = calendar(
        events=st.session_state.get("events", events),
        options={**calendar_options},
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key=mode,
    )

    if state.get("eventsSet") is not None:
        st.session_state["events"] = state["eventsSet"]

    return state
