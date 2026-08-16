# Retreieved, acknowledged and addressed healthcare alerts via database records and managed alert operations. 
# Alert management tasks for handled, get_alerts, get_user_alerts, acknowledge_alert, and resolve_alert functions.

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.connection import get_database

from database.models import Alert



router = APIRouter()



# Creating alert retrieval endpoint
@router.get("/alerts")

def get_alerts(

    db:Session=Depends(get_database)

):

    # Fetching all alert records
    alerts = (

        db.query(Alert)

        .order_by(

            Alert.created_at.desc()

        )

        .all()

    )


    # Returning alert records
    return alerts



# Creating user alert retrieval endpoint
@router.get("/alerts/{user_id}")

def get_user_alerts(

    user_id:int,

    db:Session=Depends(get_database)

):

    # Fetching user alert records
    alerts = (

        db.query(Alert)

        .filter(

            Alert.user_id==user_id

        )

        .all()

    )


    # Returning user alerts
    return alerts



# Creating alert acknowledgement endpoint
@router.put("/alerts/{alert_id}/ack")

def acknowledge_alert(

    alert_id:int,

    user:str="admin",

    db:Session=Depends(get_database)

):

    # Finding alert record
    alert = (

        db.query(Alert)

        .filter(

            Alert.id==alert_id

        )

        .first()

    )


    # Checking alert availability
    if not alert:

        return {

            "error":

            "Alert not found"

        }



    # Updating alert acknowledgement status
    alert.status="ACKNOWLEDGED"

    alert.acknowledged_by=user


    # Saving alert changes
    db.commit()



    # Returning acknowledgement response
    return {

        "message":

        "Alert acknowledged",

        "alert_id":

        alert_id

    }



# Creating alert resolution endpoint
@router.put("/alerts/{alert_id}/resolve")

def resolve_alert(

    alert_id:int,

    db:Session=Depends(get_database)

):

    # Finding alert record
    alert=(

        db.query(Alert)

        .filter(

            Alert.id==alert_id

        )

        .first()

    )


    # Checking alert availability
    if not alert:

        return {

            "error":

            "Alert not found"

        }



    # Updating alert resolution status
    alert.status="RESOLVED"


    # Saving resolution changes
    db.commit()



    # Returning resolution response
    return {

        "message":

        "Alert resolved"

    }