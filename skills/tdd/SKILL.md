---
name: tdd
description: Test-Driven Development methodology. Use when implementing features with the RED-GREEN-REFACTOR cycle. Ensures tests are written before production code.
triggers:
  - tdd
  - test-driven
  - test first
  - red green refactor
  - failing test
---

# Test-Driven Development (TDD)

Systematic test-first development methodology following the RED-GREEN-REFACTOR cycle.

## The Iron Law

**Write the test first. Watch it fail. Write minimal code to pass.**

If you didn't watch the test fail, you don't know if it tests the right thing.

## Absolute Rule

No production code should exist without a failing test first. Any code written before tests must be deleted entirely—not kept as reference or adapted during test writing.

**Implement fresh from tests. Period.**

## The Three-Phase Cycle

### RED Phase
1. Write ONE minimal test demonstrating desired behavior
2. Use real code rather than mocks when possible
3. Run the test and **watch it fail**
4. Verify it fails for the RIGHT reason

### GREEN Phase
1. Write the SIMPLEST code necessary to pass
2. No over-engineering or feature creep
3. Resist adding "while I'm here" improvements
4. Code can be ugly—that's fine

### REFACTOR Phase
1. Clean up duplication
2. Improve names and structure
3. Ensure tests STILL pass after each change
4. No new functionality

## Why This Order Matters

Tests written after implementation pass immediately, proving nothing about actual functionality. Manual testing is inherently ad-hoc and unrepeatable. TDD provides systematic verification.

## Red Flags (Restart Required)

If you catch yourself saying:
- "I'll test after"
- "It's too simple to test"
- "I already manually tested"
- "Let me just get it working first"

**STOP. Delete the code. Start with a test.**

## Verification Checklist

Before completing work:
- [ ] Every new function has a test
- [ ] Each test failed initially for the RIGHT reason
- [ ] Minimal code was written to pass
- [ ] All tests pass cleanly
- [ ] Real code is tested, not mock behavior

## Example Cycle

```typescript
// RED: Write failing test
test('adds two numbers', () => {
  expect(add(2, 3)).toBe(5)
})
// Run: FAIL - add is not defined

// GREEN: Minimal implementation
function add(a: number, b: number): number {
  return a + b
}
// Run: PASS

// REFACTOR: (nothing needed for this simple case)
```

## Anti-Patterns

- **Test after**: Writing code first, then tests
- **Testing mocks**: Verifying mock behavior, not real code
- **Skipping RED**: Not seeing the test fail first
- **Over-engineering GREEN**: Adding extra functionality
- **Skipping REFACTOR**: Leaving messy code

## Related Skills

- **Test Master** - Comprehensive testing strategies
- **Playwright Expert** - E2E testing
