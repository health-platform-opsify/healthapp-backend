from fastapi import APIRouter
from typing import List

from app.dtos.organization import OrganizationDTO
from app.services.organization_service import get_organizations

router = APIRouter()

@router.get("/organizations", response_model=List[OrganizationDTO])
def list_organizations():
    """Placeholder endpoint for organizations."""
    return get_organizations()
