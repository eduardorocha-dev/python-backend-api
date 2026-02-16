from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Cryptid(Base):
    __tablename__ = "cryptids"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True, nullable=False)
    classification = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    rarity = Column(String(50), nullable=True)
    last_seen_location = Column(String(200), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sightings = relationship("Sighting", back_populates="cryptid", cascade="all, delete-orphan")
    creator = relationship("User", back_populates="cryptids")
