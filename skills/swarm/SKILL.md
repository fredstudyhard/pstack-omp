---
name: pstack-swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /skill:pstack-swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
---

# Swarm

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Select configured native roles for each slice (`scout` for discovery, `reviewer` for read-only audit, implementation roles for code). Host configuration owns model and effort. For a model race, require actual identity evidence and fail the requested family gate closed when unavailable. Budget and host delegation rules bound the fan-out; process remaining slices sequentially when needed.
4. Give each writer an isolated worktree or output directory and name the integration owner. Verification/measurement briefs pin exact SHAs, method, sample count, sample definition and order. Only explicitly authorized measurement workers run checks before integration.

## Phase B: Fan out

Launch eligible workers in one native `task` batch with `tasks: [{task, solutionSpace, name?, agent?}]` and shared `context`. Use only configured role names; omit `agent` for the default worker. Put owned paths, scope and acceptance in each `task`; `solutionSpace` briefly describes implementation freedom. Native tasks already run in the background; isolation comes from the assigned worktree/output directory.

When a worker must start from a non-default branch, check that branch out in the worker's own worktree and name the worktree path in its brief.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
