---
name: next
description: Outlines what can be done next in the project. Use when the user says "/next", "what's next", "what should I work on", or wants to see available tasks and next steps.
---

# Next Steps

Analyze the project backlog and provide actionable next steps based on the **Current Focus** section.

## Workflow

1. Find and read the backlog file (check these locations in order):
   - `docs/backlog.md`
   - `backlog.md`
   - `.github/backlog.md`
   - `TODO.md`
2. **ALWAYS check the "Current Focus" section first** (if it exists) - this defines the strategic initiatives
3. Identify tasks that are:
   - 🟡 To Do or 🟡 Needs Verification (ready to start)
   - 🔵 In Progress (should be completed)
   - Blocking other work
4. Present a concise summary with:
   - **Current Initiative**: Which initiative from Current Focus we're working on (if applicable)
   - **Recommended Next Tasks**: 3-5 tasks that align with Current Focus
   - **Quick Wins**: Any small tasks that can be completed quickly

## Output Format

```
## Current Initiative
[Initiative name from Current Focus section, or "General Development" if no focus defined]
**Goal:** [Goal from the initiative]

## Recommended Next Tasks
1. **[Task ID]**: [Task name] - [Brief context]
2. **[Task ID]**: [Task name] - [Brief context]
3. **[Task ID]**: [Task name] - [Brief context]

## Quick Wins (Optional)
- [Small task that can be done quickly]
```

## Guidelines

- **Current Focus section is the source of truth** for what to work on next (if it exists)
- Tasks in Current Focus take priority over other backlog items
- Consider task dependencies within the initiative
- Highlight any blocked items that need attention
- Keep suggestions actionable and specific
- If Current Focus has multiple initiatives, suggest tasks from the highest priority one first
- If no backlog file exists, suggest creating one or ask the user about priorities
