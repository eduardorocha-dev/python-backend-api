from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class Sighting(Base):
    __tablename__ = "sightings"
    __table_args__ = (
        CheckConstraint("confidence >= 1 AND confidence <= 5", name="ck_sightings_confidence"),
    )

    id = Column(Integer, primary_key=True, index=True)
    cryptid_id = Column(Integer, ForeignKey("cryptids.id"), nullable=False, index=True)
    chaser_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    location = Column(String(255), nullable=False)
    sighted_at = Column(DateTime(timezone=True), nullable=False)
    confidence = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    cryptid = relationship("Cryptid", back_populates="sightings")
    chaser = relationship("User", back_populates="sightings")
