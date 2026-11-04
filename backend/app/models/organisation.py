
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Organisation(Base):
    """Represents an organisation using Resolvia."""

    __tablename__ = "organisations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    slug = Column(String(180), unique=True, nullable=False, index=True)

    logo_url = Column(String(500), nullable=True)

    created_by_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    creator = relationship("User")

    memberships = relationship(
        "Membership",
        back_populates="organisation",
        cascade="all, delete-orphan",
    )

    projects = relationship(
        "Project",
        back_populates="organisation",
        cascade="all, delete-orphan",
    )
    invitations = relationship(
    "Invitation",
    back_populates="organisation",
    )
   