# Using risk parameters and calculated risk points from health values, predict the condition of the patients.
# Pass predict_risk function to test condition and return either medical attention or healthy.

# Predicting patient risk condition
def predict_risk(data):


    # Initializing risk points
    risk_points = 0



    # Checking oxygen condition
    if data["oxygen"] < 90:

        risk_points += 1



    # Checking heart rate condition
    if data["heart_rate"] > 120:

        risk_points += 1



    # Checking blood pressure condition
    if data["blood_pressure"] >= 140:

        risk_points += 1



    # Checking blood sugar condition
    if data["blood_sugar"] >= 200:

        risk_points += 1



    # Checking diabetes condition
    if data["diabetes"] == 1:

        risk_points += 1



    # Checking smoking condition
    if data["smoking"] == 1:

        risk_points += 1





    # Assigning medical attention status
    if risk_points >= 3:

        return "Needs Medical Attention"


    # Assigning healthy status
    else:

        return "Healthy"