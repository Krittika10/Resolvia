
# Resolvia — Component Specification

Version: 1.0
Design direction: Engineering Control Room

## 1. Sidebar

Expanded width: 240px
Collapsed width: 68px

Sections:
- Workspace
- Management

Navigation:
- Overview
- Issue Queue
- My Assignments
- Activity Log
- Team
- Settings

Behaviour:
- Collapsible
- Active route indicator
- Icon tooltips when collapsed
- Keyboard accessible

## 2. Header

Height: 60px

Elements:
- Resolvia workspace identification
- Global search
- Create Issue action
- Theme selector
- User profile

## 3. Workload Summary

Display:
- Total Issues
- Open Issues
- In Progress
- Resolved

Rules:
- Values must come from GET /dashboard/stats
- Counts must not be hardcoded
- Use compact inline metrics rather than decorative cards

## 4. Issue Queue

Display:
- Issue ID
- Title
- Priority
- Status
- Reporter
- Assignee

Behaviour:
- Search
- Filter by status
- Filter by priority
- Open issue details on row selection
- Show a useful empty state

Priority values:
- Critical
- High
- Medium
- Low

Status values:
- Open
- In Progress
- Resolved
- Closed

## 5. Priority Indicators

Critical:
- Strong red semantic indicator

High:
- Orange semantic indicator

Medium:
- Amber semantic indicator

Low:
- Neutral grey indicator

Labels must always accompany colour indicators.

## 6. Status Indicators

Open:
- Neutral

In Progress:
- Signal Amber

Resolved:
- Green

Closed:
- Neutral

## 7. Resolution Trace

Display chronological activity records.

Each event contains:
- Action
- Details
- Responsible user, when available
- Timestamp

Use the existing Activity data model.

## 8. Activity Ledger

Display the latest activity across issues.

Each record contains:
- Issue identifier
- Activity description
- Responsible user
- Timestamp

Data must come from the backend.
A backend endpoint for global recent activity
is required before implementation.

## 9. Buttons

Primary:
- High-contrast action
- Used for Create Issue and Save

Secondary:
- Restrained surface
- Used for Cancel and alternative actions

Danger:
- Used for destructive operations

All buttons require:
- Hover state
- Focus state
- Disabled state
- Loading state when applicable

## 10. Forms and Inputs

Requirements:
- Consistent input heights
- Clear labels
- Validation messages
- Visible focus states
- Required-field indicators

## 11. Feedback Components

Toast notifications:
- Success
- Error
- Warning

Loading state:
- Clear progress indication

Empty state:
- Explain why no results are visible
- Provide a useful next action

## 12. General Rules

1. Avoid unnecessary decorative cards.
2. Keep table rows compact but readable.
3. Use consistent component spacing.
4. Provide keyboard accessibility.
5. Never communicate status using colour alone.
6. Ensure light and dark theme support.
7. Display real application data only.
