# Collected patient vital signs and triggered severity-based notifications with the health care thresholds.
# Handled functions generate_alerts and evaluate_patient_condition to detect abnormal conditions and return health status.

from app.config import (

    HEART_RATE_LIMIT,

    OXYGEN_LIMIT,

    TEMPERATURE_LIMIT

)



# Generating health alerts
def generate_alerts(vitals):


    # Creating alert list
    alerts = []


    # Reading heart rate value
    heart_rate = (

        vitals.get(

            "heart_rate",

            0

        )

    )


    # Reading oxygen value
    oxygen = (

        vitals.get(

            "oxygen",

            100

        )

    )


    # Reading temperature value
    temperature = (

        vitals.get(

            "temperature",

            0

        )

    )



    # Checking heart rate condition
    if heart_rate > HEART_RATE_LIMIT:


        # Adding high heart rate alert
        alerts.append(

            {

                "type":

                "High Heart Rate",

                "severity":

                "CRITICAL",

                "message":

                f"Heart rate {heart_rate} bpm exceeds safe limit"

            }

        )



    # Checking oxygen condition
    if oxygen < OXYGEN_LIMIT:


        # Adding low oxygen alert
        alerts.append(

            {

                "type":

                "Low Oxygen Level",

                "severity":

                "CRITICAL",

                "message":

                f"Oxygen level {oxygen}% is below normal range"

            }

        )



    # Checking temperature condition
    if temperature > TEMPERATURE_LIMIT:


        # Adding high temperature alert
        alerts.append(

            {

                "type":

                "High Temperature",

                "severity":

                "HIGH",

                "message":

                f"Temperature {temperature}°C requires attention"

            }

        )



    # Returning generated alerts
    return alerts





# Evaluating patient condition
def evaluate_patient_condition(vitals):


    # Generating patient alerts
    alerts = generate_alerts(

        vitals

    )


    # Checking normal condition
    if len(alerts)==0:


        # Returning normal status
        return {

            "status":

            "NORMAL",

            "alerts":

            []

        }



    # Returning abnormal status
    return {

        "status":

        "ABNORMAL",

        "alerts":

        alerts

    }