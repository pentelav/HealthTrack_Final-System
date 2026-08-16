# Designed patient risk assessment form and structured it with fields, assessment button and outcome display.
# Introduced the health risk layout component for a structured interface for collecting health values and displaying health risk results.

from dash import html,dcc

import dash_bootstrap_components as dbc



# Creating risk assessment layout
risk_layout = dbc.Container([


    # Adding risk assessment heading
    html.H2(
        "Patient Risk Assessment"
    ),



    # Creating patient input row
    dbc.Row([


        # Adding age input
        dbc.Col(
            dcc.Input(
                id="risk-age",
                placeholder="Age",
                type="number"
            )
        ),



        # Adding heart rate input
        dbc.Col(
            dcc.Input(
                id="risk-heart",
                placeholder="Heart Rate",
                type="number"
            )
        ),



        # Adding oxygen input
        dbc.Col(
            dcc.Input(
                id="risk-oxygen",
                placeholder="Oxygen",
                type="number"
            )
        )


    ]),



    html.Br(),



    # Adding risk assessment button
    dbc.Button(
        "Assess Risk",
        id="assess-risk-btn",
        color="danger"
    ),



    html.Hr(),



    # Adding risk result display
    html.Div(
        id="risk-output"
    )

])