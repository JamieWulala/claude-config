---
name: doc-coauthoring
description: Structured workflow for collaborative document creation through Context Gathering, Refinement & Structure, and Reader Testing
triggers:
  - "write a doc"
  - "draft a proposal"
  - "create a spec"
  - "write up"
  - "PRD"
  - "design doc"
  - "decision doc"
  - "RFC"
---

# Doc Co-Authoring Workflow

A structured 3-stage workflow for creating high-quality documents collaboratively.

## When to Offer This Workflow

**Trigger conditions:**
- User mentions writing documentation ("write a doc", "draft a proposal", "create a spec")
- User mentions specific doc types (PRD, design doc, decision doc, RFC)
- User seems to be starting a substantial writing task

**Initial offer:** Explain the three-stage workflow and ask if they want to try it or prefer freeform:

> I can help you write this using a structured 3-stage workflow:
> 1. **Context Gathering**: You provide context while I ask clarifying questions
> 2. **Refinement & Structure**: We build each section through brainstorming and editing
> 3. **Reader Testing**: Test the doc with a fresh Claude (no context) to catch blind spots
>
> Want to try this workflow, or prefer to work freeform?

If user declines, work freeform. If they accept, proceed to Stage 1.

---

## Stage 1: Context Gathering

**Goal:** Close the gap between what the user knows and what Claude knows.

### Initial Questions
Ask for meta-context:
1. What type of document is this? (e.g., technical spec, decision doc, proposal)
2. Who's the primary audience?
3. What's the desired impact when someone reads this?
4. Is there a template or specific format to follow?
5. Any other constraints or context?

### Info Dumping
Encourage the user to dump all context:
- Background on the project/problem
- Related discussions or documents
- Why alternatives aren't being used
- Organizational context
- Timeline pressures
- Technical dependencies
- Stakeholder concerns

**During context gathering:**
- If user mentions files or docs, offer to read them
- Track what's learned and what's still unclear
- After substantial context, generate 5-10 numbered clarifying questions

**Exit condition:** Sufficient context when you can ask about edge cases and trade-offs without needing basics explained.

**Transition:** Ask if there's more context to provide, or if ready to move to drafting.

---

## Stage 2: Refinement & Structure

**Goal:** Build the document section by section through brainstorming, curation, and iterative refinement.

### Section Ordering

**If structure is clear:** Ask which section to start with (suggest starting with the one with most unknowns)

**If user doesn't know sections needed:** Suggest 3-5 appropriate sections based on doc type

**Once structure is agreed:** Create initial document with all section headers and placeholder text.

### For Each Section:

#### Step 1: Clarifying Questions
Ask 5-10 questions about what should be included based on context and section purpose.

#### Step 2: Brainstorming
Generate 5-20 numbered options of things that might be included:
- Context shared that might have been forgotten
- Angles or considerations not yet mentioned

#### Step 3: Curation
Ask which points to keep, remove, or combine:
- "Keep 1,4,7,9"
- "Remove 3 (duplicates 1)"
- "Combine 11 and 12"

#### Step 4: Gap Check
Ask if anything important is missing for this section.

#### Step 5: Drafting
Draft the section based on selections. Ask user to read and indicate what to change.

**Key instruction:** Instead of editing directly, have them indicate changes. This helps learn their style. For example: "Remove the X bullet" or "Make paragraph 3 more concise".

#### Step 6: Iterative Refinement
- Make edits using surgical changes (not reprinting whole doc)
- Continue until user is satisfied
- After 3 iterations with no substantial changes, ask if anything can be removed

**Repeat for all sections.**

### Near Completion

At 80%+ done, re-read entire document checking for:
- Flow and consistency
- Redundancy or contradictions
- Generic filler ("slop")
- Whether every sentence carries weight

---

## Stage 3: Reader Testing

**Goal:** Test the document with a fresh Claude (no context bleed) to verify it works for readers.

### With Sub-Agents (Claude Code)

**Step 1: Predict Reader Questions**
Generate 5-10 questions readers would realistically ask.

**Step 2: Test with Sub-Agent**
For each question, invoke a sub-agent with just the document content and question:

```
Use the Task tool to spawn a sub-agent with:
- Only the document content (no conversation context)
- The test question
- Instructions to answer based solely on the document
```

Summarize what Reader Claude got right/wrong.

**Step 3: Additional Checks**
Invoke sub-agent to check for:
- Ambiguity
- False assumptions
- Contradictions

**Step 4: Report and Fix**
If issues found, loop back to refinement for problematic sections.

### Without Sub-Agents

Provide manual testing instructions:
1. Open fresh Claude conversation
2. Paste/share the document
3. Ask the generated questions
4. Check if answers are correct

### Exit Condition
Reader Claude consistently answers correctly and doesn't surface new gaps.

---

## Final Review

When Reader Testing passes:
1. Recommend user do final read-through (they own the document)
2. Suggest double-checking facts, links, technical details
3. Ask to verify it achieves the desired impact

**Final tips:**
- Consider linking this conversation in an appendix
- Use appendices for depth without bloating main doc
- Update doc as real reader feedback arrives

---

## Tips for Effective Guidance

**Tone:** Direct and procedural. Explain rationale briefly.

**Handling Deviations:**
- User wants to skip: "Want to skip this and write freeform?"
- User frustrated: "This is taking longer than expected. Here's how we can move faster..."

**Context Management:** Address gaps as they come up, don't let them accumulate.

**Quality over Speed:** Each iteration should make meaningful improvements.
