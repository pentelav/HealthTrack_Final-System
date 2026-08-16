# Set up application parameters such as database connection, system information, alert limits, risk model directory, or cache time as well as security values. 
# Set up configuration constants for HealthTrack application using environment loading and variable assignments.

import os

from dotenv import load_dotenv



# Loading environment settings
load_dotenv()



# Configuring database connection
DATABASE_URL = os.getenv(

    "DATABASE_URL",

    "mysql+pymysql://root:MySQL%4012%24@localhost/HealthTrackDB"

)



# Defining application name
APP_NAME = "HealthTrack Healthcare System"


# Defining application version
VERSION = "2.0.0"



# Defining heart rate limit
HEART_RATE_LIMIT = 120


# Defining oxygen level limit
OXYGEN_LIMIT = 90


# Defining temperature limit
TEMPERATURE_LIMIT = 38.5



# Defining risk model location
RISK_MODEL_PATH = (

    "../risk-assessment/risk_model.pkl"

)



# Defining cache timeout value
CACHE_TIMEOUT = 60



# Defining secret key value
SECRET_KEY = "HealthTrackSecretKey2026"


# Defining authentication algorithm
ALGORITHM = "HS256"


# Defining token expiry time
ACCESS_TOKEN_EXPIRE_MINUTES = 60