# Developed a patient risk assessment form and added the necessary input boxes for health parameters and risk evaluation.
# Call create_risk_form function to create the risk assessment layout including user input and results display.

from dash import html, dcc

# Creating risk assessment form
def create_risk_form():

    # Returning form layout
    return html.Div(

        [

            # Adding form heading
            html.H2(
                "Patient Risk Assessment"
            ),


            # Adding age input
            dcc.Input(
                id="age",
                placeholder="Age",
                type="number"
            ),

            html.Br(),


            # Adding heart rate input
            dcc.Input(
                id="heart_rate",
                placeholder="Heart Rate",
                type="number"
            ),

            html.Br(),


            # Adding oxygen input
            dcc.Input(
                id="oxygen",
                placeholder="Oxygen Level",
                type="number"
            ),

            html.Br(),


            # Adding blood pressure input
            dcc.Input(
                id="blood_pressure",
                placeholder="Blood Pressure",
                type="number"
            ),

            html.Br(),


            # Adding BMI input
            dcc.Input(
                id="bmi",
                placeholder="BMI",
                type="number"
            ),

            html.Br(),


            # Adding blood sugar input
            dcc.Input(
                id="blood_sugar",
                placeholder="Blood Sugar",
                type="number"
            ),

            html.Br(),


            # Adding cholesterol input
            dcc.Input(
                id="cholesterol",
                placeholder="Cholesterol",
                type="number"
            ),

            html.Br(),


            # Adding diabetes input
            dcc.Input(
                id="diabetes",
                placeholder="Diabetes 1 or 0",
                type="number"
            ),

            html.Br(),


            # Adding smoking input
            dcc.Input(
                id="smoking",
                placeholder="Smoking 1 or 0",
                type="number"
            ),

            html.Br(),


            # Adding exercise input
            dcc.Input(
                id="exercise",
                placeholder="Exercise 1 or 0",
                type="number"
            ),

            html.Br(),
            html.Br(),


            # Adding risk assessment button
            html.Button(
                "Assess Risk",
                id="risk-button"
            ),


            # Adding result display area
            html.Div(
                id="risk-result"
            )

        ],


        # Adding form spacing
        style={
            "padding":"20px"
        }

    )