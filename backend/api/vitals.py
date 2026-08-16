# Analysed patient vital information, patient health records and issued alerts for abnormal conditions. 
# The receive_vitals and get_user_vitals functions are used to save important data and get health information of a user.

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from database.connection import get_database

from database.models import HealthRecord


from schemas.schemas import VitalCreate


from services.alert_engine import generate_alerts



router = APIRouter()



# Creating vital information endpoint
@router.post("/vitals")
def receive_vitals(

    vital: VitalCreate,

    db: Session = Depends(get_database)

):


    # Creating health record
    record = HealthRecord(

        user_id=vital.user_id,

        heart_rate=vital.heart_rate,

        oxygen=vital.oxygen,

        temperature=vital.temperature,

        blood_pressure=vital.blood_pressure

    )


    # Adding health record
    db.add(record)


    # Saving health record
    db.commit()


    # Refreshing health record
    db.refresh(record)



    # Generating health alerts
    alerts = generate_alerts(

        vital.dict()

    )


    # Returning vital response
    return {

        "message":
        "Vital information received",

        "record_id":
        record.id,

        "alerts":
        alerts

    }



# Creating user vital retrieval endpoint
@router.get("/vitals/{user_id}")

def get_user_vitals(

    user_id:int,

    db:Session=Depends(get_database)

):


    # Fetching user health records
    records = (

        db.query(HealthRecord)

        .filter(

            HealthRecord.user_id==user_id

        )

        .all()

    )


    # Returning health records
    return records