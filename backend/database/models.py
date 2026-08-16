# Developed SQLAlchemy database models for users, health records, alerts, risk history, and reports and defined fields and relationships between them. 
# Developed classes for Defined User, HealthRecord, Alert, RiskHistory, and Report to handle healthcare data storage.

from sqlalchemy import (

    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Text

)

from sqlalchemy.orm import relationship

from datetime import datetime


from database.connection import Base



# Creating user table model
class User(Base):

    __tablename__ = "users"


    # Defining user identifier
    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    # Defining username field
    username = Column(

        String(100),

        unique=True,

        nullable=False

    )


    # Defining password field
    password = Column(

        String(255),

        nullable=False

    )


    # Defining user role field
    role = Column(

        String(50),

        default="Patient"

    )


    # Defining creation time field
    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    # Creating health record relation
    health_records = relationship(

        "HealthRecord",

        back_populates="user"

    )


    # Creating alert relation
    alerts = relationship(

        "Alert",

        back_populates="user"

    )



# Creating health record table model
class HealthRecord(Base):

    __tablename__ = "health_records"


    # Defining record identifier
    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    # Defining user reference
    user_id = Column(

        Integer,

        ForeignKey("users.id"),

        nullable=False

    )


    # Defining heart rate field
    heart_rate = Column(

        Integer

    )


    # Defining oxygen field
    oxygen = Column(

        Float

    )


    # Defining temperature field
    temperature = Column(

        Float

    )


    # Defining blood pressure field
    blood_pressure = Column(

        String(20)

    )


    # Defining creation time field
    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    # Creating user relation
    user = relationship(

        "User",

        back_populates="health_records"

    )



# Creating alert table model
class Alert(Base):

    __tablename__ = "alerts"


    # Defining alert identifier
    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    # Defining user reference
    user_id = Column(

        Integer,

        ForeignKey("users.id"),

        nullable=False

    )


    # Defining alert type field
    alert_type = Column(

        String(100)

    )


    # Defining alert severity field
    severity = Column(

        String(50)

    )


    # Defining alert message field
    message = Column(

        Text

    )


    # Defining alert status field
    status = Column(

        String(50),

        default="Unread"

    )


    # Defining creation time field
    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    # Creating user relation
    user = relationship(

        "User",

        back_populates="alerts"

    )



# Creating risk history table model
class RiskHistory(Base):

    __tablename__ = "risk_history"


    # Defining risk identifier
    id = Column(

        Integer,

        primary_key=True

    )


    # Defining user reference
    user_id = Column(

        Integer,

        ForeignKey("users.id")

    )


    # Defining risk score field
    risk_score = Column(

        Float

    )


    # Defining risk level field
    risk_level = Column(

        String(50)

    )


    # Defining prediction field
    prediction = Column(

        String(100)

    )


    # Defining creation time field
    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



# Creating report table model
class Report(Base):

    __tablename__ = "reports"


    # Defining report identifier
    id = Column(

        Integer,

        primary_key=True

    )


    # Defining user reference
    user_id = Column(

        Integer,

        ForeignKey("users.id")

    )


    # Defining report title field
    report_title = Column(

        String(200)

    )


    # Defining report content field
    report_content = Column(

        Text

    )


    # Defining creation time field
    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )