# Retrieved healthcare alert data from the API and managed alert response data from the alert management system.
# The check_alerts function is used to submit alert information and to retrieve information about available alerts.

import requests

# Defining API address
API_URL = "http://127.0.0.1:8000"



# Checking alert records
def check_alerts():

    try:

        # Sending alert request
        response = requests.get(

            f"{API_URL}/api/alerts"

        )


        # Checking successful response
        if response.status_code == 200:

            # Returning alert records
            return response.json()


        # Returning empty alert list
        return []


    except Exception:

        # Returning empty alert list
        return []