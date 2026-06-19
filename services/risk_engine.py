def calculate_risk(
        glucose,
        haemoglobin,
        cholesterol):

    score = 0

    # Glucose

    if glucose > 180:
        score += 40

    elif glucose > 140:
        score += 20

    # Cholesterol

    if cholesterol > 240:
        score += 40

    elif cholesterol > 200:
        score += 20

    # Haemoglobin

    if haemoglobin < 11:
        score += 20

    # Final Risk

    if score >= 60:
        return "High"

    elif score >= 30:
        return "Moderate"

    return "Low"