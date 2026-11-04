
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    """Represents a registered Resolvia user."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    role = Column(String(50), default="Tester")

    reported_issues = relationship(
        "Issue",
        foreign_keys="Issue.reporter_id",
        back_populates="reporter",
    )

    assigned_issues = relationship(
        "Issue",
        foreign_keys="Issue.assigned_to_id",
        back_populates="assignee",
    )
