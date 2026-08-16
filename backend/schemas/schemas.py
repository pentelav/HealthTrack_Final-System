# Formulated Pydantic schemas to validate critical information, alerts, risk assessment information, and report responses. 
# Developed VitalCreate, AlertResponse, RiskRequest, RiskResponse, ReportResponse classes for handling API data.

from pydantic import BaseModel

from typing import Optional



# Creating vital input schema
class VitalCreate(BaseModel):

    # Defining user identifier
    user_id:int

    # Defining heart rate value
    heart_rate:int

    # Defining oxygen value
    oxygen:float

    # Defining temperature value
    temperature:float

    # Defining blood pressure value
    blood_pressure:Optional[str]=None



# Creating alert response schema
class AlertResponse(BaseModel):

    # Defining alert identifier
    id:int

    # Defining user identifier
    user_id:int

    # Defining alert severity
    severity:str

    # Defining alert message
    message:str

    # Defining alert status
    status:str



# Creating risk request schema
class RiskRequest(BaseModel):

    # Defining user identifier
    user_id: int

    # Defining age value
    age: int

    # Defining heart rate value
    heart_rate: int

    # Defining oxygen value
    oxygen: float

    # Defining blood pressure value
    blood_pressure: int

    # Defining BMI value
    bmi: float

    # Defining exercise value
    exercise: int

    # Defining blood sugar value
    blood_sugar: float = 0

    # Defining cholesterol value
    cholesterol: float = 0

    # Defining diabetes value
    diabetes: int = 0

    # Defining smoking value
    smoking: int = 0



# Creating prediction response schema
class RiskResponse(BaseModel):

    # Defining risk score
    score:float

    # Defining risk level
    level:str

    # Defining prediction result
    prediction:str



# Creating report response schema
class ReportResponse(BaseModel):

    # Defining user identifier
    user_id:int

    # Defining report content
    report:str