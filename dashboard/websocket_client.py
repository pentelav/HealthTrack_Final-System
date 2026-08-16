# Patient physiological data stored most up to date and sensor data updates managed from monitoring simulator.
# Implements update_data and get_latest_data functions for updating and fetching current health values.

# Creating latest sensor data storage
latest_data = {

    "heart_rate": 145,

    "oxygen": 85,

    "temperature": 39.5

}



# Updating sensor values
def update_data(data):


    # Accessing latest data storage
    global latest_data


    # Updating sensor values
    latest_data = {


        # Updating heart rate value
        "heart_rate": data.get(

            "heart_rate",

            0

        ),


        # Updating oxygen value
        "oxygen": data.get(

            "oxygen",

            0

        ),


        # Updating temperature value
        "temperature": data.get(

            "temperature",

            0

        )

    }

# Retrieving latest sensor values
def get_latest_data():


    # Returning current sensor data
    return latest_data  