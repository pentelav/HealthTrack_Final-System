# Incorporated risk assessment API with risk scoring, machine learning prediction, factor detection, recommendations and history storage.
# Processes patient risk details in handled assess_risk and risk_history functions to retrieve patient risk history.


from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from database.connection import get_database

from database.models import RiskHistory


from schemas.schemas import RiskRequest


from services.risk_engine import calculate_risk

from services.prediction import predict_risk


from risk_assessment.recommendations import get_recommendations


# Creating API router
router = APIRouter()





# Creating risk assessment endpoint
@router.post("/risk-assessment")

def assess_risk(

    request: RiskRequest,

    db: Session = Depends(get_database)

):


    try:


        # Converting request data
        data = request.dict()



        # Calculating risk score
        risk_result = calculate_risk(

            data

        )



        # Predicting risk status
        prediction = predict_risk(

            data

        )





        # Creating risk factor list
        factors = []



        # Checking blood pressure factor
        if request.blood_pressure >= 140:


            factors.append(

                "High Blood Pressure"

            )



        # Checking blood sugar factor
        if request.blood_sugar >= 200:


            factors.append(

                "High Blood Sugar"

            )



        # Checking smoking factor
        if request.smoking == 1:


            factors.append(

                "Smoking History"

            )



        # Checking BMI factor
        if request.bmi >= 30:


            factors.append(

                "High BMI"

            )



        # Checking oxygen factor
        if request.oxygen < 90:


            factors.append(

                "Low Oxygen Level"

            )



        # Checking age factor
        if request.age >= 60:


            factors.append(

                "Advanced Age"

            )





        # Generating recommendations
        recommendations = get_recommendations(

            factors

        )







        # Creating risk history record
        history = RiskHistory(

            user_id=request.user_id,

            risk_score=risk_result["risk_score"],

            risk_level=risk_result["risk_level"],

            prediction=prediction

        )



        # Adding history record
        db.add(history)


        # Saving history record
        db.commit()


        # Refreshing saved record
        db.refresh(history)





        # Returning risk details
        return {


            "message":

            "Risk assessment completed",



            "user_id":

            request.user_id,



            "risk_score":

            risk_result["risk_score"],



            "risk_level":

            risk_result["risk_level"],



            "prediction":

            prediction,



            "risk_factors":

            factors,



            "recommendations":

            recommendations,



            "record_id":

            history.id


        }




    except Exception as error:


        # Reverting database changes
        db.rollback()



        # Returning server error
        raise HTTPException(

            status_code=500,

            detail=str(error)

        )









# Creating risk history endpoint
@router.get("/risk-history/{user_id}")

def risk_history(

    user_id: int,

    db: Session = Depends(get_database)

):


    # Fetching risk history records
    records = (

        db.query(RiskHistory)

        .filter(

            RiskHistory.user_id == user_id

        )

        .order_by(

            RiskHistory.created_at.desc()

        )

        .all()

    )


    # Returning risk history records
    return records