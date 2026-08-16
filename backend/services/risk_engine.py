# Determined a patient health risk score based on a dictionary of health parameters and set risk levels.
# Pass calculate_risk function with health conditions to determine risk score and assign the risk score category.

# Calculating patient risk score
def calculate_risk(data):


    # Initializing risk score
    score = 0



    # Checking age risk
    if data["age"] >= 60:

        score += 20

    elif data["age"] >= 45:

        score += 10



    # Checking heart rate risk
    if data["heart_rate"] > 120:

        score += 20

    elif data["heart_rate"] < 50:

        score += 15



    # Checking oxygen risk
    if data["oxygen"] < 90:

        score += 25

    elif data["oxygen"] < 95:

        score += 10



    # Checking blood pressure risk
    if data["blood_pressure"] >= 160:

        score += 20

    elif data["blood_pressure"] >= 140:

        score += 10



    # Checking BMI risk
    if data["bmi"] >= 30:

        score += 10



    # Checking blood sugar risk
    if data["blood_sugar"] >= 200:

        score += 15

    elif data["blood_sugar"] >= 140:

        score += 8



    # Checking cholesterol risk
    if data["cholesterol"] >= 240:

        score += 10



    # Checking diabetes risk
    if data["diabetes"] == 1:

        score += 15



    # Checking smoking risk
    if data["smoking"] == 1:

        score += 10



    # Checking exercise risk
    if data["exercise"] == 0:

        score += 5



    # Assigning risk level
    if score >= 80:

        level = "High Risk"


    elif score >= 40:

        level = "Moderate Risk"


    else:

        level = "Low Risk"



    # Returning risk details
    return {

        "risk_score": score,

        "risk_level": level

    }