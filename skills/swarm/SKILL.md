---
name: pstack-swarm
description: Coordinate explicit bounded team work with parent-owned decomposition, isolated workers, integration, and project-defined acceptance. Supports coverage, races, gauntlets, and exploration without default fan-out for routine work.
---

# Swarm

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

## Activation and project ownership

Use for an explicit team-workflow, swarm, or parallel-work request, not ordinary single-agent work. Host delegation policy, configured roles, model/effort routing, and authorization remain authoritative. This contract grants no additional tools or provider access.

Read applicable repository routing and classify the work as source-only or requiring execution, verification, or resource lifecycle operations. For the latter, locate the project execution contract: a task packet, adapter, runner, or explicit combination. Missing required mechanics mean blocked, not reconstructed commands from memory. Source-only work needs no mechanical runner unless repository policy requires one.

Repository instructions own domain/routing constraints. Project contracts own scope, dependencies, acceptance, stop conditions, commands, fixtures, evidence destinations, deadlines, retention, and lifecycle. Adapters/runners implement those mechanics. If instructions and runner disagree on a required gate, stop for contract repair rather than choosing the easier result. Do not create a second task-state system or impose a universal worktree, packet, artifact, or report schema.

## Parent and worker authority

The parent alone interprets the objective, defines the task graph and independent seams, assigns paths/inputs/outputs, approves the plan, integrates results, resolves conflicts, runs or commissions project-defined verification, and decides final complete/incomplete/blocked status.

Workers stay within explicit ownership and return inspectable changes or findings, evidence, blockers, and unverified scope. They may not expand scope, declare whole-task acceptance, deploy, mutate remote providers, or enable automatic merge. Worker-reported evidence is not parent acceptance until checked against the project contract and user-relevant path.

Parallelize only genuinely independent bounded slices. Serialize shared files/interfaces, migrations, deployment, shared configuration, and integration boundaries without an explicit contract. Isolate writers with explicit disjoint ownership and, when needed, separate worktrees or output directories. Never allow overlapping writes to shared state. Unknown shared state, secrets, irreversible effects, and unclear ownership require the project's serial or approval path.

## Lifecycle

1. **Plan:** establish objective, done predicate, graph/dependencies, independent slices, ownership, handoff shape, and slice acceptance. Keep existing project task tracking. Routine clear work needs no reviewer. For material ambiguity/risk or explicit adversarial plan review, load [bounded plan challenge](references/plan-challenge.md).
2. **Contract:** confirm routing and any required execution/lifecycle contract. Choose a coverage/race recipe only when needed from [execution recipes](references/execution-recipes.md).
3. **Execute:** use eligible configured native workers within host limits. Give each a standalone brief: goal, inputs, owned paths, dependencies, allowed side effects, implementation freedom, acceptance, verification authority, deadline/stop conditions, and expected handoff. No hidden background activity.
4. **Handoff:** collect inspectable changes/findings, verification tier and evidence, blockers, unverified scope, and residual resources. Missing or dropped required work remains a gap.
5. **Integrate:** parent resolves conflicts and checks cross-slice boundaries. Material scope, dependency, acceptance, or side-effect changes pause affected work for a parent decision.
6. **Verify:** parent follows the project's user path, tests, smoke, or other acceptance surface after integration. Only explicitly assigned measurement/verification workers run checks before integration. Do not replace acceptance with worker self-report or model agreement.
7. **Close:** perform project-defined lifecycle cleanup and report residual/unverified state. Preserve explicit deadlines and stop conditions; no unbounded polling, retries, cron, idle sockets, background jobs, or automatic reruns.

## Acceptance and reporting

Local work is the default boundary. Remote API/provider mutations, remote migrations, deployment, push, and automatic merge require separate explicit authorization/workflows. A local draft is not a published work order.

Return one consolidated report rather than worker dumps. Separate observed outcomes from inference, identify the exercised project verification path and project-selected artifacts, and classify evidence as `parent-verified`, `worker-reported`, `blocked`, or `unverified` where relevant. Preserve limitations and residual state.

- **Complete:** parent integration plus required verification and lifecycle checks passed.
- **Partial:** bounded work finished but a required verification/lifecycle boundary remains unverified.
- **Failed:** an executed required slice, integration boundary, or gate failed.
- **Blocked:** required contract, prerequisite, authority, or dependency is unavailable.

A failed gate or missing evidence cannot become success by reinterpretation. One successful project run proves neither cross-project portability, production readiness, nor automatic-routing correctness.
