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

### Single Source of Truth + Logging (2026-01-15)
Always use a single source of truth for operations. Write logs for future reference and debugging.

### Task Tracking with backlog.md (2026-01-15)
Create `backlog.md` in project root for task tracking. Use this to track upcoming work, priorities, and project roadmap.

### Check Existing Patterns First (2026-01-15)
Before implementing something new, search the codebase for existing patterns and conventions. Match the project's style.

### Verify Deployments After Push (2026-01-15)
After pushing changes, always verify deployment succeeded. Check logs and don't assume success.

### Test OAuth Flows End-to-End (2026-01-15)
Button click isn't enough - verify the full redirect cycle completes successfully. Check callback handling.

### Prefer Direct APIs Over Browser Automation (2026-01-15)
Before reaching for Playwright/Puppeteer, check the network tab for direct APIs. They're faster, more reliable, and lighter.

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
