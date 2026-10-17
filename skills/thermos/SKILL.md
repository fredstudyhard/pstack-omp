---
name: pstack-thermos
description: "Launch both thermo-nuclear review subagents in parallel, then synthesize their findings. Use for thermos, double thermo review, or combined bug/security and code-quality branch audits."
---

# Thermos

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

Run the two thermo review passes as async background subagents in parallel, then synthesize their results.

## Workflow

1. Determine the review scope from the user request, PR, current branch, or relevant changed files.
2. Gather the diff and any file/context excerpts needed for reviewers to evaluate the change without guessing.
3. Launch two eligible native `reviewer` tasks in one `tasks[]` batch, bounded by host delegation and budget rules:
   - Read [`../thermo-nuclear-review/SKILL.md`](../thermo-nuclear-review/SKILL.md) for bugs, breakages, security, devex and feature-gate leaks.
   - Read [`../thermo-nuclear-code-quality-review/SKILL.md`](../thermo-nuclear-code-quality-review/SKILL.md) for maintainability, structure, size, spaghetti and abstraction risks.
   Each scope is read-only and pins revision/base. A required unavailable independent model gate is BLOCKED; applying both lenses locally is not independent review.
4. Pass each subagent the same scoped diff/file context and ask it to return prioritized findings with file references and evidence.
5. After both finish, synthesize the results with findings first, deduplicated across reviewers. Weight overlapping findings more heavily, resolve disagreements with your own judgment, and keep summaries brief.

If individual background summaries are already visible to the user, do not restate them wholesale. Surface the unified verdict, the highest-signal findings, and any remaining uncertainty.
