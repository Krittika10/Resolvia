
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


# USER TABLE
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    role = Column(String(50), default="Tester")

    # Issues reported by this user
    reported_issues = relationship(
        "Issue",
        foreign_keys="Issue.reporter_id",
        back_populates="reporter"
    )

    # Issues assigned to this user
    assigned_issues = relationship(
        "Issue",
        foreign_keys="Issue.assigned_to_id",
        back_populates="assignee"
    )


# ISSUE TABLE
class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    priority = Column(String(20), default="Medium")
    status = Column(String(30), default="Open")

    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    reporter = relationship(
        "User",
        foreign_keys=[reporter_id],
        back_populates="reported_issues"
    )

    assignee = relationship(
        "User",
        foreign_keys=[assigned_to_id],
        back_populates="assigned_issues"
    )

    activities = relationship(
        "Activity",
        back_populates="issue",
        cascade="all, delete-orphan"
    )


# ACTIVITY TABLE
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("issues.id"), nullable=False)
    changed_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    action = Column(String(200), nullable=False)
    details = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    issue = relationship("Issue", back_populates="activities")
