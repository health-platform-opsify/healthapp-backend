from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    dob: Optional[str] = None
    nhs_number: Optional[str] = None
    gender: Optional[str] = None
    ethnicity: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    vitals: Optional[Dict[str, Any]] = None
    lab_results: Optional[Dict[str, Any]] = None
    comorbidities: Optional[List[str]] = None
    medications: Optional[List[str]] = None
    prior_admissions: Optional[int] = None
    socioeconomic_status: Optional[str] = None
    last_visit: Optional[str] = None
    imaging: Optional[Dict[str, Any]] = None
    risk_scores: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None


class PatientDTO(PatientCreate):
    id: str

    class Config:
        orm_mode = True
