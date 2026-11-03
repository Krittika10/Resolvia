# Resolvia — Dashboard Specification

Version: 1.0
Design direction: Engineering Control Room

## 1. Application Shell

The application has three primary regions:

- Top header
- Collapsible left sidebar
- Main operational workspace

On wider screens, the workspace can have a secondary
activity panel on the right.

## 2. Top Header

Left:
- Resolvia brand identity
- Workspace identification

Right:
- Global issue search
- Create issue action
- Theme selector
- User profile area

## 3. Sidebar Navigation

WORKSPACE
- Overview
- Issue Queue
- My Assignments
- Activity Log

MANAGEMENT
- Team
- Settings

The sidebar must be collapsible.

## 4. Main Dashboard

Page heading:
- Issue Control
- Short workspace description

Workload summary:
- Total Issues
- Open Issues
- In Progress
- Resolved

Priority Queue:
- Critical and high-priority issues
- Issue identifier
- Issue title
- Priority
- Status
- Assignee

Latest Activity:
- Issue identifier
- Activity description
- Person responsible
- Timestamp

## 5. Right Activity Panel

On wide screens, display recent issue activity
alongside the main workspace.

On smaller screens, move this section below
the primary dashboard content.

## 6. Visual Language

- Technical operations-room aesthetic
- Inter typography
- Monospace technical metadata
- Precise alignment
- Thin separators and structured grids
- Restrained signal-colour accents
- Light and dark themes

## 7. Data Integrity

All dashboard values must come from the backend.

Never use fabricated issue counts or fake activity.

## 8. Responsive Behaviour

Desktop:
- Collapsible sidebar
- Main workspace
- Secondary activity panel

Tablet:
- Collapsible sidebar
- Main workspace
- Activity below primary content

Mobile:
- Compact navigation
- Single-column content
- Horizontally scrollable issue tables where needed