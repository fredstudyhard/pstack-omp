---
name: pstack-setup-pstack
description: "Read-only OMP setup and capability diagnosis for pstack skill discovery, configured roles and real-surface verification. Use for setup pstack or configure pstack models; does not mutate configuration."
---

# Setup pstack

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

This is a read-only doctor, not a model registry or installer. OMP owns model routing, effort, provider credentials and skill discovery. Do not create override sheets, change presets, install hooks, activate providers or edit user configuration.

## Diagnose

1. Identify the current host and actual tool schema. Record the OMP version if exposed; otherwise mark it unknown rather than inferring it from this bundle.
2. Read the installed fork's README for the supported native installation procedure. Inspect the current skill registry or concrete installed files to establish whether `pstack-poteto-mode` and the requested leaf are discoverable. A source file alone is not proof of runtime registration. Distinguish project `.omp/skills/` from user `~/.omp/agent/skills/` installation and follow its repository canonical source.
3. Inspect only the host-exposed configured role inventory needed for this task: implementation, scout, reviewer, sage, designer, and council roles when requested. Report actual available roles and unknowns; do not probe providers with billed calls. A role name does not prove a model family. Required independent family review stays BLOCKED without actual transcript attribution and no fallback.
4. Check that native task, read/edit/write, ask/todo and relevant real-surface tools exist. Never invent a foreign tool or unsupported parameter. Explain precisely which requested workflow is blocked by a missing capability.
5. Locate the actual project verification skill or documented app harness. If absent, offer `/skill:pstack-create-verification-skill` once. Do not generate or run one merely as a setup side effect.
6. For a proposed multi-agent run, identify cost drivers and agree a finite observable dispatch/usage ceiling, deadline and stop conditions before billed work. Smaller scope and fewer reviewers reduce cost without changing provider configuration.

## Guidance, not mutation

Give the exact repository-documented installation or host configuration step for a missing prerequisite only after reading its source. If the supported host procedure is unavailable, report that prerequisite rather than guessing CLI flags. Any later install or configuration change is a separate, explicitly authorized task. Preserve existing user state and never delete or move `.omp` paths as cleanup.

## Report

Return a compact table: capability, observed evidence, PASS / FAIL / BLOCKED / NOT_RUN, and next action. Include discovery scope, role attribution limitations, verification-harness status and any required independent review gate. Never report an unrun capability as passing.

For a ready installation, offer one concrete `/skill:pstack-poteto-mode <goal and acceptance>` prompt. This doctor does not start the task.
