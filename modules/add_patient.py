import streamlit as st
from datetime import date
from database.db import add_patient
from services.risk_engine import calculate_risk
from services.ai_service import generate_health_assessment
from utils.validators import (
    validate_email,
    validate_blood_values,
    
)


def show():

    st.header("➕ Add Patient")

    full_name = st.text_input("Full Name")

    
    dob = st.date_input(
        "Date of Birth",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )
    email = st.text_input("Email")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0
    )

    if st.button("Generate Assessment"):

        if not full_name.strip():
            st.error("Full Name is required")
            return

        if not validate_email(email):
            st.error("Invalid Email")
            return

        if not validate_blood_values(
                glucose,
                haemoglobin,
                cholesterol):
            st.error("Invalid Blood Values")
            return

        risk_level = calculate_risk(
            glucose,
            haemoglobin,
            cholesterol
        )

        with st.spinner("Generating AI Assessment..."):

            remarks = generate_health_assessment(
                glucose,
                haemoglobin,
                cholesterol,
                risk_level
            )

        add_patient(
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            risk_level,
            remarks
        )

        st.success("Patient Added Successfully")

        st.subheader("Risk Level")
        st.write(risk_level)

        st.subheader("AI Assessment")
        st.write(remarks)