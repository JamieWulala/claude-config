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

## Project Initialization Strategy (2026-01-26)

**Every new project MUST go through this structured initialization process.** This prevents repeating mistakes from previous projects and ensures proper scaffolding from day one.

### Phase 1: Context Gathering

Before writing any code, gather context from three sources:

1. **Read the PRD/Requirements**
   - Convert any non-text formats (docx, pdf) to readable text
   - Identify: tech stack, external services, user flows, success metrics
   - Note any UI mockups or wireframes specified

2. **Review Similar Projects**
   - Check `~/workplace/` for projects with similar stack (Supabase, Stripe, Vercel, Next.js)
   - Extract: project structure, CLAUDE.md patterns, scripts, lessons learned
   - Identify bugs and pitfalls to avoid

3. **Identify External Services**
   - List all external services from PRD (Supabase, Stripe, GitHub API, email, etc.)
   - Each service = dedicated package with own CLAUDE.md

### Phase 2: Brainstorm Package Structure

Use the `superpowers:brainstorming` skill to collaboratively design:

**Standard Monorepo Structure:**
```
project-root/
├── CLAUDE.md                 # Project rules, lessons learned
├── packages/
│   ├── web/                  # Next.js frontend
│   ├── supabase/             # Auth, DB, RLS, migrations
│   ├── vercel/               # Deployment automation & verification
│   ├── stripe/               # Payments (if needed)
│   ├── shared/               # Types, logger, errors, validators
│   ├── e2e/                  # Playwright E2E tests (black-box)
│   ├── integration/          # Vitest component tests (white-box)
│   └── ui-mockups/           # v0 design workflow
├── docs/
│   ├── product-requirements.md
│   ├── architecture.md
│   ├── backlog.md
│   ├── backlog-items/
│   └── operations.md
├── scripts/
│   ├── dev/
│   ├── deploy/
│   ├── test/
│   ├── infra/
│   └── ops/
└── logs/
    ├── operations/
    ├── sessions/
    └── learnings/
```

**Questions to answer during brainstorm:**
- Which external services need dedicated packages?
- What's the UI-first workflow? (v0 mockups → approval → component generation)
- What verification scripts prevent "works for me" bugs?
- What E2E tests cover critical user flows?

### Phase 3: Generate Project Scaffolding

After brainstorm approval, generate in this order:

1. **Directory Structure**
   ```bash
   mkdir -p packages/{web,supabase,vercel,shared,e2e,integration,ui-mockups}
   mkdir -p docs/backlog-items
   mkdir -p scripts/{dev,deploy,test,infra,ops}
   mkdir -p logs/{operations,sessions,learnings}
   ```

2. **Root Files**
   - `CLAUDE.md` - Project rules (copy patterns from similar projects)
   - `pnpm-workspace.yaml` - Monorepo configuration
   - `package.json` - Root scripts
   - `.gitignore` - Include `/logs` by default

3. **Package CLAUDE.md Files** (one per package)
   - Each external service package gets detailed CLAUDE.md
   - Include: setup commands, env vars, CLI commands, troubleshooting

4. **Documentation**
   - `docs/product-requirements.md` - Copy/convert from PRD
   - `docs/architecture.md` - System design based on PRD
   - `docs/backlog.md` - Initial task breakdown
   - `docs/operations.md` - Scripts reference

5. **Scripts** (skeleton with proper headers)
   - `scripts/dev/start.sh`
   - `scripts/deploy/deploy.sh`, `verify.sh`
   - `scripts/test/run-all.sh`, `run-e2e.sh`, `run-integration.sh`
   - `scripts/infra/setup-{service}.sh` for each external service

6. **E2E Structure**
   - `packages/e2e/CLAUDE.md` - Testing rules
   - `packages/e2e/tests/pages/` - Page Object Models
   - `packages/e2e/tests/helpers/` - Auth, DB, API helpers

### Phase 4: UI-First Development Workflow

**Critical: Always generate UI mockups before code.**

```
v0 Mockup → User Approval → Component Code → Integration → E2E Test
```

1. **Generate v0 mockup** for each screen in PRD
2. **Get user feedback** on mockup before proceeding
3. **Generate component code** from approved mockup
4. **Wire up to backend** (Supabase, API routes)
5. **Write E2E test** that verifies the full flow

This prevents wasted effort on UI that doesn't match user expectations.

### Project Init Checklist

Before starting any implementation, verify:

- [ ] PRD read and understood
- [ ] Similar projects reviewed for patterns
- [ ] Package structure brainstormed and approved
- [ ] All CLAUDE.md files created (root + packages)
- [ ] `/docs` populated with PRD, architecture, backlog
- [ ] `/scripts` skeleton created with proper headers
- [ ] `/logs` directory structure created
- [ ] E2E test structure ready
- [ ] v0 mockups generated for first screens
- [ ] User approved mockups before component work

### Trigger Phrases

When user says any of these, invoke this initialization process:
- "New project"
- "Initialize project"
- "Set up [project name]"
- "Start a new [app/tool/service]"
- "Let's build [something] from scratch"

## Best Practices

### Expert Panel for Complex Questions (2026-01-24)
When faced with a complex question, invite a group of experts relevant to the domain and let them discuss the problem collaboratively. Present their different perspectives, debate trade-offs, and synthesize a plan from the discussion.

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

### All Testing MUST Use Scripts (2026-01-20)
**NEVER run ad-hoc test commands.** All testing must go through designated scripts in `/scripts/test/`.

**Why this matters:**
- Ad-hoc commands create uncertainty about what was actually tested
- Scripts document the canonical way to test each component
- Scripts can include setup, teardown, and proper environment configuration
- Scripts make testing reproducible across sessions

**The rule:**
1. Before testing anything, check `/scripts/test/` for an existing script
2. If no script exists, **create one first** before running tests
3. Never run `pnpm test`, `npx`, or direct test commands without a wrapper script

**Script naming convention:**
```
/scripts/test/
├── run-all.sh              # Run entire test suite
├── run-unit.sh             # Unit tests only
├── run-e2e.sh              # E2E tests only
├── test-{component}.sh     # Test specific component
├── diagnose-{issue}.ts     # Diagnostic scripts for debugging
└── verify-{flow}.sh        # Verify specific flows work
```

**Example enforcement:**
```bash
# BAD: Ad-hoc command (creates uncertainty)
pnpm test src/renderer/src/store/session-store.test.ts

# GOOD: Use designated script (reproducible, documented)
./scripts/test/test-session-store.sh
```

**When creating test scripts:**
- Include clear usage instructions in comments
- Support common flags (e.g., `--watch`, `--coverage`, `--diagnose`)
- Exit with proper codes so CI can use them
- Log what's being tested for visibility

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

### External Service Packages (2026-01-25)
When integrating external services (Supabase, Stripe, etc.), create dedicated packages with their own `CLAUDE.md`:

```
packages/
├── supabase/           # Supabase integration
│   ├── CLAUDE.md       # Setup, migrations, RLS policies, CLI commands
│   ├── client.ts       # Browser client
│   ├── server.ts       # Server client (service role)
│   └── types.ts        # Generated types
├── stripe/             # Stripe integration
│   ├── CLAUDE.md       # Products, webhooks, testing, CLI commands
│   ├── client.ts       # Client-side (loadStripe)
│   ├── server.ts       # Server-side (Stripe SDK)
│   └── webhooks.ts     # Webhook handlers
```

**Each service CLAUDE.md should document:**
- Setup scripts and verification commands
- Environment variables required
- Key concepts (RLS for Supabase, webhooks for Stripe)
- Common operations and troubleshooting
- Links to dashboard and docs

**Why separate packages:**
- Isolates service-specific complexity
- Makes it easy to find all service-related code
- CLAUDE.md provides context when working on that service
- Encourages reusable patterns across projects

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

**Task ID Naming Convention (2026-01-19):**
Use epic/category aliases as prefixes instead of generic `TASK-XXX`:

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

Format: `{PREFIX}-{NUMBER}` (3-digit zero-padded). Example: `AUTH-007`, `UIUX-023`.

For projects without clear epics, use generic `TASK-XXX`.

**Backlog Item Files (2026-01-19):**
When adding tasks to `backlog.md`, always create corresponding detail files in `/docs/backlog-items/{ID}.md`:

```markdown
## AUTH-007
state: unplanned
title: Short task title
epic: Epic Name (if applicable)
phase: Phase Name (if applicable)

### Description
What this task accomplishes and why it matters.

### Acceptance Criteria
- [ ] Specific, verifiable outcome 1
- [ ] Specific, verifiable outcome 2

### Technical Notes
Implementation hints, commands, or code snippets.

### Dependencies
- AUTH-003 (if blocked by another task)

### Current Status
*(Add when task moves to `review` or `blocked` state)*
What was accomplished, what needs verification, any known issues.
```

This ensures tasks have clear scope and acceptance criteria before work begins.

**Task File Structure for Review/Blocked States (2026-01-19):**
When moving a task to `review` or `blocked` state, add a `## Current Status` section:
- What was accomplished
- What's ready for verification
- Any known issues or limitations
- Blocker details (for blocked state)

This section is automatically displayed in the Argos task detail panel to provide context for review.

**Task State Discipline (2026-01-19):**
Backlog tasks move through states: `unplanned` → `planned` → `in_progress` → `review` → `done` (or `blocked`).

When **planning a task**:
1. Flesh out the detail file in `docs/backlog-items/{ID}.md`
2. Ensure it has clear acceptance criteria and technical notes
3. Update state to `planned` in both backlog.md and the detail file
4. A task is "planned" when someone could pick it up and know exactly what to do

When **starting work** on a task:
1. Update state to `in_progress` in both:
   - `docs/backlog.md` (table or checklist)
   - `docs/backlog-items/{ID}.md` (frontmatter)
2. Only one task should be `in_progress` at a time per stream of work

When **blocked**:
1. Update state to `blocked`
2. Add a note in the detail file explaining what's blocking

When **done**:
1. Update state to `done` (or `review` if needs verification)
2. Check off acceptance criteria in the detail file

Never leave tasks in `in_progress` across sessions without updating status.

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

## E2E Test-Driven Development (2026-01-20)

### Mandatory E2E Test Structure
Every project must have a dedicated E2E testing folder with its own documentation:

```
project-root/
├── e2e/                        # E2E test root
│   ├── CLAUDE.md               # E2E-specific rules and patterns
│   ├── fixtures/               # Test data matching production variations
│   │   ├── simple/             # Happy path scenarios
│   │   └── complex/            # Edge cases, fallback scenarios
│   ├── integration/            # Cross-module integration tests
│   │   └── *.spec.ts           # Tests that verify module boundaries
│   ├── workflows/              # User journey tests
│   │   └── *.spec.ts           # Full user flows (create, update, delete)
│   └── utils/                  # Test helpers and utilities
│       ├── setup.ts            # Global test setup
│       └── helpers.ts          # Shared test utilities
├── docs/
│   └── e2e-testing.md          # E2E testing strategy and coverage map
```

### E2E CLAUDE.md Template
Every `e2e/CLAUDE.md` should document:

```markdown
# E2E Testing Rules

## Test Commands
- `pnpm test:e2e` - Run all E2E tests
- `pnpm test:e2e:ui` - Run with Playwright UI
- `pnpm test:e2e <file>` - Run specific test

## Fixture Requirements
- All fixtures must match production data variations
- Each code branch must have a corresponding fixture

## Side Effect Verification (MANDATORY)
Every test must verify:
- [ ] UI state changes
- [ ] File/database persistence
- [ ] API calls made (if applicable)

## Coverage Requirements
- All user-facing features must have E2E tests
- All CRUD operations must be tested
- All error states must be tested
```

### Feature Development MUST Include E2E Tests
**No feature is complete without E2E tests.** Before marking any feature as `done`:

1. **Write E2E test first** - Define expected behavior before implementation
2. **Test all user flows** - Create, read, update, delete
3. **Verify side effects** - Not just UI, but persistence and state
4. **Test error cases** - Invalid input, network failures, edge cases
5. **Run against varied fixtures** - Ensure all code paths are exercised

```markdown
## Feature Completion Checklist
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] E2E tests written and pass
- [ ] Side effects verified (files, DB, API)
- [ ] Error states tested
- [ ] Fixtures cover all code branches
```

### E2E Tests Must Verify Side Effects (CRITICAL)
UI-only assertions give false positives. Always verify that expected side effects actually occurred:

```typescript
// BAD: Only verifies UI state - task might not be persisted!
await expect(taskCard).toBeVisible()

// GOOD: Verify BOTH UI and side effects
await expect(taskCard).toBeVisible()
expect(fs.existsSync(taskFilePath)).toBe(true)
expect(backlogContent).toContain(taskId)
```

**What to verify:**
- File writes (task files, config changes)
- Database mutations (query after action)
- API calls made (intercept and assert)
- State persistence (reload and verify)

### Test Fixtures Must Match Production Variations
Test fixtures that don't represent real-world data variations allow bugs to ship:

```
❌ Simple fixture: Single table, happy path only
✅ Production-like fixture: Multiple formats, edge cases, fallback scenarios
```

**Fixture checklist:**
- [ ] Covers all code branches (if/else, switch cases, fallback strategies)
- [ ] Includes edge cases from production data
- [ ] Has variations that exercise error handling
- [ ] Mirrors the complexity of real user data
- [ ] Documents which code path each fixture exercises

### Write E2E Tests BEFORE Manual Testing
When implementing features that affect user-facing behavior:

1. **Write the E2E test first** - Define expected behavior
2. **Make the test pass** - Implement the feature
3. **Run against varied fixtures** - Test all code paths
4. **Then manual test** - Confirm UX feels right

This catches bugs like "works in test, fails in production" before users see them.

### Debug Logging for Multi-Strategy Code
Functions with fallback strategies should log which path executed:

```typescript
console.log('[Module] Strategy 1: Attempting primary approach...')
if (primarySucceeds) {
  console.log('[Module] Strategy 1 SUCCESS')
  return result
}
console.log('[Module] Strategy 2: Falling back to secondary...')
```

This makes debugging production issues much faster.

### E2E Test Naming Convention
Use descriptive names that document the user story:

```typescript
// BAD: Vague names
test('task creation', ...)
test('handles error', ...)

// GOOD: User story format
test('user can create task with custom ID and see it in unplanned column', ...)
test('user sees error message when creating task with duplicate ID', ...)
```

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
- "Run tests" → Check `/scripts/test/`
- "Debug this" → Check `/scripts/test/diagnose-*.ts`
- "Verify this works" → Check `/scripts/test/verify-*.sh`
- "Set up [service]" → Check `/scripts/infra/`
- "Check logs" → Check `/scripts/ops/`

If no script exists and it's a repeatable operation, **create one first before proceeding**.

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

## Testing Guidelines

### E2E Testing (Playwright/WebdriverIO) Organization
- Organize tests by feature domain in dedicated directories (e.g., tests/e2e/functional/buckets/, `tests/e2e/functional/upload/`)
- Use naming convention: <feature>.test.ts (e.g., create-bucket.test.ts, `delete-object.test.ts`)
- Keep feature-specific helpers in helpers.ts files within feature directories
- Centralize shared utilities in /utils directory

### Page Object/Accessor Pattern
- Create accessor classes that encapsulate all DOM interactions for a page/component
- Expose UI elements as properties (buttons, inputs, tables)
- Provide high-level methods like setData(), waitForVisible(), sortByColumn()
- Never expose raw selectors in test files - always use accessors

### Test Data Management
- Generate unique resource names using session ID + suffix pattern
- Use beforeEach to reset test state, afterEach for cleanup
- Implement aggressive cleanup with time-based filtering (delete resources older than N hours)
- Always clean up resources even when tests fail - wrap cleanup in try/catch

### Eventual Consistency Handling
- Use batch verification pattern: verify condition N times consecutively before passing
- Implement retry utilities with configurable attempts and backoff
- Pattern: expectUntil(condition, description, { batchSize, maxRetries, timeout })
- Pattern: getDataWithRetries(call, expected, maxRetries, matchingDataSets)

### Debugging Support
- Capture screenshots automatically on test failures
- Generate HAR files for network request/response logging
- Implement structured logging with levels (verbose, debug, info, warning, error, fatal)

### Test Categorization
- Tag tests by environment (gamma/prod), severity (sanity/durability), and purpose (canary/a11y)
- Define test suites with metadata: files, tags, priority, groups, dependencies
- Support filtering by tags via CLI (e.g., `--tag sanity`)

### Integration/Component Testing (Jest/RTL) Organization
- Collocate tests with source: src/[domain]/__tests__/[component].test.tsx
- Keep test helpers in __tests__/helpers/ subdirectories
- Use .test.ts/.test.tsx for unit/component tests
- Use .integ.ts/.integ-ui.tsx for integration tests

### Mocking Strategy
- Create default connector mocks that stub all methods with jest.fn()
- Default mocks should log warnings when unmocked methods are called
- Use override mocks for specific test behavior - import after defaults
- Pattern: jest.createMockFromModule() + selective overrides

### Fixture Pattern (Builder/Modifier)
- Use immutable fixture builders with deep cloning
- Pattern: buildModelModifier<T>(base: T) => (modifier?: (base: T) => void) => T
- Naming: MOCK_[DOMAIN]_[TYPE] for constants, get[Domain][Type] for builders
- Separate SDK model fixtures from display model fixtures

### White Box Component Testing
- Mock connectors at the function level with controlled responses
- Test both success and failure paths explicitly
- Use accessor classes to abstract DOM queries from implementation
- Test observable/epic flows with marble diagrams when using RxJS

### Async Test Handling
- Always wrap async operations in act() for React state updates
- Use waitFor() for assertions that depend on async state
- Implement navigation helpers that wait for path changes and spinners
- Account for eventual consistency in distributed system tests with delays

### Parameterized Testing
- Use test.each() or custom parameterized test runners for multiple scenarios
- Pattern: testCases.forEach(({ description, input, expected }) => it(description, ...))
- Keep test data arrays near the tests they serve

### State Isolation
- Reset mocks between tests with jest.clearAllMocks() or beforeEach
- Reset router history and DOM state between tests
- Use mock stores for Redux testing to isolate state changes

### General Testing Principles
1. **Isolation:** Each test must be self-contained with proper setup/teardown
2. **Determinism:** Use batch verification and retries for eventual consistency
3. **Debuggability:** Comprehensive logging, screenshots, and network capture
4. **Cleanup:** Always clean up created resources, even on failure
5. **Parameterization:** Use data-driven tests to reduce duplication
6. **Async Safety:** Proper await, act(), and waitFor() usage
7. **Mock Clarity:** Default mocks with explicit overrides prevent surprises
8. **Naming:** "should [behavior] when [condition]" for test descriptions
