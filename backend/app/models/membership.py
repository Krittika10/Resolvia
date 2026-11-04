from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Membership(Base):
    """Connects a user to an organisation."""

    __tablename__ = "memberships"

    __table_args__ = (
        UniqueConstraint(
            "organisation_id",
            "user_id",
            name="uq_organisation_user",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    organisation_id = Column(
        Integer,
        ForeignKey("organisations.id"),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    role = Column(
        String(30),
        nullable=False,
        default="member",
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    organisation = relationship(
        "Organisation",
        back_populates="memberships",
    )

    user = relationship(
    "User",
    back_populates="memberships",
    )
    