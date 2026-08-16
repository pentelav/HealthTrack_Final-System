# Constructed HealthTrack FastAPI application, including vital, alert, risk, and report modules and initialised database. 
# Carried out home and health duties to provide information about applications and service status.

from fastapi import FastAPI

from api import (
    vitals,
    alerts,
    risk,
    reports
)

from database.connection import create_database



# Creating database tables
create_database()



# Creating FastAPI application
app = FastAPI(

    title="HealthTrack Healthcare Monitoring System",

    description=
    """
    Complete healthcare monitoring,
    alert management,
    risk assessment,
    and reporting platform.
    """,

    version="2.0.0"

)



# Registering vital monitoring module
app.include_router(

    vitals.router,

    prefix="/api",

    tags=["Vital Monitoring"]

)



# Registering alert management module
app.include_router(

    alerts.router,

    prefix="/api",

    tags=["Alert Management"]

)



# Registering risk assessment module
app.include_router(

    risk.router,

    prefix="/api",

    tags=["Risk Assessment"]

)



# Registering reporting module
app.include_router(

    reports.router,

    prefix="/api",

    tags=["Reports"]

)



# Creating home endpoint
@app.get("/")

def home():

    # Returning application information
    return {

        "application":
        "HealthTrack Final System",

        "status":
        "running",

        "version":
        "2.0.0",

        "modules":
        [

            "Vitals",

            "Alerts",

            "Risk Assessment",

            "Reporting"

        ]

    }



# Creating health check endpoint
@app.get("/health")

def health():

    # Returning service status
    return {

        "service":
        "HealthTrack API",

        "status":
        "healthy"

    }