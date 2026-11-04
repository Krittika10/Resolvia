import sys
from pathlib import Path

backend_dir = str(Path(__file__).resolve().parents[1])
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from sqlalchemy.orm import configure_mappers

from app import models
from app.database import Base


def test_all_model_tables_are_registered():
    """Verify all eight database tables are registered."""

    expected_tables = {
        "users",
        "issues",
        "activities",
        "organisations",
        "memberships",
        "projects",
        "project_members",
        "invitations",
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
    assert hasattr(models.Project, "project_members")
    assert hasattr(models.Project, "issues")
    assert hasattr(models.ProjectMember, "project")
    assert hasattr(models.ProjectMember, "user")
    assert hasattr(models.Issue, "project")
    assert hasattr(models.Project, "issues")

    assert hasattr(models.Invitation, "organisation")
    assert hasattr(models.Invitation, "project")
    assert hasattr(models.Invitation, "inviter")
    assert hasattr(models.Organisation, "invitations")
    assert hasattr(models.User, "memberships")
    assert hasattr(models.User, "project_memberships")

def test_sqlalchemy_can_configure_all_relationships():
    """Verify SQLAlchemy can resolve all model relationships."""

    configure_mappers()
    assert all(mapper.configured for mapper in Base.registry.mappers)


def test_invitation_model_fields_exist():
    """Verify important invitation fields exist."""

    assert hasattr(models.Invitation, "email")
    assert hasattr(models.Invitation, "token_hash")
    assert hasattr(models.Invitation, "expires_at")
    assert hasattr(models.Invitation, "accepted_at")
    assert hasattr(models.Invitation, "revoked_at")