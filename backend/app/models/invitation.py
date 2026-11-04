from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Invitation(Base):
    """Stores invitations to join a workspace or project."""

    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(150), nullable=False, index=True)

    # Store a hashed invitation token, never the raw token.
    token_hash = Column(String(64), unique=True, nullable=False)

    organisation_id = Column(
        Integer,
        ForeignKey("organisations.id"),
        nullable=False,
    )

    # Null means this is a workspace-level invitation.
    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=True,
    )

    invited_by_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    # Used only for project-specific invitations.
    project_role = Column(
        String(30),
        nullable=True,
    )

    expires_at = Column(DateTime(timezone=True), nullable=False)

    accepted_at = Column(DateTime(timezone=True), nullable=True)

    revoked_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    organisation = relationship(
    "Organisation",
    back_populates="invitations",
    )

    project = relationship("Project")

    inviter = relationship(
        "User",
        foreign_keys=[invited_by_id],
    )
