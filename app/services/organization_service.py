from typing import List
from app.dtos.organization import OrganizationDTO


def get_organizations() -> List[OrganizationDTO]:
    """Return a small placeholder list of organizations."""
    return [OrganizationDTO(id=1, name="Default Org")]
