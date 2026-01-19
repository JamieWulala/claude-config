# Global Claude Guidelines

## Constraints

### No Co-Authored-By Footer (2026-01-15)
Never add `Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>` or any AI attribution to commit messages.

### Concise Commit Messages (2026-01-15)
Keep commit messages concise - prefer one-line summaries. Avoid verbose multi-line bodies unless absolutely necessary.

### Minimal Changes Only (2026-01-15)
Don't add features, refactor, or "improve" beyond what's asked. Keep solutions focused on the specific request.

### Read Before Edit (2026-01-15)
Never modify code you haven't read. Always understand existing code before suggesting changes.

## Best Practices

### File Header Comments (2026-01-19)
Every code file should start with a comment block containing three sections:

```typescript
/**
 * @role
 * What this file does and where it fits in the system.
 * Example: "API route handler for user authentication. Sits between client and auth service."
 *
 * @scope-exclusions
 * What this file should NOT handle (prevents scope creep):
 * - Session management (handled by /lib/session)
 * - Password hashing (handled by /lib/crypto)
 *
 * @usage
 * How to use this module correctly:
 * - Import: `import { authenticate } from '@/api/auth'`
 * - Test: `pnpm test src/api/auth.test.ts`
 */
```

**Purpose**: Improves maintainability by making scope explicit upfront. Prevents files from becoming dumping grounds for unrelated functionality.

**When to include**:
- All new files with logic (skip for pure type definitions, simple configs)
- Components, utilities, API routes, services, hooks

**Keep it concise**: 2-5 lines per section max. If it needs more, the file is doing too much.

### Single Source of Truth Documentation (2026-01-18)
Every project needs a `/docs` directory as the canonical source for all knowledge:
- `/docs/product-requirements.md` - What we're building and why
- `/docs/architecture.md` - How the system works
- `/docs/backlog.md` - Current tasks and priorities
- `/docs/operations.md` - How to deploy, test, debug
- `/docs/lessons-learned.md` - Pitfalls and patterns discovered

Update docs AS you work, not after. Reference from CLAUDE.md, don't duplicate.

### Script-Based SOPs (2026-01-18)
**Script everything you do more than once.** Put all scripts in `/scripts`:
```
/scripts
├── dev/           # start.sh, reset-db.sh
├── deploy/        # deploy.sh, verify.sh
├── test/          # run-tests.sh, test-api.sh
├── infra/         # setup-prod.sh, set-secrets.sh
└── ops/           # check-logs.sh, rollback.sh
```

When asked to do something manually, check if a script exists. If not, **propose creating one**:
> "I notice we don't have a script for this. Want me to create `/scripts/deploy/deploy-prod.sh`?"

### Default to Dev, Confirm for Prod (2026-01-18)
All scripts should default to development environment. Production operations require explicit `--prod` flag AND confirmation prompt:
```bash
ENV=${1:-dev}
if [[ "$ENV" == "prod" ]]; then
    read -p "⚠️  PROD operation. Type 'yes': " confirm
    [[ "$confirm" != "yes" ]] && exit 1
fi
```

### Monorepo Package Documentation (2026-01-18)
In monorepos, each package needs its own `CLAUDE.md` documenting:
- Package-specific build commands
- Dependencies and their purposes
- Cross-package data dependencies (what fields this package expects from others)

### Execution Logs Directory (2026-01-19)
Every monorepo should have a `/logs` directory at project root for documenting:

```
/logs
├── operations/           # SOP execution logs
│   ├── deployments/      # Vercel, Railway, Supabase deploys
│   ├── migrations/       # Database migrations
│   └── incidents/        # Outages, rollbacks, hotfixes
├── sessions/             # Claude Code session summaries
│   └── YYYY-MM-DD-*.md   # What was accomplished, decisions made
├── learnings/            # Patterns and pitfalls discovered
│   ├── bugs/             # Root cause analyses (COE)
│   └── discoveries/      # Useful techniques found
└── progress/             # Project milestones and metrics
    └── weekly/           # Weekly progress snapshots
```

**Guidelines:**
- Subfolder structure is flexible - create what makes sense for the context
- Name files with ISO dates: `2026-01-19-vercel-deploy.md`
- Keep entries concise - bullet points, not essays
- Link to relevant commits, PRs, or docs
- This is a **living log**, not a formal document

**When to log:**
- After any deployment or infrastructure change
- After resolving a tricky bug (COE analysis)
- After a significant session with learnings
- When discovering a pattern worth remembering

**Example entry** (`/logs/operations/deployments/2026-01-19-railway-worker.md`):
```markdown
# Railway Worker Deployment - 2026-01-19

## What
Deployed eligibility-worker with AeroDataBox fallback fix

## Changes
- Fallback on ANY SSET error (not just specific ones)
- Include flight_date in SSET jobs for fallback

## Commits
- 33c22d7 fix: fallback to AeroDataBox on ANY SSET error
- 796ec85 fix: include flight_date in SSET jobs

## Verification
- [ ] Railway deployment completed
- [ ] Logs show fallback working
- [ ] Test flight shows correct status
```

> The `/logs` directory is gitignored by default. Add to git if you want to preserve history.

### Task Tracking with backlog.md (2026-01-15)
Create `backlog.md` in `/docs` for task tracking. Track upcoming work, priorities, and roadmap.

### Check Existing Patterns First (2026-01-15)
Before implementing something new, search the codebase for existing patterns and conventions. Match the project's style.

### Verify Deployments After Push (2026-01-15)
After pushing changes, always verify deployment succeeded. Check logs and don't assume success.

### Test OAuth Flows End-to-End (2026-01-15)
Button click isn't enough - verify the full redirect cycle completes successfully. Check callback handling.

### Prefer Direct APIs Over Browser Automation (2026-01-15)
Before reaching for Playwright/Puppeteer, check the network tab for direct APIs. They're faster, more reliable, and lighter.

### Script External Service Setup (2026-01-15)
Always use scripts for external service configuration and credential management. Avoid manual dashboard actions - human steps add intransparency and uncertainty. Use CLI tools (gh, vercel, railway, supabase) to set secrets programmatically.

## Common Pitfalls

### Verify CSS Variable Pairs (2026-01-15)
In UI libraries (Shadcn, etc.), always check that `--*-foreground` variables contrast with their `--*` counterparts. Example: `--destructive-foreground` should be white, not the same red as `--destructive`.

### Check HTML Semantics in UI Libraries (2026-01-15)
Components like `AlertDialogDescription` render as `<p>` elements. Don't nest block elements (`<p>`, `<div>`, `<ul>`) inside them - use `asChild` prop or `<span className="block">` instead.

## User Preferences

### Testing Email Recipients
When testing emails, only send to Jamie's addresses:
- `jamie.laevatin@gmail.com`
- `jamieli98909@gmail.com`

Never send test emails to other users in the database.

### UI Feedback Iterations (2026-01-16)
When user gives negative UI feedback ("ugly", "not visible", etc.), iterate quickly:
- Ask for preferences with concrete options (AskUserQuestion tool)
- Don't defend initial implementation - just fix it
- Be ready for multiple rounds of adjustment

## Compounding Engineering (2026-01-18)

### Every Task Should Leave the Codebase Smarter
After completing any task, proactively ask:
1. **New script?** Should this manual process be automated in `/scripts`?
2. **Doc update?** Should `/docs` or `CLAUDE.md` be updated?
3. **Lesson learned?** Is there a pitfall or pattern to document?
4. **New skill?** Could this workflow become a reusable `/skill`?

### Trigger Phrases → Check for Scripts
When user says:
- "Deploy this" → Check `/scripts/deploy/`
- "Test the API" → Check `/scripts/test/`
- "Set up [service]" → Check `/scripts/infra/`
- "Check logs" → Check `/scripts/ops/`

If no script exists and it's a repeatable operation, propose creating one.

### Red Flags to Address
- "Let me check the dashboard..." → Should be a script
- "I think we do it this way..." → Should be documented
- "Which environment is this?" → Should be obvious from script/config

> "If it's worth doing twice, it's worth scripting."

### Hierarchical CLAUDE.md (2026-01-18)
Use three levels of documentation for context that compounds:
- **Global** (`~/.claude/CLAUDE.md`): Cross-project preferences and universal patterns
- **Project** (`/CLAUDE.md`): Project-specific patterns, lessons, tech stack
- **Package** (`/packages/*/CLAUDE.md`): Package-specific conventions and APIs

Update the appropriate level based on generality. Project patterns don't belong in global.

### Session Wrap-Up Discipline (2026-01-18)
At end of every significant session, update:
1. `/docs/backlog.md` with completed/in-progress task status
2. `/logs/sessions/YYYY-MM-DD-summary.md` with what was accomplished
3. `/logs/learnings/` if any bugs were fixed or patterns discovered
4. CLAUDE.md (appropriate level) with any lessons learned
5. Consider if any workflow should become a skill

This ensures context isn't lost between sessions.

### Root Cause Analysis - 5 Whys (2026-01-18)
When bugs occur, don't just fix the symptom. Ask "Why?" recursively:
```
Problem → Why #1 → Why #2 → Why #3 → Why #4 → Why #5 (root cause)
```
Stop when you reach a process, knowledge, or tooling gap. Then fix at 3 layers:
1. **Immediate**: Fix the current bug
2. **Preventive**: Add validation, tests, or docs to prevent recurrence
3. **Detection**: Add checks to catch similar issues earlier

Document patterns in CLAUDE.md so the same mistake isn't made twice.

### Make Systems Verifiable (2026-01-18)
Since AI coding is opaque to the user, make verification easy:
- **Version endpoint**: `/api/version` returns build version and timestamp
- **Health check**: Quick endpoint to verify service is running
- **Structured logging**: Shared logger with context, not console.log
- **Error codes as enums**: Consistent, searchable error handling
- **Debug endpoints**: `/api/debug/*` routes in development only

### Strategic Focus Drives Task Selection (2026-01-18)
Maintain a "Current Focus" section in backlog with 2-4 strategic initiatives:
```markdown
## Current Focus
### Initiative 1: [Name]
**Goal:** [What success looks like]
| Task | Status |
```
All task selection should align with current initiative. This prevents scope creep and ensures coherent progress across sessions.

### Skills as SOPs (2026-01-18)
Turn repetitive workflows into documented skills in `.claude/skills/`:
- **Deployment**: `/deploy-and-verify` - bump version, push, verify
- **Debugging**: `/coe-analysis` - 5 Whys root cause analysis
- **Session mgmt**: `/wrap-up` - capture learnings, update backlog
- **Task selection**: `/next` - choose based on Current Focus
- **Maintenance**: `/groom-backlog` - audit task status and priority

Skills should have: trigger phrases, step-by-step workflow, output format, troubleshooting.

## React & Next.js Best Practices (2026-01-18)

> Based on Vercel Engineering guidelines. Apply when writing or reviewing React/Next.js code.

### Critical: Eliminate Async Waterfalls
Sequential awaits for independent operations are the #1 performance killer:

```typescript
// BAD: Sequential (3 round trips)
const user = await fetchUser()
const posts = await fetchPosts()
const comments = await fetchComments()

// GOOD: Parallel (1 round trip)
const [user, posts, comments] = await Promise.all([
  fetchUser(),
  fetchPosts(),
  fetchComments()
])
```

In API routes: **start promises early, await late**.

### Critical: Avoid Barrel File Imports
Barrel imports (from package root) load thousands of modules:

```typescript
// BAD: Loads entire library (~200-800ms)
import { Check, X } from 'lucide-react'
import { Button } from '@mui/material'

// GOOD: Direct imports (~2KB vs ~1MB)
import Check from 'lucide-react/dist/esm/icons/check'
import Button from '@mui/material/Button'
```

**Next.js 13.5+ fix** - add to `next.config.js`:
```js
experimental: {
  optimizePackageImports: ['lucide-react', '@mui/material', 'lodash', 'date-fns']
}
```

### High: Server Component Data Minimization
Only pass what client components actually need:

```typescript
// BAD: Passes entire user object
<ClientComponent user={user} />

// GOOD: Pass only needed fields
<ClientComponent name={user.name} avatar={user.avatar} />
```

### Medium: Re-render Optimization
1. **Extract expensive work into memoized components** - enables early returns before computation
2. **Use primitive dependencies** in useEffect/useMemo - objects trigger on every render
3. **Functional setState** for stable callbacks: `setCount(c => c + 1)` not `setCount(count + 1)`
4. **Lazy state initialization**: `useState(() => expensiveComputation())` not `useState(expensiveComputation())`

### Medium: Animation Performance
- Only animate `transform` and `opacity` (GPU-accelerated)
- Never use `transition: all` - list properties explicitly
- Respect `prefers-reduced-motion`
- Animate SVG via wrapper `<g>` with `transform-box: fill-box`

### UI Review Checklist
When reviewing React UI code, check:
- [ ] **Accessibility**: Icon buttons have `aria-label`, form controls have labels
- [ ] **Focus states**: Visible focus indicators (don't use `outline-none` without replacement)
- [ ] **Forms**: Inputs have `autocomplete`, `type`, and `name` attributes
- [ ] **Images**: All `<img>` have explicit `width` and `height` to prevent CLS
- [ ] **Loading**: Use skeleton states, not spinners for content areas
- [ ] **Errors**: Inline near fields, not toast-only
- [ ] **State in URL**: Filters, tabs, pagination sync with query params
- [ ] **Semantic HTML**: `<button>` not `<div onClick>`, `<a>` for navigation

### Anti-Patterns to Flag
- `user-scalable=no` or `maximum-scale=1` (disables zoom)
- `onPaste` with `preventDefault` (blocks password managers)
- `transition: all` (poor performance)
- `outline-none` without `focus-visible` replacement
- `<div onClick>` instead of `<button>`
- Images without dimensions
- Unvirtualized lists > 50 items
- Hardcoded date/number formats (use `Intl.*`)
