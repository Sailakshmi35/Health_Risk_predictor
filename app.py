import streamlit as st

from database.db import create_table
from modules.add_patient import show as add_patient_page
from modules.view_patients import show as view_patients_page
from modules.analytics import show as analytics_page

create_table()

st.set_page_config(
    page_title="Health Intelligence",
    layout="wide"
)

st.sidebar.title("🏥 Health Risk Predictor")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Add Patient",
        "View Patients",
        "Analytics"
    ]
)

if menu == "Add Patient":
    add_patient_page()

elif menu == "View Patients":
    view_patients_page()
elif menu == "Analytics":
    analytics_page()