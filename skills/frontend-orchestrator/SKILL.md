---
name: frontend-orchestrator
description: "Orchestrator for UI feature development. Combines ui-ux-pro-max (design systems, UX best practices, accessibility) with frontend-design (creative direction, bold aesthetics). Use when building any UI feature: components, pages, dashboards, landing pages, forms, or visual interfaces. Triggers: 'build UI', 'create component', 'design page', 'implement feature', 'add UI', '/frontend', '/ui'."
---

# Frontend Orchestrator

Intelligent orchestration layer that combines two specialized skills:
- **ui-ux-pro-max**: Design systems, UX patterns, accessibility, validation
- **frontend-design**: Creative direction, bold aesthetics, avoiding generic AI looks

## When This Skill Activates

Any UI feature work including:
- Building new components or pages
- Creating dashboards, landing pages, forms
- Implementing visual features
- Designing user interfaces
- Adding UI elements to existing applications

## Orchestration Decision Tree

```
┌─────────────────────────────────────────────────────────────┐
│                    UI FEATURE REQUEST                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: DESIGN SYSTEM (ui-ux-pro-max)                    │
│  • Generate design system for product type                  │
│  • Get color palette, typography, style recommendations     │
│  • Identify UX patterns and accessibility requirements      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: CREATIVE DIRECTION (frontend-design)              │
│  • Choose bold aesthetic direction based on design system   │
│  • Define differentiation: what makes it UNFORGETTABLE      │
│  • Commit to specific tone: minimal, maximal, retro, etc.   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: IMPLEMENTATION                                    │
│  • Build with creative direction + design system rules      │
│  • Apply UX best practices from ui-ux-pro-max              │
│  • Ensure distinctive aesthetic from frontend-design        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: VALIDATION (ui-ux-pro-max)                       │
│  • Run pre-delivery checklist                               │
│  • Verify accessibility compliance                          │
│  • Check interaction patterns                               │
└─────────────────────────────────────────────────────────────┘
```

## Workflow

### Phase 1: Design System Generation

Run ui-ux-pro-max design system search:

```bash
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system -p "Project Name"
```

Extract from results:
- Recommended style (glassmorphism, minimalism, etc.)
- Color palette (primary, secondary, accent colors)
- Typography pairing (heading + body fonts)
- UX patterns for the product type

### Phase 2: Creative Direction

Apply frontend-design principles to elevate the design system:

| Design System Output | Creative Enhancement |
|---------------------|---------------------|
| Style: minimalism | Push to: refined luxury OR brutalist raw |
| Colors: soft pastels | Commit to: dominant color with sharp accent |
| Typography: professional | Replace with: distinctive characterful fonts |
| Layout: standard grid | Break with: asymmetry, overlap, diagonal flow |

**Creative Direction Questions:**
1. What's the ONE thing someone will remember about this UI?
2. What unexpected choice will make this feel "designed" not "generated"?
3. What visual atmosphere matches the product's soul?

### Phase 3: Implementation

Build the UI applying both:

**From ui-ux-pro-max (MUST HAVE):**
- Accessibility: 4.5:1 contrast, focus states, aria-labels
- Touch targets: minimum 44x44px
- Performance: transform/opacity animations only
- Layout: responsive breakpoints, no horizontal scroll

**From frontend-design (DIFFERENTIATE):**
- Typography: distinctive fonts, not Inter/Roboto/Arial
- Color: bold dominant colors, not safe neutrals
- Motion: one well-orchestrated animation, not scattered micro-interactions
- Composition: unexpected layout choices, intentional asymmetry

### Phase 4: Pre-Delivery Validation

Run validation using ui-ux-pro-max checklist:

**Visual Quality**
- [ ] No emojis as icons (use SVG: Lucide, Heroicons)
- [ ] Consistent icon set and sizing
- [ ] Hover states don't cause layout shift

**Interaction**
- [ ] All clickable elements have `cursor-pointer`
- [ ] Smooth transitions (150-300ms)
- [ ] Visible focus states for keyboard nav

**Accessibility**
- [ ] Color contrast 4.5:1 minimum
- [ ] Form inputs have labels
- [ ] Images have alt text

**Creative Direction (frontend-design)**
- [ ] No generic AI aesthetics (purple gradients, cookie-cutter layouts)
- [ ] Distinctive font choice (not system fonts)
- [ ] Memorable visual element or interaction
- [ ] Cohesive aesthetic point-of-view

## Quick Reference: When to Use Which Skill

| Task | Primary Skill | Secondary Skill |
|------|---------------|-----------------|
| New page/component | frontend-design | ui-ux-pro-max (validation) |
| Design system setup | ui-ux-pro-max | frontend-design (enhancement) |
| Accessibility audit | ui-ux-pro-max | - |
| Style refresh | frontend-design | ui-ux-pro-max (constraints) |
| Form/table heavy UI | ui-ux-pro-max | frontend-design (polish) |
| Landing page | frontend-design | ui-ux-pro-max (UX patterns) |
| Dashboard | ui-ux-pro-max | frontend-design (visual hierarchy) |
| Chart/data viz | ui-ux-pro-max | frontend-design (color/styling) |

## Anti-Patterns to Avoid

**Generic AI Output** (frontend-design warns against):
- Inter/Roboto/Arial fonts
- Purple gradients on white backgrounds
- Predictable grid layouts
- Same component patterns everywhere

**UX Violations** (ui-ux-pro-max warns against):
- Low contrast text
- Missing focus states
- Emojis as functional icons
- Transitions on width/height (use transform)
- No cursor-pointer on clickables

## Example Orchestration

**Request:** "Build a settings page for our SaaS dashboard"

**Phase 1 (ui-ux-pro-max):**
```bash
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "saas dashboard settings" --design-system
```
→ Gets: Style (clean minimal), Colors (neutral + accent), Typography (professional), UX patterns (grouped settings, toggles, save states)

**Phase 2 (frontend-design):**
- Tone: Refined industrial - precision meets warmth
- Differentiation: Subtle depth through layered cards with micro-shadows
- Typography: Replace generic with IBM Plex Mono for labels + Source Sans Pro for values
- Color: Dark sidebar with warm accent color for active states

**Phase 3 (Implementation):**
- Build with the creative direction
- Apply all UX patterns (grouped sections, clear labels, loading states)
- Ensure accessibility (contrast, focus, aria)

**Phase 4 (Validation):**
- Run pre-delivery checklist
- Verify no generic AI patterns leaked in
- Confirm distinctive design choices survived implementation
