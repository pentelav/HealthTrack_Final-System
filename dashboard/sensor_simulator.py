# Health values of simulated patients are continuously updated with pre-specified health parameters via monitoring data.
# Call update_data function periodically to send sensor readings and update stored physiological values.

import time

from websocket_client import update_data

# Running sensor data simulation
while True:


    # Creating sensor values
    sensor_data = {


        # Adding heart rate value
        "heart_rate":145,


        # Adding oxygen value
        "oxygen":85,


        # Adding temperature value
        "temperature":39.5


    }


    # Updating sensor values
    update_data(sensor_data)


    # Displaying updated sensor data
    print(

        "Sensor Updated:",

        sensor_data

    )


    # Waiting before next update
    time.sleep(5)