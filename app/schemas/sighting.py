from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint


class SightingBase(BaseModel):
    cryptid_id: int
    chaser_id: int
    location: str
    sighted_at: datetime
    confidence: Optional[conint(ge=1, le=5)] = None
    notes: Optional[str] = None


class SightingCreate(SightingBase):
    pass


class SightingUpdate(BaseModel):
    location: Optional[str] = None
    sighted_at: Optional[datetime] = None
    confidence: Optional[conint(ge=1, le=5)] = None
    notes: Optional[str] = None


class SightingOut(SightingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
