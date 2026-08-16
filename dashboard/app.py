# Developed HealthTrack dashboard to provide real-time patient vitals, chart of patient heart rate, alerts, risk assessment and recommendations.
# Executed update_dashboard and assess_risk functions to update monitoring information and to run patient risk assessment.

from dash import Dash, html, dcc

from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

import datetime

import requests


from components.cards import create_card

from components.charts import create_line_chart

from websocket_client import get_latest_data

from alert_system import check_alerts



# Defining backend API URL
API_URL = "http://127.0.0.1:8000"



# Creating Dash application
app = Dash(

    __name__,

    external_stylesheets=[

        dbc.themes.BOOTSTRAP

    ]

)



# Setting dashboard title
app.title = "HealthTrack Dashboard"



# Creating history storage
heart_history = []

time_history = []





# Creating dashboard layout
app.layout = dbc.Container(

[


    # Adding dashboard heading
    html.H1(

        "HealthTrack Real-Time Health Dashboard",

        className="header"

    ),



    # Adding connection display
    html.Div(

        id="connection",

        className="connection"

    ),




    # Adding vital cards
    dbc.Row(

        [

            dbc.Col(

                create_card(

                    "Heart Rate",

                    "heart"

                ),

                width=4

            ),


            dbc.Col(

                create_card(

                    "Oxygen Level",

                    "oxygen"

                ),

                width=4

            ),



            dbc.Col(

                create_card(

                    "Temperature",

                    "temperature"

                ),

                width=4

            )

        ]

    ),




    # Adding heart rate chart
    dcc.Graph(

        id="heart-chart"

    ),





    # Adding alert section
    html.H3(

        "Patient Alerts"

    ),



    html.Div(

        id="alerts"

    ),



    # Adding risk assessment section
    html.H3(

        "Patient Risk Assessment"

    ),




    dbc.Row(

        [

            # Adding age input
            dbc.Col(

                dbc.Input(

                    id="age",

                    placeholder="Age",

                    type="number"

                )

            ),



            # Adding heart rate input
            dbc.Col(

                dbc.Input(

                    id="risk-heart",

                    placeholder="Heart Rate",

                    type="number"

                )

            ),



            # Adding oxygen input
            dbc.Col(

                dbc.Input(

                    id="risk-oxygen",

                    placeholder="Oxygen Level",

                    type="number"

                )

            )


        ]

    ),




    html.Br(),




    # Adding risk button
    dbc.Button(

        "Assess Risk",

        id="risk-button",

        color="danger"

    ),




    html.Br(),

    html.Br(),




    # Adding risk result display
    html.Div(

        id="risk-result"

    ),





    # Adding refresh control
    dcc.Interval(

        id="refresh",

        interval=2000,

        n_intervals=0

    )


],


fluid=True


)







# Updating dashboard data
@app.callback(

    [

        Output("heart","children"),

        Output("oxygen","children"),

        Output("temperature","children"),

        Output("heart-chart","figure"),

        Output("alerts","children"),

        Output("connection","children")

    ],


    Input(

        "refresh",

        "n_intervals"

    )

)



# Refreshing monitoring details
def update_dashboard(n):


    # Fetching latest sensor data
    data = get_latest_data()



    # Reading heart rate value
    heart = data.get(

        "heart_rate",

        0

    )



    # Reading oxygen value
    oxygen = data.get(

        "oxygen",

        0

    )



    # Reading temperature value
    temperature = data.get(

        "temperature",

        0

    )




    # Storing heart rate history
    heart_history.append(

        heart

    )



    # Storing time history
    time_history.append(

        datetime.datetime.now()

    )



    # Limiting history values
    if len(heart_history) > 50:


        heart_history.pop(0)

        time_history.pop(0)





    # Fetching alert details
    alerts = check_alerts()



    # Creating alert display
    alert_box=[]



    # Adding alert messages
    for alert in alerts:


        alert_box.append(

            html.Div(

                alert.get(

                    "message",

                    "Alert"

                ),

                style={

                    "backgroundColor":"red",

                    "color":"white",

                    "padding":"10px"

                }

            )

        )




    # Showing normal condition
    if not alert_box:


        alert_box.append(

            html.Div(

                "Patient Condition Normal",

                style={

                    "backgroundColor":"green",

                    "color":"white",

                    "padding":"10px"

                }

            )

        )





    # Creating heart rate chart
    chart = create_line_chart(

        time_history,

        heart_history

    )




    # Returning dashboard updates
    return (

        f"{heart} bpm",

        f"{oxygen} %",

        f"{temperature} °C",

        chart,

        alert_box,

        "🟢 Sensor Connected"

    )









# Processing risk assessment
@app.callback(

    Output(

        "risk-result",

        "children"

    ),



    Input(

        "risk-button",

        "n_clicks"

    ),



    [

        State(

            "age",

            "value"

        ),


        State(

            "risk-heart",

            "value"

        ),


        State(

            "risk-oxygen",

            "value"

        )

    ]

)



# Assessing patient risk
def assess_risk(

    clicks,

    age,

    heart,

    oxygen

):


    # Checking button click
    if not clicks:


        return ""




    # Creating risk request data
    payload = {


        "user_id":2,


        "age":age,


        "heart_rate":heart,


        "oxygen":oxygen,


        "blood_pressure":170,


        "bmi":32,


        "exercise":0,


        "blood_sugar":240,


        "cholesterol":260,


        "diabetes":1,


        "smoking":1


    }





    try:


        # Sending risk assessment request
        response=requests.post(

            f"{API_URL}/api/risk-assessment",

            json=payload

        )



        # Reading risk response
        result=response.json()



        # Returning risk information
        return html.Div(


            [

                html.H4(

                    "Risk Result"

                ),



                html.P(

                    f"Risk Score: {result.get('risk_score')}"

                ),



                html.P(

                    f"Risk Level: {result.get('risk_level')}"

                ),



                html.P(

                    f"Prediction: {result.get('prediction')}"

                ),



                html.H5(

                    "Recommendations"

                ),



                html.Ul(

                    [

                        html.Li(x)

                        for x in result.get(

                            "recommendations",

                            []

                        )

                    ]

                )

            ]

        )



    except Exception as e:


        # Returning error message
        return str(e)








# Running dashboard application
if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=8050,

        debug=False

    )