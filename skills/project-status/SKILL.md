---
name: project-status
description: Give a status update of each open stream/milestone on the project
---

# Project Status

Provide a comprehensive status update based on the **Current Focus** section and milestones.

## Workflow

1. Find and read the backlog file (check these locations in order):
   - `docs/backlog.md`
   - `backlog.md`
   - `.github/backlog.md`
   - `TODO.md`
2. **ALWAYS check the "Current Focus" section first** (if it exists) - this defines what we're actively working on
3. Review the Milestones Overview for high-level progress (if available)
4. Summarize each active initiative from Current Focus with:
   - What's complete (🟢)
   - What's in progress (🔵 or 🟡 Needs Verification)
   - What's blocked or at risk

## Output Format

```
## Project Status Update

### Current Milestone
**[Milestone Name]** - [Status emoji] [Progress %]
[Brief description of milestone goal]

---

### Current Focus: Active Initiatives

#### Initiative 1: [Name]
**Goal:** [Goal statement]
| Status | Item |
|--------|------|
| 🟢 Done | [Completed items] |
| 🔵 In Progress | [Active items] |
| 🟡 To Do | [Next items] |

#### Initiative 2: [Name]
**Goal:** [Goal statement]
| Status | Item |
|--------|------|
| 🟢 Done | [Completed items] |
| 🔵 In Progress | [Active items] |
| 🟡 To Do | [Next items] |

---

### Summary
- **Overall Progress:** [X of Y initiatives on track]
- **Blockers:** [Any blockers or risks]
- **Recommended Focus:** [What to prioritize next]
```

## Guidelines

- **Current Focus section is the source of truth** for active work (if it exists)
- Report on all initiatives listed in Current Focus
- Be concise but comprehensive
- Highlight any blockers or dependencies
- Include specific task IDs when referencing backlog items
- If an initiative is blocked, explain why and what's needed
- If no backlog file exists, report on recent git commits and open issues instead
