---
name: react-review
description: Review React/Next.js code for performance issues and best practices. Use when user says "review React", "check performance", "optimize component", or "/react-review".
---

# React Performance Review

Review React/Next.js code for performance issues and best practices.

## Triggers

Use this skill when the user says:
- "Review this React component"
- "Check for performance issues"
- "Optimize this Next.js page"
- "Review my React code"
- `/react-review`

## How It Works

1. Read the specified file(s) or recently modified React/Next.js files
2. Apply Vercel Engineering performance rules (45 rules, 8 categories)
3. Check against UI/UX guidelines (100+ rules, 11 categories)
4. Report issues with `file:line - issue` format
5. Suggest fixes with code examples

## Categories (Priority Order)

### Critical Priority
| Category | Prefix | Impact |
|----------|--------|--------|
| Async Waterfalls | `async-` | 2-10x improvement |
| Bundle Size | `bundle-` | 15-70% faster loads |

### High Priority
| Category | Prefix | Impact |
|----------|--------|--------|
| Server Performance | `server-` | Reduced TTFB |
| Client Data Fetching | `client-` | Fewer requests |

### Medium Priority
| Category | Prefix | Impact |
|----------|--------|--------|
| Re-renders | `rerender-` | Smoother UI |
| Rendering | `rendering-` | Less jank |

### Low Priority
| Category | Prefix | Impact |
|----------|--------|--------|
| JS Micro-opts | `js-` | Marginal gains |
| Advanced | `advanced-` | Edge cases |

## Rules Checklist

### Async Waterfalls (CRITICAL)
- [ ] **async-parallel**: Use `Promise.all()` for independent operations
- [ ] **async-defer-await**: Move `await` into branches where actually used
- [ ] **async-api-routes**: Start promises early, await late
- [ ] **async-suspense-boundaries**: Use Suspense to stream content

### Bundle Size (CRITICAL)
- [ ] **bundle-barrel-imports**: Import directly, avoid barrel files (`lucide-react`, `@mui/material`)
- [ ] **bundle-dynamic-imports**: Use `next/dynamic` for heavy components
- [ ] **bundle-defer-third-party**: Load analytics/tracking after hydration
- [ ] **bundle-preload**: Preload on hover/focus for perceived speed

### Server Performance (HIGH)
- [ ] **server-cache-react**: Use `React.cache()` for per-request deduplication
- [ ] **server-serialization**: Minimize data passed to client components
- [ ] **server-parallel-fetching**: Restructure components to parallelize fetches

### Re-render Optimization (MEDIUM)
- [ ] **rerender-memo**: Extract expensive work into memoized components
- [ ] **rerender-dependencies**: Use primitive dependencies in effects
- [ ] **rerender-functional-setstate**: Use `setCount(c => c + 1)` for stable callbacks
- [ ] **rerender-lazy-state-init**: Pass function to `useState` for expensive init

### UI/UX Guidelines
- [ ] **a11y**: Icon buttons have `aria-label`, form controls have labels
- [ ] **focus**: Visible focus indicators (`focus-visible:ring-*`)
- [ ] **forms**: Inputs have `autocomplete`, `type`, `name` attributes
- [ ] **images**: All `<img>` have explicit `width` and `height`
- [ ] **animation**: Only animate `transform`/`opacity`, respect `prefers-reduced-motion`
- [ ] **semantics**: `<button>` not `<div onClick>`, `<a>` for navigation

## Anti-Patterns to Flag

```
❌ Sequential awaits for independent operations
❌ Barrel imports from package roots
❌ user-scalable=no or maximum-scale=1
❌ onPaste with preventDefault
❌ transition: all
❌ outline-none without focus-visible replacement
❌ <div onClick> instead of <button>
❌ Images without dimensions
❌ Unvirtualized lists > 50 items
❌ Hardcoded date/number formats
```

## Output Format

```
## Performance Review: {filename}

### Critical Issues
- `file.tsx:42` - Sequential awaits: Use Promise.all() for fetchUser/fetchPosts
- `file.tsx:15` - Barrel import: Import directly from 'lucide-react/dist/esm/icons/check'

### High Priority
- `file.tsx:88` - Large client payload: Only pass needed fields to ClientComponent

### Medium Priority
- `file.tsx:55` - Missing memo: Extract ExpensiveList into React.memo()

### UI/Accessibility
- `file.tsx:23` - Missing aria-label on icon button
- `file.tsx:67` - Image missing width/height attributes

### ✓ Passing
- No async waterfalls detected
- Proper Suspense boundaries
```

## Usage

```
/react-review                     # Review recently modified files
/react-review src/components/     # Review specific directory
/react-review src/app/page.tsx    # Review specific file
```

## References

- [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)
- [Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines)
