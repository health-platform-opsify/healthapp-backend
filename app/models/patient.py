from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from app.db.database import Base
from app.core.config import settings


class Patient(Base):
    __tablename__ = "patients"
    __table_args__ = {"schema": settings.db_schema}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dob = Column(String, nullable=True)
    nhs_number = Column(String, nullable=True, index=True)
    gender = Column(String, nullable=True)
    ethnicity = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    vitals = Column(JSON, nullable=True)
    lab_results = Column(JSON, nullable=True)
    comorbidities = Column(JSON, nullable=True)
    medications = Column(JSON, nullable=True)
    prior_admissions = Column(Integer, nullable=True)
    socioeconomic_status = Column(String, nullable=True)
    last_visit = Column(String, nullable=True)
    imaging = Column(JSON, nullable=True)
    risk_scores = Column(JSON, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
