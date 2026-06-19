import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_health_assessment(
        glucose,
        haemoglobin,
        cholesterol,
        risk_level):

    prompt = f"""
    You are a healthcare assistant.

    Patient Blood Test Results:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Risk Level: {risk_level}

    Provide:
    1. Possible health concerns
    2. Risk summary
    3. Lifestyle recommendations

    Keep response under 100 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text