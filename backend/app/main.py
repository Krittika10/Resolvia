from sqlalchemy import func
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize application
app = FastAPI(
    title="Resolvia API",
    description="Issue Tracking and Resolution Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Resolvia!",
        "status": "Application is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Resolvia"
    }


# -------------------------
# USER APIs
# -------------------------

# Register a new user
@app.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check whether email already exists
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get all registered users
@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


# -------------------------
# ISSUE APIs
# -------------------------

# Create a new issue
@app.post("/issues", response_model=schemas.IssueResponse, status_code=201)
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):

    # Check whether reporter exists
    reporter = db.query(models.User).filter(
        models.User.id == issue.reporter_id
    ).first()

    if not reporter:
        raise HTTPException(
            status_code=404,
            detail="Reporter not found"
        )

    # Check whether assigned user exists
    if issue.assigned_to_id is not None:
        assignee = db.query(models.User).filter(
            models.User.id == issue.assigned_to_id
        ).first()

        if not assignee:
            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

    new_issue = models.Issue(**issue.model_dump())

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return new_issue


# Get all issues
@app.get("/issues", response_model=list[schemas.IssueResponse])
def get_issues(db: Session = Depends(get_db)):
    issues = db.query(models.Issue).all()
    return issues


# -------------------------
# UPDATE ISSUE API
# -------------------------

@app.patch("/issues/{issue_id}", response_model=schemas.IssueResponse)
def update_issue(
    issue_id: int,
    update_data: schemas.IssueUpdate,
    db: Session = Depends(get_db)
):
    # Find the issue
    issue = db.query(models.Issue).filter(
        models.Issue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    # Get only the fields submitted by the user
    changes = update_data.model_dump(exclude_unset=True)

    # Validate the assigned developer
    if "assigned_to_id" in changes and changes["assigned_to_id"] is not None:
        assignee = db.query(models.User).filter(
            models.User.id == changes["assigned_to_id"]
        ).first()

        if not assignee:
            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

    # Record changes in activity history
    for field, new_value in changes.items():
        old_value = getattr(issue, field)

        if old_value != new_value:
            activity = models.Activity(
                issue_id=issue.id,
                action=f"{field} updated",
                details=f"Changed from '{old_value}' to '{new_value}'"
            )

            db.add(activity)
            setattr(issue, field, new_value)

    db.commit()
    db.refresh(issue)

    return issue


# -------------------------
# ISSUE ACTIVITY API
# -------------------------

@app.get("/issues/{issue_id}/activities")
def get_issue_activities(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = db.query(models.Issue).filter(
        models.Issue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return db.query(models.Activity).filter(
        models.Activity.issue_id == issue_id
    ).order_by(models.Activity.created_at.desc()).all()


# -------------------------
# SEARCH AND FILTER ISSUES
# -------------------------

@app.get("/issues/search", response_model=list[schemas.IssueResponse])
def search_issues(
    q: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    assigned_to_id: Optional[int] = None,
    reporter_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Issue)

    # Search title and description
    if q:
        query = query.filter(
            (models.Issue.title.ilike(f"%{q}%")) |
            (models.Issue.description.ilike(f"%{q}%"))
        )

    # Filter by status
    if status:
        query = query.filter(models.Issue.status == status)

    # Filter by priority
    if priority:
        query = query.filter(models.Issue.priority == priority)

    # Filter by assigned developer
    if assigned_to_id is not None:
        query = query.filter(
            models.Issue.assigned_to_id == assigned_to_id
        )

    # Filter by reporter
    if reporter_id is not None:
        query = query.filter(
            models.Issue.reporter_id == reporter_id
        )

    return query.order_by(models.Issue.created_at.desc()).all()


# -------------------------
# DASHBOARD STATISTICS API
# -------------------------

@app.get("/dashboard/stats")
def dashboard_stats(db: Session = Depends(get_db)):

    total_issues = db.query(models.Issue).count()

    open_issues = db.query(models.Issue).filter(
        models.Issue.status == "Open"
    ).count()

    in_progress_issues = db.query(models.Issue).filter(
        models.Issue.status == "In Progress"
    ).count()

    resolved_issues = db.query(models.Issue).filter(
        models.Issue.status == "Resolved"
    ).count()

    closed_issues = db.query(models.Issue).filter(
        models.Issue.status == "Closed"
    ).count()

    critical_issues = db.query(models.Issue).filter(
        models.Issue.priority == "Critical"
    ).count()

    return {
        "total_issues": total_issues,
        "open_issues": open_issues,
        "in_progress_issues": in_progress_issues,
        "resolved_issues": resolved_issues,
        "closed_issues": closed_issues,
        "critical_issues": critical_issues
    }

#Individual issue statistics

@app.get("/issues/{issue_id}", response_model=schemas.IssueResponse)
def get_issue(issue_id: int, db: Session = Depends(get_db)):

    issue = db.query(models.Issue).filter(
        models.Issue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return issue