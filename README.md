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

<img width="1371" height="838" alt="Screenshot 2026-06-18 223033" src="https://github.com/user-attachments/assets/b474d386-5736-4e3e-983a-c253670867c1" />

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

<img width="1866" height="666" alt="Screenshot 2026-06-18 223059" src="https://github.com/user-attachments/assets/08317e9c-d242-44f1-b5c7-74a0b30e908d" />



<img width="1837" height="822" alt="Screenshot 2026-06-18 223124" src="https://github.com/user-attachments/assets/7bdd45f6-6375-4318-8915-f13c8b2b11b2" />



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
