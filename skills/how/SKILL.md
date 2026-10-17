---
name: pstack-how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
---

# How

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); it governs tools, roles, authority, budgets and verification throughout this skill.

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

For eligible independent exploration slices use native `task` with configured `scout` roles and explicit read-only scope. Use `sage` for architectural explanation when warranted; otherwise explain locally. Put scope, owned paths and acceptance in each `task`, concise design freedom in `solutionSpace`, and shared evidence in `context`. Model/effort stay host-owned. Do not claim model diversity without transcript evidence or replace an unavailable required reviewer.

## 1. Assess complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): explore and explain locally using `references/explainer-prompt.md`, without an explorer-findings section. Do not spawn a delegate for this one bounded question. Go to step 4.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): go to step 2.

When in doubt, take the simple path.

## 2. Explore (complex only)

Decompose the question into 2 to 4 angles, each a distinct slice of the subsystem. Spawn all explorers in a single message, each with `references/explorer-prompt.md` and its angle filled in.

## 3. Synthesize (complex only)

Once all explorers have returned, read their evidence and synthesize locally using `references/explainer-prompt.md`. Verify accepted findings against the source; do not launch a separate delegate merely to combine summaries.

## 4. Present

Present the parent-owned explanation, preserving evidence and uncertainty. Do not pass through worker completion claims or an unverified explanation.

## Output format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
