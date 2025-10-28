from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.core.config import settings

class Organization(Base):
    __tablename__ = "organizations"
    __table_args__ = {"schema": settings.db_schema}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
