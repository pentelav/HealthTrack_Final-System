# Designed dashboard vital cards with reusable piece of card components to show healthcare information.
# Used create_card function to create cards with dynamic display features.

import dash_bootstrap_components as dbc

from dash import html





# Creating dashboard card
def create_card(title,component_id):


    # Returning card component
    return dbc.Card(

        [

            # Adding card title
            dbc.CardHeader(

                title

            ),


            # Adding card content
            dbc.CardBody(

                html.H2(

                    id=component_id

                )

            )

        ],


        # Adding card spacing
        className="mb-3"

    )