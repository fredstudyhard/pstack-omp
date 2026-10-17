---
name: pstack-arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /skill:pstack-arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
---

# Arena

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); it governs tools, roles, authority, budgets and verification throughout this skill.

Open a todolist with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Choose available native roles suited to the artifact (`sage` for architecture, configured implementation roles for code). Use genuinely different approaches within approved budget and host delegation rules. Record actual identity for diversity claims. A required unavailable model-specific seat is BLOCKED, never silently substituted. If delegation is not allowed, compare local sketches without claiming independent evidence.
4. Give each candidate its own output location (a git worktree where possible, otherwise `/tmp/arena-<slug>/candidate-<n>/`), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Launch eligible candidates together using native `task` with one `tasks[]` entry per candidate and shared grounding in `context`. Put each candidate's owned output path, requirements and acceptance in its `task`; `solutionSpace` briefly describes the open design choices. Require the artifact and a short rationale naming considered and rejected alternatives.

For the local-sketch alternative selected in Phase A, make the contrasting sketches locally instead of dispatching candidates. Label them as one author's exploration, not independent attempts. Carry this local mode through every later phase; it does not authorize a review task that the host's delegation rules prohibit.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

In delegated mode, after all candidates finish writing, dispatch a fresh native `reviewer` with a read-only scope. Prefer independently evidenced model-family diversity when configured; a specifically required unavailable family blocks that gate. The judge sees the rubric and candidates by path label, scores each criterion, and recommends a base with rationale. It may run while the parent reads in Phase D. In local-sketch mode, the parent applies the rubric locally and records that no independent cross-judge ran. Any separately required independent review remains an unsatisfied gate until a qualified nonauthor can run.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel. In delegated mode compare with the cross-judge, investigate disagreement and read both rationales. In local mode choose from the local rubric assessment without reporting agreement, consensus or an independent verdict.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

When independently produced candidates converge on one shape, note that agreement; no graft is needed. Local sketches converging are only the author's design assessment. If candidates wildly diverge, Phase A may be under-specified: reframe within the approved finite budget or report the unresolved decision, rather than averaging the divergence or restarting indefinitely.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note naming the mode, base and why, any actual cross-judge verdict (or explicitly no independent judge in local mode), each graft and its source, what was rejected, dropouts, unresolved review gates and verification result.
