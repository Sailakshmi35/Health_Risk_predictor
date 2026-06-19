import streamlit as st
import pandas as pd

from database.db import get_all_patients


def show():

    st.header("📋 View Patients")

    patients = get_all_patients()

    if not patients:
        st.warning("No Patient Records Found")
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

    search = st.text_input(
        "Search Patient"
    )

    if search:

        df = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
    label="📥 Download Patient Report",
    data=csv,
    file_name="patients_report.csv",
    mime="text/csv"
)

    st.dataframe(
        df,
        width = "stretch"
    )