#!/usr/bin/env python3
"""
Quick Skill Validator - Validates skill directory structure and SKILL.md format

Usage:
    quick_validate.py <skill-directory>

Example:
    quick_validate.py .claude/skills/my-skill
"""

import sys
import re
from pathlib import Path


ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}


def validate_skill(skill_path):
    """
    Validate a skill directory.

    Args:
        skill_path: Path to the skill folder

    Returns:
        Tuple of (is_valid: bool, message: str)
    """
    skill_path = Path(skill_path).resolve()

    # Check directory exists
    if not skill_path.exists():
        return False, f"Skill directory not found: {skill_path}"

    if not skill_path.is_dir():
        return False, f"Path is not a directory: {skill_path}"

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, f"SKILL.md not found in {skill_path}"

    # Read and validate SKILL.md
    try:
        content = skill_md.read_text()
    except Exception as e:
        return False, f"Error reading SKILL.md: {e}"

    # Check for YAML frontmatter
    if not content.startswith('---'):
        return False, "SKILL.md must start with YAML frontmatter (---)"

    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, "SKILL.md must have closing --- for YAML frontmatter"

    frontmatter = parts[1].strip()

    # Parse frontmatter manually (simple YAML parsing)
    properties = {}
    for line in frontmatter.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            properties[key.strip()] = value.strip()

    # Check required fields
    if 'name' not in properties:
        return False, "SKILL.md frontmatter must include 'name' field"

    if 'description' not in properties:
        return False, "SKILL.md frontmatter must include 'description' field"

    # Validate name format
    name = properties['name']

    if len(name) > 64:
        return False, f"Skill name must be 64 characters or less (got {len(name)})"

    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name):
        return False, "Skill name must be hyphen-case (lowercase letters, digits, hyphens only, no leading/trailing/consecutive hyphens)"

    # Validate description
    description = properties['description']

    if len(description) > 1024:
        return False, f"Description must be 1024 characters or less (got {len(description)})"

    if '<' in description or '>' in description:
        return False, "Description must not contain angle brackets"

    # Check for disallowed properties
    for key in properties:
        if key not in ALLOWED_PROPERTIES:
            return False, f"Unknown property in frontmatter: '{key}'. Allowed: {ALLOWED_PROPERTIES}"

    # Check that name matches directory name
    if name != skill_path.name:
        return False, f"Skill name '{name}' must match directory name '{skill_path.name}'"

    return True, f"Skill '{name}' is valid"


def main():
    if len(sys.argv) < 2:
        print("Usage: quick_validate.py <skill-directory>")
        print("\nExample:")
        print("  quick_validate.py .claude/skills/my-skill")
        sys.exit(1)

    skill_path = sys.argv[1]

    print(f"Validating skill: {skill_path}\n")

    valid, message = validate_skill(skill_path)

    if valid:
        print(f"VALID: {message}")
        sys.exit(0)
    else:
        print(f"INVALID: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
