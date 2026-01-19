---
name: wrapup
description: End-of-session workflow to capture learnings, update docs, and commit changes. Use when the user says "/wrapup", "wrap up", "end session", "done for now", or wants to close out a work session with proper documentation and git hygiene.
---

# Session Wrap-Up

Comprehensive end-of-session workflow that captures context, updates documentation, commits changes, and suggests learnings.

## When to Use

- At the end of a significant coding session
- After completing a feature or fixing a bug
- Before switching to a different project
- When the user wants to preserve session context

## Workflow

### Phase 1: Gather Session Context

1. **Review what was accomplished**
   - Check git diff for uncommitted changes
   - Check git log for recent commits in this session
   - Review any todos that were completed
   - Note any errors encountered and how they were resolved

2. **Identify key decisions and learnings**
   - What approaches worked well?
   - What patterns should be documented?
   - Were there any surprises or gotchas?
   - Any new constraints discovered?

### Phase 2: Update Documentation

Update docs in priority order. Always use existing files, never create new ones unless explicitly requested.

#### 2a. Update `/docs/backlog.md`
- Mark completed tasks as ✅ Done
- Update in-progress tasks with current status
- Add any new tasks discovered during the session
- Keep "Current Focus" section accurate

#### 2b. Update `/docs/lessons-learned.md` (if exists)
- Add any pitfalls discovered
- Document patterns that worked well
- Note any debugging insights

#### 2c. Update Work Log
Check for a logs section in the project. Common locations:
- `/docs/worklog.md`
- `/docs/changelog.md`
- `CHANGELOG.md`

If no work log exists, suggest creating `/docs/worklog.md` with format:
```markdown
# Work Log

## 2026-01-19

### Session Summary
[Brief description of what was accomplished]

### Changes Made
- [File/component]: [What changed]

### Learnings
- [Any insights or patterns discovered]
```

### Phase 3: Update CLAUDE.md (Learnings & Rules)

Determine the appropriate level for each learning:

| Learning Type | Destination |
|--------------|-------------|
| Cross-project patterns | `~/.claude/CLAUDE.md` (Global) |
| Project-specific patterns | `/CLAUDE.md` (Project) |
| Package-specific conventions | `/packages/*/CLAUDE.md` (Package) |

**Format for new rules:**
```markdown
### [Rule Name] (YYYY-MM-DD)
[Concise explanation of the rule and why it matters]
```

Ask the user before adding new rules to CLAUDE.md files.

### Phase 4: Git Commit

Use scripts if available, otherwise standard git:

```bash
# Check for deploy script
./scripts/deploy/deploy.sh 2>/dev/null || git add . && git commit

# For production
./scripts/deploy/deploy.sh prod
```

**Commit message format:**
- Keep it concise (one line preferred)
- Describe what changed, not how
- NO Co-Authored-By footer

### Phase 5: Push and Verify

1. Push to remote:
   ```bash
   git push origin HEAD
   ```

2. Verify deployment (if applicable):
   ```bash
   ./scripts/deploy/verify.sh
   ```

3. Check deployment URL if production

### Phase 6: Suggest Learnings

Present suggested additions to CLAUDE.md:

```markdown
## Suggested CLAUDE.md Updates

### For Global (~/.claude/CLAUDE.md)
- [Learning that applies across projects]

### For Project (/CLAUDE.md)
- [Learning specific to this project]

Would you like me to add any of these?
```

## Output Format

```markdown
## Session Wrap-Up Summary

### Accomplished
- [What was done in this session]

### Documentation Updated
- ✅ `/docs/backlog.md` - [changes]
- ✅ `/docs/worklog.md` - [entry added]
- ⏭️ `CLAUDE.md` - [pending user approval]

### Git Status
- Commit: `abc1234` - [message]
- Pushed to: `origin/main`
- Deployment: ✅ Verified at [URL]

### Suggested Learnings
[Proposed CLAUDE.md additions for user approval]
```

## Important Notes

- Always ask before modifying CLAUDE.md files (they compound across sessions)
- Use existing scripts from `/scripts/` folder when available
- Update docs AS you go, don't batch at the end
- Keep commit messages concise
- Verify deployments don't just check HTTP status - verify content
