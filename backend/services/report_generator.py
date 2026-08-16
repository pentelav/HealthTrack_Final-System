# Produced patient health briefs with crucial information, hazard details, and healthcare suggestions.
# Handled generate_report function to collect health data, prepare report content, and return patient information.

from database.models import (

    RiskHistory,

    HealthRecord

)




# Generating patient health report
def generate_report(

    user_id,

    db

):


    # Retrieving health records
    records=(

        db.query(

            HealthRecord

        )

        .filter(

            HealthRecord.user_id==user_id

        )

        .all()

    )



    # Retrieving risk history
    risks=(

        db.query(

            RiskHistory

        )

        .filter(

            RiskHistory.user_id==user_id

        )

        .all()

    )



    # Creating report content
    report = ""



    # Adding report title
    report += (

        "HealthTrack Patient Report\n"

    )



    # Adding report separator
    report += (

        "===========================\n\n"

    )



    # Adding patient identifier
    report += (

        f"Patient ID: {user_id}\n\n"

    )



    # Adding health record count
    report += (

        f"Total Health Records: {len(records)}\n"

    )



    # Adding risk assessment count
    report += (

        f"Risk Assessments: {len(risks)}\n\n"

    )



    # Checking health record availability
    if records:


        # Selecting latest health record
        latest = records[-1]


        # Adding latest vital details
        report += "Latest Vital Information:\n"


        # Adding heart rate details
        report += (

            f"Heart Rate: {latest.heart_rate} bpm\n"

        )


        # Adding oxygen details
        report += (

            f"Oxygen: {latest.oxygen}%\n"

        )


        # Adding temperature details
        report += (

            f"Temperature: {latest.temperature} C\n"

        )



    # Adding risk summary section
    report += "\nRisk Summary:\n"



    # Checking risk history availability
    if risks:


        # Selecting latest risk record
        latest_risk = risks[-1]


        # Adding risk score details
        report += (

            f"Risk Score: "

            f"{latest_risk.risk_score}\n"

        )


        # Adding risk level details
        report += (

            f"Risk Level: "

            f"{latest_risk.risk_level}\n"

        )


        # Adding prediction details
        report += (

            f"Prediction: "

            f"{latest_risk.prediction}\n"

        )


    else:


        # Adding missing risk message
        report += (

            "No risk assessment available\n"

        )



    # Adding recommendation section
    report += "\nRecommendations:\n"



    # Adding health monitoring recommendation
    report += (

        "- Maintain regular health monitoring\n"

    )


    # Adding healthcare guidance recommendation
    report += (

        "- Follow healthcare provider guidance\n"

    )


    # Adding health pattern recommendation
    report += (

        "- Review abnormal health patterns\n"

    )



    # Returning report content
    return report