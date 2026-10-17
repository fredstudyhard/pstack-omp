# OMP port decisions

## Base and scope

The fork starts at Michael Denyer's `pstack-claude@5bd452955f8ded23ee81e022a19c537d6e523350` (0.9.90). Its original pstack pin is `cursor/plugins@99743e9c151c8537cbbf1f98bb38f34ef3368453`. Both identities are immutable provenance, not publisher authorization or a security verdict.

The original pin's API inventory has 54 skills, including 24 principles. This fork includes all 54, restores `make-bot-ui` as a native RPC authoring workflow, and retains ten selected-port additions. Every skill and all 23 playbooks are listed in `omp-capabilities.json`. A workflow is a procedure executed by the coding agent; it is not a new host tool or permission boundary.

## Base rationale

The selected base preserves broad workflow coverage, isolated writers, operator-controlled merge and revision-bound review. The fork retains those user functions while replacing foreign host mechanisms with native OMP primitives. The alternative OMP port is provenance-only reference, not copied implementation.

## Intentional differences

| Area | Native decision | Preserved user function |
| --- | --- | --- |
| Discovery | Native user skills only; every name prefixed `pstack-` | Explicit entrypoints and cross-skill routing without overriding existing skills |
| Models | Existing OMP roles/modelRoles; no model sheet | Role-appropriate workers and observable attribution |
| Delegation | Native task batches, actual task schema, isolated writers | Swarm coverage, competing designs and parent integration |
| Review | Fresh nonauthor reviewer; model-specific gate stays closed if unavailable | Independent pressure without false fallback verdicts |
| Verification | Native browser/terminal/API tools and project feature maps | Run the real surface, observe effects and retain proof |
| Long tasks | Native goal/todo, bounded supervised segments and checkpoint/resume | Continued progress, explicit limits and recoverability |
| Bot UI | OMP-owned bounded RPC interaction; localhost and approval gates | User-triggered agent control page, not Cursor-only Grok routines |
| History | Explicit named host URIs/files, no corpus mining | Relevant context and learning without unrelated private-session access |
| External operations | Existing target/identity/permission/budget gates | Authorized PR/release/integration workflows, never blanket authority |
| Cleanup | Read-only audit by default, no implicit network/history discovery | Evidence-based worktree decisions; no automatic deletion |
| Install/disable | Owned materialized native skills and content checks | Reversible loadability without deleting or moving protected .omp paths |
| Maintenance | Candidate upstream comparison and explicit review | Upstream improvements without automatic activation |

## Removed mechanisms, not removed workflows

Claude/Codex/Copilot plugin catalogs, model sheets/effort agents, routing hooks, Pi subagent/scheduler extension and its tests are not native features and are removed. Native equivalents replace their user function. Existing portable helper behavior tests and formal lock/watcher models are retained; obsolete wording/wiring tests are not repinned to the new prose.

No automatic global routing is installed. Enter `/skill:pstack-poteto-mode` explicitly. This keeps the original user's existing policy and skills authoritative and avoids a duplicate always-on instruction layer. In an active pstack task, routing and the full playbooks remain available.

## Limits are not hidden fallbacks

- A session-local URI is not durable across fresh OMP processes. Portable checkpoint files supply cold-session continuity.
- A foreground owner must exist for native RPC or supervised monitoring. No cloud wake/cron is installed.
- Prompt instructions are not an OS sandbox, permission grant or enforced server-side merge condition.
- A real provider, service, app or deployment requires its own applicable authorization and verification. Synthetic demonstrations do not certify those integrations.
- Unavailable required cross-family reviewers remain BLOCKED. Parent acceptance cannot be relabeled as their verdict.

Verification entrypoints and acceptance boundaries are documented in `omp-verification.md`; the capability catalog describes the shipped API, not internal evaluation verdicts.
