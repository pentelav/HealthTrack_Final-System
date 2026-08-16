# Produced patient risk reports and kept report information based on database records. 
# Created create_report and get_reports functions; used them to create new reports and to get user reports.

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.connection import get_database

from database.models import Report

from services.report_generator import generate_report



router=APIRouter()



# Creating report generation endpoint
@router.post("/reports/{user_id}")

def create_report(

    user_id:int,

    db:Session=Depends(get_database)

):

    # Generating patient report
    report_text = generate_report(

        user_id,

        db

    )


    # Creating report record
    report = Report(

        user_id=user_id,

        report_content=report_text

    )


    # Adding report record
    db.add(report)


    # Saving report details
    db.commit()



    # Returning generated report
    return {

        "message":

        "Report generated",

        "user_id":

        user_id,

        "report":

        report_text

    }



# Creating report retrieval endpoint
@router.get("/reports/{user_id}")

def get_reports(

    user_id:int,

    db:Session=Depends(get_database)

):

    # Fetching user reports
    reports=(

        db.query(Report)

        .filter(

            Report.user_id==user_id

        )

        .all()

    )


    # Returning report records
    return reports