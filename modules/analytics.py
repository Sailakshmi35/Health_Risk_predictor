import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_all_patients


def show():

    st.header("📊 Analytics Dashboard")

    patients = get_all_patients()

    if not patients:
        st.warning("No Data Available")
        return

    columns = [
        "ID",
        "Name",
        "DOB",
        "Email",
        "Glucose",
        "Haemoglobin",
        "Cholesterol",
        "Risk Level",
        "Remarks"
    ]

    df = pd.DataFrame(
        patients,
        columns=columns
    )

    total_patients = len(df)

    high_risk = len(
        df[df["Risk Level"] == "High"]
    )

    moderate_risk = len(
        df[df["Risk Level"] == "Moderate"]
    )

    low_risk = len(
        df[df["Risk Level"] == "Low"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Patients",
        total_patients
    )

    col2.metric(
        "High Risk",
        high_risk
    )

    col3.metric(
        "Moderate Risk",
        moderate_risk
    )

    col4.metric(
        "Low Risk",
        low_risk
    )

    st.subheader("Risk Distribution")

    risk_counts = (
        df["Risk Level"]
        .value_counts()
        .reset_index()
    )

    risk_counts.columns = [
        "Risk Level",
        "Count"
    ]

    fig = px.pie(
        risk_counts,
        names="Risk Level",
        values="Count",
        title="Patient Risk Distribution"
    )

    st.plotly_chart(
        fig,
        width = "stretch"
    )