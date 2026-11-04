
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Issue(Base):
    """Represents an issue within a project."""

    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    priority = Column(String(20), default="Medium")
    status = Column(String(30), default="Open")

    reporter_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    assigned_to_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )
    project_id = Column(
    Integer,
    ForeignKey("projects.id"),
    nullable=True,
)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    reporter = relationship(
        "User",
        foreign_keys=[reporter_id],
        back_populates="reported_issues",
    )

    assignee = relationship(
        "User",
        foreign_keys=[assigned_to_id],
        back_populates="assigned_issues",
    )

    activities = relationship(
        "Activity",
        back_populates="issue",
        cascade="all, delete-orphan",
    )
    project = relationship(
    "Project",
    back_populates="issues",
)
