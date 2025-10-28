from pydantic import BaseModel

class OrganizationDTO(BaseModel):
    id: int
    name: str
