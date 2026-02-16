from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SightingBase(BaseModel):
    cryptid_id: int
    user_id: int
    location: str
    date: datetime
    notes: Optional[str] = None


class SightingCreate(SightingBase):
    pass


class SightingUpdate(BaseModel):
    location: Optional[str] = None
    date: Optional[datetime] = None
    notes: Optional[str] = None


class SightingOut(SightingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
