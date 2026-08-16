# Developed a Plotly chart component to plot heart rate trends from time and value data.
# Handled create_line_chart function to build chart figures with trend lines and axis details.

import plotly.graph_objects as go





# Creating line chart
def create_line_chart(

    times,

    values

):


    # Creating chart figure
    figure=go.Figure()



    # Adding heart rate data
    figure.add_trace(

        go.Scatter(

            x=times,

            y=values,

            mode="lines+markers",

            name="Heart Rate"

        )

    )



    # Updating chart details
    figure.update_layout(

        title="Heart Rate Trend",

        xaxis_title="Time",

        yaxis_title="BPM"

    )



    # Returning chart figure
    return figure