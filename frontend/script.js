const API_BASE_URL = "http://127.0.0.1:8000";

// Fetch dashboard statistics
async function loadDashboardStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/dashboard/stats`);

        if (!response.ok) {
            throw new Error("Could not fetch dashboard statistics");
        }

        const stats = await response.json();

        // Display statistics on the dashboard
        document.getElementById("total-issues").textContent =
            stats.total_issues;

        document.getElementById("open-issues").textContent =
            stats.open_issues;

        document.getElementById("progress-issues").textContent =
            stats.in_progress_issues;

        document.getElementById("resolved-issues").textContent =
            stats.resolved_issues;

        console.log("Dashboard statistics loaded:", stats);

    } catch (error) {
        console.error("Error loading dashboard statistics:", error);
    }
}

// Load dashboard data when the page opens
loadDashboardStats();

// Fetch and display issues
async function loadIssues() {
    const tableBody = document.getElementById("issue-table-body");

    try {
        const response = await fetch(`${API_BASE_URL}/issues`);

        if (!response.ok) {
            throw new Error("Could not fetch issues");
        }

        const issues = await response.json();

        // Clear the loading message
        tableBody.replaceChildren();

        if (issues.length === 0) {
            const row = document.createElement("tr");
            const cell = document.createElement("td");

            cell.colSpan = 4;
            cell.textContent = "No issues found.";

            row.appendChild(cell);
            tableBody.appendChild(row);
            return;
        }

        issues.forEach(issue => {
            const row = document.createElement("tr");
            row.classList.add("clickable-row");
            row.title = "Click to view issue details";

            row.addEventListener("click", () => {
             openIssueDetails(issue.id);
  });
            const issueCell = document.createElement("td");
            issueCell.textContent = `${issue.id}. ${issue.title}`;

            const priorityCell = document.createElement("td");
            priorityCell.textContent = issue.priority;

            const statusCell = document.createElement("td");
            statusCell.textContent = issue.status;

            const assigneeCell = document.createElement("td");
            assigneeCell.textContent = issue.assigned_to_id
                ? `User #${issue.assigned_to_id}`
                : "Unassigned";

            row.append(
                issueCell,
                priorityCell,
                statusCell,
                assigneeCell
            );

            tableBody.appendChild(row);
        });

        console.log("Issues loaded successfully:", issues);

    } catch (error) {
        console.error("Error loading issues:", error);

        tableBody.textContent = "Unable to load issues.";
    }
}

// Load issues when the page opens
loadIssues();

// Fetch and display recent activity
async function loadRecentActivity() {
    const activityContainer = document.getElementById("recent-activity");

    try {
        const response = await fetch(`${API_BASE_URL}/activities/recent`);

        if (!response.ok) {
            throw new Error("Could not fetch recent activity");
        }

        const activities = await response.json();

        activityContainer.replaceChildren();

        if (activities.length === 0) {
            activityContainer.textContent = "No recent activity.";
            return;
        }

        activities.forEach(activity => {
            const item = document.createElement("div");
            item.className = "activity-item";

            const marker = document.createElement("span");
            marker.className = "activity-marker";
            marker.textContent = "●";

            const content = document.createElement("div");
            content.className = "activity-content";

            const title = document.createElement("strong");
            title.textContent = activity.issue_title;

            const description = document.createElement("p");
            description.textContent =
                `${activity.action}: ${activity.details || "No details available"}`;

            const metadata = document.createElement("span");
            metadata.className = "activity-meta";

            const actor = activity.changed_by || "System";
            const date = new Date(activity.created_at);

            metadata.textContent =
                `${actor} · ${date.toLocaleString()}`;

            content.append(title, description, metadata);
            item.append(marker, content);

            activityContainer.appendChild(item);
        });

        console.log("Recent activity loaded:", activities);

    } catch (error) {
        console.error("Error loading recent activity:", error);
        activityContainer.textContent = "Unable to load recent activity.";
    }
}

// Load activity when the page opens
loadRecentActivity();

// Sidebar collapse and expand
const sidebarToggle = document.getElementById("sidebar-toggle");
const appShell = document.querySelector(".app-shell");

sidebarToggle.addEventListener("click", () => {
    const isCollapsed = appShell.classList.toggle("sidebar-collapsed");

    sidebarToggle.setAttribute("aria-expanded", String(!isCollapsed));
    sidebarToggle.setAttribute(
        "aria-label",
        isCollapsed ? "Expand sidebar" : "Collapse sidebar"
    );
});
// Render Lucide icons
lucide.createIcons();

// CREATE ISSUE MODAL

const issueModal = document.getElementById("issue-modal");
const createIssueBtn = document.getElementById("create-issue-btn");
const closeIssueBtn = document.getElementById("close-issue-modal");
const cancelIssueBtn = document.getElementById("cancel-issue");

function openIssueModal() {
    issueModal.hidden = false;
    document.getElementById("issue-title").focus();
}

function closeIssueModal() {
    issueModal.hidden = true;
}

createIssueBtn.addEventListener("click", openIssueModal);

closeIssueBtn.addEventListener("click", closeIssueModal);

cancelIssueBtn.addEventListener("click", closeIssueModal);

// Close when clicking outside the modal
issueModal.addEventListener("click", (event) => {
    if (event.target === issueModal) {
        closeIssueModal();
    }
});

// Close using Escape key
document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !issueModal.hidden) {
        closeIssueModal();
    }
});
// LOAD USERS INTO CREATE ISSUE FORM
let teamMembers = [];
async function loadUsersIntoForm() {
    try {
        const response = await fetch(`${API_BASE_URL}/users`);

        if (!response.ok) {
            throw new Error("Could not load users");
        }

        const users = await response.json();
        teamMembers = users;
        const reporterSelect = document.getElementById("issue-reporter");
        const assigneeSelect = document.getElementById("issue-assignee");

        users.forEach(user => {
            const reporterOption = document.createElement("option");
            reporterOption.value = user.id;
            reporterOption.textContent = user.name;
            reporterSelect.appendChild(reporterOption);

            const assigneeOption = document.createElement("option");
            assigneeOption.value = user.id;
            assigneeOption.textContent = user.name;
            assigneeSelect.appendChild(assigneeOption);
        });

    } catch (error) {
        console.error("Error loading users:", error);
    }
}

loadUsersIntoForm();
// CREATE ISSUE — SUBMIT FORM
const createIssueForm = document.getElementById("create-issue-form");

createIssueForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const issueData = {
        title: document.getElementById("issue-title").value.trim(),
        description: document.getElementById("issue-description").value.trim(),
        priority: document.getElementById("issue-priority").value,
        reporter_id: Number(document.getElementById("issue-reporter").value),
        assigned_to_id: document.getElementById("issue-assignee").value
            ? Number(document.getElementById("issue-assignee").value)
            : null
    };

    try {
        const response = await fetch(`${API_BASE_URL}/issues`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(issueData)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Could not create issue");
        }

        alert("Issue created successfully!");

        createIssueForm.reset();
        closeIssueModal();

        loadIssues();
        loadDashboardStats();
        loadRecentActivity();

    } catch (error) {
        console.error("Error creating issue:", error);
        alert(error.message);
    }
});

// OPEN ISSUE DETAILS PANEL
async function openIssueDetails(issueId) {
    try {
        const response = await fetch(`${API_BASE_URL}/issues/${issueId}`);

        if (!response.ok) {
            throw new Error("Could not fetch issue details");
        }

        const issue = await response.json();

        // Fill issue information
        document.getElementById("detail-issue-id").textContent =
            `ISSUE ${issue.id}`;

        document.getElementById("detail-title").textContent =
            issue.title;

        document.getElementById("detail-description").textContent =
            issue.description || "No description available.";

        document.getElementById("detail-status").value =
            issue.status;

        document.getElementById("detail-priority").value =
            issue.priority;

        const reporter = teamMembers.find(
           user => user.id === issue.reporter_id
        );

        const assignee = teamMembers.find(
           user => user.id === issue.assigned_to_id
        );

        document.getElementById("detail-reporter").textContent =
           reporter ? reporter.name : "Unknown user";

        document.getElementById("detail-assignee").textContent =
           assignee ? assignee.name : "Unassigned";

        // Open the side panel
        document.getElementById("details-overlay").hidden = false;
        document.body.classList.add("details-open");

        // Load Resolution Trace
        await loadResolutionTrace(issueId);

    } catch (error) {
        console.error("Error loading issue details:", error);
        alert("Unable to load issue details.");
    }
}

// LOAD RESOLUTION TRACE
async function loadResolutionTrace(issueId) {
    const traceContainer = document.getElementById("resolution-trace");

    traceContainer.textContent = "Loading activity history...";

    try {
        const response = await fetch(
            `${API_BASE_URL}/issues/${issueId}/activities`
        );

        if (!response.ok) {
            throw new Error("Could not load activity history");
        }

        const activities = await response.json();

        traceContainer.replaceChildren();

        if (activities.length === 0) {
            traceContainer.textContent = "No activity recorded yet.";
            return;
        }

        activities.forEach(activity => {
            const item = document.createElement("div");
            item.className = "activity-item";

            const content = document.createElement("div");
            content.className = "activity-content";

            const title = document.createElement("strong");
            title.textContent = activity.action;

            const description = document.createElement("p");
            description.textContent =
                activity.details || "No additional details";

            const date = document.createElement("span");
            date.className = "activity-meta";
            date.textContent =
                new Date(activity.created_at).toLocaleString();

            content.append(title, description, date);
            item.appendChild(content);
            traceContainer.appendChild(item);
        });

    } catch (error) {
        console.error("Error loading resolution trace:", error);
        traceContainer.textContent = "Unable to load activity history.";
    }
}
// CLOSE ISSUE DETAILS PANEL
const detailsOverlay = document.getElementById("details-overlay");

document.getElementById("close-details").addEventListener("click", () => {
    detailsOverlay.hidden = true;
    document.body.classList.remove("details-open");
});

detailsOverlay.addEventListener("click", (event) => {
    if (event.target === detailsOverlay) {
        detailsOverlay.hidden = true;
        document.body.classList.remove("details-open");
    }
});
    