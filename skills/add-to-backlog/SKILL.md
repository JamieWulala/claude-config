---
name: add-to-backlog
description: Add tasks, epics, or initiatives to the project backlog. Use when the user says "/add-to-backlog", "add task", "create backlog item", "new feature request", or describes work they want to track. Automatically determines the right structure (task, epic, or initiative) and creates both the backlog entry and detail file.
---

# Add to Backlog

Add items to the project backlog with proper structure and detail files.

## When to Use

- User describes a feature, bug, or work item to track
- User says "add to backlog", "create task", "new feature"
- User wants to plan future work
- After discovering work during another task

## Workflow

### 1. Find the Backlog

Locate the backlog file (check in order):
- `docs/backlog.md`
- `backlog.md`
- `.github/backlog.md`

If no backlog exists, offer to create one following the standard structure.

### 2. Analyze the Request

Determine what type of item to create based on scope:

| Type | Scope | Example |
|------|-------|---------|
| **Initiative** | Strategic goal with multiple epics | "Enable E2E testing infrastructure" |
| **Epic** | Theme with multiple related tasks | "UI/UX Campaign" |
| **Milestone** | Time-boxed group of tasks | "M1: App Shell (Week 1)" |
| **Task** | Single actionable work item | "Add drag-drop to Kanban" |

**Decision Tree:**
```
Is this a strategic multi-month goal? → Initiative
Is this a theme grouping many features? → Epic
Is this a single deliverable? → Task
```

### 3. Determine Task ID with Epic Prefix

Use epic/category aliases as prefixes:

| Prefix | Category | Example |
|--------|----------|---------|
| `AUTH-` | Authentication, OAuth, sessions | `AUTH-007` |
| `UIUX-` | UI/UX design, styling, animations | `UIUX-023` |
| `FEAT-` | New features, functionality | `FEAT-015` |
| `BUG-` | Bug fixes | `BUG-042` |
| `OPS-` | Operations, deployment, infra | `OPS-003` |
| `PERF-` | Performance optimization | `PERF-008` |
| `TEST-` | Testing infrastructure | `TEST-011` |
| `DOCS-` | Documentation | `DOCS-005` |
| `REFAC-` | Refactoring, tech debt | `REFAC-012` |

Find the highest existing number for that prefix:
```bash
grep -oE 'AUTH-[0-9]+' docs/backlog.md | sort -t'-' -k2 -n | tail -1
```

Increment to get the next ID (e.g., `AUTH-006` → `AUTH-007`).

For projects without clear epics, use generic `TASK-XXX`.

### 4. Ask Clarifying Questions (if needed)

If the request is ambiguous, ask:
- What problem does this solve?
- What does "done" look like? (acceptance criteria)
- Does this depend on other work?
- Which initiative/epic does this belong to?

### 5. Create the Backlog Entry

**For a Task** - Add to the appropriate section in backlog.md:

```markdown
## Epics

### Epic: [Epic Name]
...
- [ ] FEAT-015 - [Task title]
```

AND add to the Task Index table:

```markdown
| FEAT-015 | [Task title] | unplanned | [Phase/Category] |
```

**For an Epic** - Add a new epic section:

```markdown
### Epic: [Epic Name]
**Theme:** [What this epic accomplishes]
**Dependencies:** [Any prerequisites]

#### Phase 1: [Phase Name]
- [ ] AUTH-007 - [First task]
- [ ] AUTH-008 - [Second task]
```

**For an Initiative** - Add to Current Focus:

```markdown
### Initiative N: [Initiative Name]
**Goal:** [What success looks like]
```

### 6. Create Task Detail Files

For EACH task, create `/docs/backlog-items/{ID}.md` (e.g., `AUTH-007.md`):

```markdown
## AUTH-007
state: unplanned
title: [Task title]
epic: [Epic name, if applicable]
phase: [Phase name, if applicable]

### Description
[What this task accomplishes and why it matters.
Include context that helps understand the "why".]

### Acceptance Criteria
- [ ] [Specific, verifiable outcome 1]
- [ ] [Specific, verifiable outcome 2]
- [ ] [Specific, verifiable outcome 3]

### Technical Notes
[Implementation hints, relevant code paths, commands, or examples.
Include enough detail for someone unfamiliar with the area.]

### Dependencies
- [AUTH-003 if blocked by another task]
- [Or "None" if independent]
```

### 7. Confirm Creation

Report what was created:

```
✅ Added to backlog:

**[Task/Epic/Initiative]:** [Title]
- ID: AUTH-007
- Epic: [Epic name]
- State: unplanned

**Files created:**
- docs/backlog.md (updated)
- docs/backlog-items/AUTH-007.md

**Next steps:**
- Review and refine acceptance criteria
- Move to "planned" when ready to work on it
```

## Output Guidelines

### Good Task Titles
- Start with a verb: "Add", "Fix", "Implement", "Create", "Update"
- Be specific: "Add dark mode toggle to settings" not "Dark mode"
- Include context: "Fix login redirect on Safari" not "Fix bug"

### Good Acceptance Criteria
- Observable outcomes, not implementation details
- Each criterion independently verifiable
- Include edge cases if relevant

**Good:**
```markdown
- [ ] User can toggle dark mode from settings menu
- [ ] Preference persists across app restarts
- [ ] All text remains readable in dark mode
```

**Bad:**
```markdown
- [ ] Use CSS variables for theming
- [ ] Store preference in localStorage
```

### Good Technical Notes
- Relevant file paths or components
- Similar patterns in the codebase to reference
- Commands to run
- Potential gotchas

## Handling Multiple Tasks

If the request implies multiple tasks:

1. Break into logical chunks (each independently valuable)
2. Reserve sequential task IDs
3. Identify dependencies between them
4. Group under an epic if > 3 related tasks
5. Create detail files for each

Example:
```
User: "Add user authentication with OAuth"

Break into:
- AUTH-001: Add Google OAuth provider
- AUTH-002: Create login/logout UI
- AUTH-003: Implement session persistence
- AUTH-004: Add protected route middleware
```

## Edge Cases

**No docs/backlog-items/ folder:** Create it.

**User gives vague description:** Ask clarifying questions before creating.

**Task already exists:** Search for duplicates first. If similar task exists, ask if this is a duplicate or distinct work.

**Very large scope:** Suggest breaking into an epic with multiple tasks rather than one giant task.
