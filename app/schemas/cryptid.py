from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CryptidBase(BaseModel):
    name: str
    classification: Optional[str] = None
    description: Optional[str] = None
    rarity: Optional[str] = None
    habitat: Optional[str] = None
    image_url: Optional[str] = None
    last_seen_at: Optional[datetime] = None


class CryptidCreate(CryptidBase):
    pass


class CryptidUpdate(BaseModel):
    name: Optional[str] = None
    classification: Optional[str] = None
    description: Optional[str] = None
    rarity: Optional[str] = None
    habitat: Optional[str] = None
    image_url: Optional[str] = None
    last_seen_at: Optional[datetime] = None


class CryptidOut(CryptidBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
