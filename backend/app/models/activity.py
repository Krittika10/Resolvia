
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Activity(Base):
    """Records changes and events associated with an issue."""

    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)

    issue_id = Column(
        Integer,
        ForeignKey("issues.id"),
        nullable=False,
    )

    changed_by_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    action = Column(String(200), nullable=False)
    details = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    issue = relationship("Issue", back_populates="activities")
