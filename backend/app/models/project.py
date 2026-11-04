from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Project(Base):
    """Represents a project within an organisation."""

    __tablename__ = "projects"

    __table_args__ = (
        UniqueConstraint(
            "organisation_id",
            "slug",
            name="uq_organisation_project_slug",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    organisation_id = Column(
        Integer,
        ForeignKey("organisations.id"),
        nullable=False,
    )

    name = Column(String(150), nullable=False)

    slug = Column(String(180), nullable=False)

    description = Column(Text, nullable=True)

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

    organisation = relationship(
        "Organisation",
        back_populates="projects",
    )

    creator = relationship("User")