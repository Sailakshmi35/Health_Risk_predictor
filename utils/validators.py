import re
from datetime import date


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)


def validate_dob(dob):

    today = date.today()

    return dob <= today


def validate_blood_values(
        glucose,
        haemoglobin,
        cholesterol):

    try:
        float(glucose)
        float(haemoglobin)
        float(cholesterol)

        return True

    except ValueError:
        return False