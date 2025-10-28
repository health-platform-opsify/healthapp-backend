from typing import List, Optional
from app.dtos.patient import PatientCreate, PatientDTO

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# In-memory fallback to preserve existing behavior for tests / environments
_PATIENTS: List[PatientDTO] = [
    PatientDTO(id="1", name="Alice Smith", dob="1988-01-20", nhs_number="1111111111"),
    PatientDTO(id="2", name="Bob Jones", dob="1977-05-12", nhs_number="2222222222"),
]


async def list_patients(db: Optional[AsyncSession] = None, q: Optional[str] = None) -> List[PatientDTO]:
    """List patients. If an AsyncSession is provided, query the DB; otherwise use in-memory list."""
    if db is None:
        if not q:
            return _PATIENTS
        ql = q.lower()
        return [p for p in _PATIENTS if ql in p.name.lower() or (p.nhs_number and q in p.nhs_number)]

    # DB-backed path
    try:
        from app.models.patient import Patient as PatientModel
    except Exception:
        # fallback if model can't be imported
        return await list_patients(None, q)

    stmt = select(PatientModel)
    if q:
        like_q = f"%{q}%"
        stmt = stmt.where(
            (PatientModel.name.ilike(like_q)) | (PatientModel.nhs_number.ilike(like_q))
        )

    res = await db.execute(stmt)
    rows = res.scalars().all()
    return [PatientDTO.from_orm(r) for r in rows]


async def create_patient(db: Optional[AsyncSession], payload: PatientCreate) -> PatientDTO:
    """Create a patient using DB if session provided else in-memory fallback."""
    if db is None:
        new_id = str(len(_PATIENTS) + 1)
        dto = PatientDTO(id=new_id, **payload.dict())
        _PATIENTS.append(dto)
        return dto

    try:
        from app.models.patient import Patient as PatientModel
    except Exception:
        return await create_patient(None, payload)

    obj = PatientModel(**payload.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return PatientDTO.from_orm(obj)
