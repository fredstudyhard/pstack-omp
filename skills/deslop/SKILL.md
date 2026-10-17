---
name: pstack-deslop
description: Explicit behavior-preserving diff cleanup, or a separately selected simplification phase mode for code/config. Preserve complete scope, safety, UX, and verification; do not automatically audit governance prose.
---

# Deslop

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

## Select the mode

### Diff cleanup

For an explicit code-slop or diff-cleanup request, establish the authorized diff/base and owned paths from task or project context; do not assume a branch named main. Use the [code-slop lens](references/code-slop.md). Keep behavior unchanged. A discovered bug needs separate authorization for a behavioral fix; report it rather than silently expanding cleanup. Prefer focused edits, not a repository-wide style rewrite. Review-only requests do not authorize edits.

### Simplification phase mode

For an explicit simplest/minimal/YAGNI or simplification request, apply the ladder below. Task-local language such as “simplest solution” or “do less” applies only to the current task. An explicitly continuing mode lasts for this conversation until the user requests normal mode or stops simplification. Do not write mode state; a new process or conversation starts inactive unless the owning runtime explicitly configures persistence.

- `lite`: implement complete scope and mention one simpler alternative.
- `full`: enforce the ladder; default for an unqualified explicit simplification request.
- `ultra`: aggressively remove speculative implementation, never explicit requirements or completeness.

Workspace policy may invoke a one-boundary automatic gate before a code/config slice, before structural complexity, or after a non-trivial slice. It is not persistent mode, a mandate to shorten later answers, or authority for unrelated work. Do not automatically audit PRD, wiki, synthesis, governance, or handoff prose; UI/visual/brand exploration; or safety-critical security, privacy, auth, payment, migration, accessibility, public API, concurrency, persistence, compliance, or data-loss-prevention paths. For frontend work, settle design, accessibility, and visual verification first, then simplify implementation only.

## Simplification ladder

Stop at the first rung that fully meets the current requirement:

1. Omit speculative implementation not needed now.
2. Use a correct standard-library solution.
3. Use a native platform, browser, database, or framework feature.
4. Reuse an installed dependency when it adds no unacceptable risk.
5. Write a short clear implementation without hiding edge cases.
6. Otherwise build the minimum custom solution meeting the full contract.

Before adding a dependency, abstraction, interface, factory, adapter, configuration layer, wrapper, or file, state why earlier rungs do not satisfy the requirement. Prefer deletion and reuse, not line-count tricks at the expense of clarity or a demonstrated extension point.

## Non-negotiable boundaries

Neither mode may shrink requested scope, substitute a smaller feature, or waive safety, UX, or acceptance. Retain necessary validation, error handling, rollback, observability, tests, accessibility, security, privacy, auth, payment, migration, public API, concurrency, persistence, compliance, and data-loss prevention. Required verification remains proportional to risk and project policy; this workflow cannot cap it at one test or waive a gate. Similarly small options favor correctness and readability.

Do not label ordinary clean code as debt. Only a deliberately accepted shortcut with a real ceiling and measurable upgrade trigger merits a `ponytail: <ceiling>, <upgrade trigger>` comment under the existing marker convention. This is a code annotation, not a registry invocation or persistent mode setting.

## On-demand subflows and delivery

Load [complexity review, audit, and debt](references/complexity-subflows.md) only for those explicit requests. These are read-only and cannot supply final merge acceptance; the configured review gate retains that authority.

Keep routine cleanup summaries concise, normally 1–3 sentences, but report changed scope, observed checks, gaps, and blockers truthfully. Requested reports, rationale, and walkthroughs remain complete. Automatic gates do not change communication style. This workflow does not choose provider/model roles or invent new verification commands.
