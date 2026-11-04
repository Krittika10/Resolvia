
from app import models
from app.database import Base


def test_existing_tables_are_registered():
    """Verify all existing database models are registered."""

    expected_tables = {"users", "issues", "activities"}

    assert expected_tables.issubset(Base.metadata.tables.keys())


def test_model_relationships_exist():
    """Verify relationships between existing models."""

    assert hasattr(models.User, "reported_issues")
    assert hasattr(models.User, "assigned_issues")

    assert hasattr(models.Issue, "reporter")
    assert hasattr(models.Issue, "assignee")
    assert hasattr(models.Issue, "activities")

    assert hasattr(models.Activity, "issue")
