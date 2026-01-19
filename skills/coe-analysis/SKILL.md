---
name: coe-analysis
description: Root cause analysis using "5 Whys" technique after bugs or errors occur. Use when the user says "/coe-analysis", "why did this happen", "root cause", "what went wrong", "analyze this error", or after deployment failures, build errors, functional bugs, or mistakes made during development. Investigates the causal chain to find true root causes and propose preventive solutions.
---

# COE Analysis (Correction of Error)

Perform root cause analysis using the "5 Whys" technique to find the true cause of an error and prevent recurrence.

## When to Use

- After a bug, build failure, or deployment error
- When something unexpected happened during development
- When the same type of error keeps recurring
- To understand why a mistake was made

## Analysis Process

### 1. Identify the Problem

State the observable symptom clearly:
- What error message or behavior occurred?
- When and where did it happen?
- What was the expected vs actual outcome?

### 2. Perform 5 Whys Analysis

Ask "Why?" recursively to trace the causal chain:

```
Problem: [The observable error/bug]
    │
    └─ Why #1: Why did [problem] happen?
         Answer: [First-level cause]
         │
         └─ Why #2: Why did [first-level cause] happen?
              Answer: [Second-level cause]
              │
              └─ Why #3: Why did [second-level cause] happen?
                   Answer: [Third-level cause]
                   │
                   └─ Why #4: Why did [third-level cause] happen?
                        Answer: [Fourth-level cause]
                        │
                        └─ Why #5: Why did [fourth-level cause] happen?
                             Answer: [Root cause - usually process/knowledge gap]
```

Stop when you reach:
- A process gap (missing validation, checks, or workflow)
- A knowledge gap (missing documentation or context)
- A tooling gap (missing automation or guardrails)

### 3. Categorize Root Cause

Identify which layer failed:

| Layer | Examples | Solution Type |
|-------|----------|---------------|
| **Code** | Missing validation, wrong logic | Fix the code |
| **Tests** | Missing test coverage, wrong assertions | Add tests |
| **Types** | Missing type safety, wrong types | Add type checks |
| **Documentation** | Missing context in CLAUDE.md | Update docs |
| **Process** | Missing review step, unclear workflow | Update workflow |
| **Tooling** | Missing linter rule, no CI check | Add automation |

### 4. Propose Solutions

For each root cause, propose solutions at multiple layers:

**Immediate Fix**: Solve the current problem
**Preventive Measure**: Stop recurrence at the source
**Detection Improvement**: Catch similar issues earlier

## Output Format

```markdown
## COE Analysis: [Brief Problem Title]

### Problem Statement
[Clear description of what went wrong]

### 5 Whys Analysis

**Why #1**: Why did [X] happen?
→ Because [answer]

**Why #2**: Why did [answer from #1] happen?
→ Because [answer]

**Why #3**: Why did [answer from #2] happen?
→ Because [answer]

**Why #4**: Why did [answer from #3] happen?
→ Because [answer]

**Why #5**: Why did [answer from #4] happen?
→ Because [root cause]

### Root Cause
[The fundamental cause - usually a process, knowledge, or tooling gap]

### Solutions

#### Immediate Fix
- [What to do right now to fix the issue]

#### Preventive Measures
- [ ] [Action item 1 - e.g., "Add to CLAUDE.md: ..."]
- [ ] [Action item 2 - e.g., "Add validation in ..."]
- [ ] [Action item 3 - e.g., "Create test for ..."]

#### Detection Improvements
- [ ] [How to catch this earlier next time]
```

## Common Root Cause Patterns

| Pattern | Symptom | Typical Root Cause | Solution |
|---------|---------|-------------------|----------|
| Wrong assumption | Used incorrect value/approach | Missing context in CLAUDE.md | Document the constraint |
| Missed edge case | Works sometimes, fails others | Missing test coverage | Add test cases |
| Validation gap | Invalid data accepted | No input validation | Add validators |
| Type mismatch | Runtime type error | Missing TypeScript types | Add proper types |
| Stale knowledge | Used outdated API/pattern | Docs not updated | Update documentation |
| Missing dependency | Module not found | Incomplete setup | Document dependencies |

## After Analysis

1. Implement the immediate fix
2. Create tasks for preventive measures
3. Update relevant documentation (especially CLAUDE.md)
4. Consider if this pattern applies elsewhere in the codebase
