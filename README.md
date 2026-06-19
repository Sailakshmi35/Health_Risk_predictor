#🏥 Health Risk Predictor
###About the Project

Health Risk Predictor is an AI-powered healthcare application that helps analyze patient health data and identify potential health risks.

The application collects patient information and blood test values such as:

Glucose
Haemoglobin
Cholesterol

Based on these values, the system predicts whether the patient falls into:

Low Risk
Moderate Risk
High Risk

The application also uses Google's Gemini AI to generate health recommendations and insights.

#Features
###Add Patient

Users can enter:

Full Name
Date of Birth
Email
Glucose Level
Haemoglobin Level
Cholesterol Level


###Risk Prediction

The system analyzes the patient's health values and predicts the risk level.

Example:

Normal values → Low Risk
Slightly abnormal values → Moderate Risk
Highly abnormal values → High Risk

###AI Health Assessment

Google Gemini AI generates:
Possible health concerns
Risk summary
Lifestyle recommendations
Preventive health suggestions


###View Patients

Users can view all stored patient records.

###Analytics Dashboard

The application provides charts and visual reports showing:

Number of patients
Risk distribution
Health statistics


###Technologies Used

Python
Streamlit
SQLite
Pandas
Plotly
Google Gemini API


###Project Structure
Health-Risk-Predictor
│
├── app.py
├── database
├── services
├── modules
├── utils
├── assets
├── patients.db
├── requirements.txt
└── README.md


#How the Application Works
Step 1

The user enters patient details and blood test values.

Step 2

The application validates the entered information.

Step 3

The Risk Engine analyzes the blood values and calculates the risk level.

Step 4

The patient information is sent to Gemini AI.

Step 5

Gemini AI generates health recommendations.

Step 6

All information is stored in the SQLite database.

Step 7

The Analytics Dashboard displays patient statistics and charts.