from sqlalchemy.orm import configure_mappers

from app import models
from app.database import Base


def test_all_model_tables_are_registered():
    """Verify all seven database models are registered."""

    expected_tables = {
        "users",
        "issues",
        "activities",
        "organisations",
        "memberships",
        "projects",
        "project_members",
    }

    assert expected_tables.issubset(Base.metadata.tables.keys())


def test_model_relationships_exist():
    """Verify relationships between existing models."""

    assert hasattr(models.User, "reported_issues")
    assert hasattr(models.User, "assigned_issues")

    assert hasattr(models.Issue, "reporter")
    assert hasattr(models.Issue, "assignee")
    assert hasattr(models.Issue, "activities")

    assert hasattr(models.Activity, "issue")

    assert hasattr(models.Organisation, "memberships")
    assert hasattr(models.Organisation, "projects")

    assert hasattr(models.Membership, "organisation")
    assert hasattr(models.Membership, "user")

    assert hasattr(models.Project, "organisation")

    assert hasattr(models.ProjectMember, "project")
    assert hasattr(models.ProjectMember, "user")


def test_sqlalchemy_can_configure_all_relationships():
    """Verify SQLAlchemy can resolve all model relationships."""

    configure_mappers()