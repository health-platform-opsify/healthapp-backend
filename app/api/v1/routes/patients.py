from fastapi import APIRouter, Query, Body, HTTPException, Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.patient import PatientCreate, PatientDTO
from app.services.patient_service import list_patients, create_patient
from app.dependencies.db import get_db

router = APIRouter()


@router.get("/patients", response_model=List[PatientDTO])
async def get_patients(q: str = Query(None, description="Search query for name or NHS number"), db: AsyncSession = Depends(get_db)):
    return await list_patients(db, q)


@router.post("/patients", response_model=PatientDTO, status_code=201)
async def post_patient(payload: PatientCreate = Body(...), db: AsyncSession = Depends(get_db)):
    # basic validation example
    if not payload.name:
        raise HTTPException(status_code=422, detail="name is required")
    created = await create_patient(db, payload)
    return created
