# Explicit complexity subflows

These subflows are read-only. Load only the requested section; remediation requires separate write intent. Correctness/security/performance review and final merge verdict remain with the configured review gate.

## Complexity-only diff review

Review the authorized diff for evidence-backed opportunities: `delete` (dead/speculative behavior with no current consumer), `stdlib` (named standard-library replacement), `native` (named platform/framework replacement), `yagni` (unneeded variation or configuration), or `shrink` (materially clearer equivalent).

For each finding include `important` or `suggestion`, exact file/line, current evidence, replacement, and behavior that must remain. Never flag required validation, safety, accessibility, observability, tests, migration support, readability, or a demonstrated extension point as unnecessary. End with estimated removable lines/dependencies and coverage gaps. If nothing material can be removed, say it is already lean; that is not correctness or merge acceptance.

## Bounded complexity audit

Establish repository/folder scope, exclusions, generated/vendor boundaries, and output cap. Use bounded inventory/search before opening large files; do not infer dead code from a missed text search. Rank the same finding categories by likely maintenance reduction. Include paths/lines, consumer/reference evidence, proposed replacement, and verification needed before deletion. Do not relabel correctness, security, performance, or style findings as complexity findings. Report estimated removable lines/dependencies and gaps, including when no material opportunity is found.

## Read-only shortcut ledger

Search only the authorized scope for language-appropriate comment prefixes followed by `ponytail:`. Exclude version-control metadata, dependencies, generated files, vendor trees, archives, binaries, and prose merely documenting the marker. This preserves the existing annotation format, not an external skill call.

Report `file:line — ceiling: ... — upgrade trigger: ...` for each marker. Missing or non-measurable triggers are `no-trigger`; do not guess owner, deadline, or upgrade path. Do not run blame unless requested. Default to chat output; persisting a ledger requires explicit intent and repository documentation policy. End with marker and no-trigger counts, or say no markers were found.

## Mode help

Explain only the selected mode, intensity, task-versus-conversation lifetime, and non-persistence from the entrypoint. Do not infer active persistent state from a comment, a prior process, or this reference being loaded.
