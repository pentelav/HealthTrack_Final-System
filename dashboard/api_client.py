# Integrated dashboard app to patient risk assessment API to send patient data, get risk history.
# The functions assess_patient_risk and get_risk_history were used to send and retrieve patient's risk information.

import requests

# Defining backend API address
API_URL = "http://127.0.0.1:8000"

# Sending patient risk assessment request
def assess_patient_risk(data):

    try:

        # Sending risk data request
        response = requests.post(

            f"{API_URL}/api/risk-assessment",

            json=data

        )


        # Checking successful response
        if response.status_code == 200:

            # Returning risk details
            return response.json()


        # Returning API failure message
        return {

            "error":"Risk API failed"

        }


    except Exception as e:

        # Returning error details
        return {

            "error":str(e)

        }






# Fetching patient risk history
def get_risk_history(user_id):

    try:

        # Sending history request
        response = requests.get(

            f"{API_URL}/api/risk-history/{user_id}"

        )


        # Checking successful response
        if response.status_code == 200:

            # Returning risk history
            return response.json()


        # Returning empty history
        return []


    except:

        # Returning empty history
        return []