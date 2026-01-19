# Workflow Patterns

Use these patterns when skills need to guide Claude through multi-step processes.

## Sequential Workflows

For tasks with ordered steps, provide a clear progression:

```markdown
## PDF Form Filling Workflow

1. **Analyze the form** - Run `scripts/analyze_form.py` to identify fields
2. **Extract field info** - Run `scripts/extract_fields.py` for field details
3. **Prepare data** - Map user data to form fields
4. **Fill the form** - Run `scripts/fill_form.py` with mapped data
5. **Verify output** - Run `scripts/verify_output.py` to check results
```

Providing an overview helps Claude understand the complete progression before starting.

## Conditional Workflows

For tasks requiring decisions, guide Claude through branching logic:

```markdown
## Content Workflow

**First, determine the task type:**

### Creating new content?
1. Gather requirements from user
2. Create outline
3. Draft content
4. Review and refine

### Editing existing content?
1. Read the existing document
2. Identify changes needed
3. Apply edits
4. Verify formatting preserved
```

Present decision points first, then offer separate instruction sets for each path.

## Key Principles

- Make workflows explicit and structured
- Use either linear progression or clear conditional branches
- Help Claude understand the full scope before executing
