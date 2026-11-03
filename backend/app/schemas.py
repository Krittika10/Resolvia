
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal


# USER SCHEMAS

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(max_length=150)
    role: Literal["Tester", "Developer", "Manager"] = "Tester"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    model_config = ConfigDict(from_attributes=True)


# ISSUE SCHEMAS

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: Optional[str] = None

    priority: Literal["Low", "Medium", "High", "Critical"] = "Medium"

    status: Literal["Open", "In Progress", "Resolved", "Closed"] = "Open"

    reporter_id: int
    assigned_to_id: Optional[int] = None


class IssueResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str
    reporter_id: int
    assigned_to_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=200)
    description: Optional[str] = None

    priority: Optional[
        Literal["Low", "Medium", "High", "Critical"]
    ] = None

    status: Optional[
        Literal["Open", "In Progress", "Resolved", "Closed"]
    ] = None

    assigned_to_id: Optional[int] = None
