### Opening a PR

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md).

**Enter only when PR creation is requested or covered by existing explicit authorization.** A read-only investigation, completed local change or desire for CI does not grant publication, push or merge authority. If unauthorized, return local work and evidence without a PR.

**Worktree.** Preserve the current checkout and unrelated changes. Use an authorized clean worktree based on the intended revision, not an assumed default branch. Concurrent writers each need an exclusive worktree/output and recorded base. Native `task` has no isolation parameter. Never reset hard, patch out someone else's work, force-remove a worktree or move/delete `.omp` to get clean state. Establish that owned writers have stopped or released the shipping tree through actual native controls and captured ownership. Unknown ownership is a gate, not a reason to stop unrelated agents. Integrate completed outputs, then inspect the task-scoped diff and tree to be published.

**Commits.** Within authority, stage explicit task files and shape small ordered, independently understandable commits. Amend only task-owned unpublished work when appropriate; shared-history rewrite requires its own authority and lease/safety protocol. Bodies do not repeat the subject. No automatic commit/push is implied by entering this playbook.

**Prose passes.** Apply `/skill:pstack-deslop` before commit and `/skill:pstack-no-comments` before review. Use `/skill:pstack-technical-writing` for title, description and commit body, except Diátaxis classification; apply its controlled vocabulary and `/skill:pstack-unslop`.

**Titles.** Use Conventional Commits `type(scope): subject`, no trailing period. Choose feat, fix, docs, refactor, test, chore or perf, a real area scope and a short imperative subject naming a useful symbol when it carries the change.

**Description.** A one-minute briefing, not a lab notebook. Keep the resulting squash body roughly under 40 lines. Use these `##` headings in order, omitting empty optional sections.

- `## Why`: problem and approach in 1–3 sentences, no SHA genealogy.
- `## What changed`: 1–3 short bullets; name both sides of a rename/retarget.
- `## Scope`: always, 1–3 items on included and intentionally excluded behavior, not a file inventory.
- `## Tradeoffs`: genuine rejected alternatives only.
- `## Blast Radius`: affected users/systems and the concrete safety/risk, including existing red-base cost when relevant.
- `## Verification`: 1–3 actual run paths and outcomes. For perf give one primary before/after number with unit and linked method/artifact. Mark NOT_RUN/BLOCKED honestly.

Attach authorized screenshots/video when they prove a claim. Keep full SHAs, per-lane receipts and long checklists in linked named evidence artifacts, not prose verdict theater. Never upload secrets, raw private transcripts or unrelated evidence.

**Forge.** Verify repository, identity and target before external writes. GitHub CLI `gh` is the default. If installed `origin` can resolve this repository under the approved identity, use `origin pr` consistently; otherwise retain `gh` and record the fallback. Do not activate another account or require Graphite. If the host actually provides an applicable PR tool, use it for supported creation/edit/ready operations and the selected forge for uncovered reads/actions, respecting its real schema. Do not invent a built-in PR tool.

**Size and stacks.** Prefer narrow verifiable units, not arbitrary fragmentation. Independent work branches from trunk. A dependent child branches from the parent's exact recorded tip and targets its parent branch. Under the selected authorized forge, create with `gh pr create --base <parent-branch>` or `origin pr create --status open --base <parent-branch>`. The topology owner alone retargets/rebases; [Shipping](shipping.md) owns post-parent-merge restacking, cancellation and leases. No automatic rebase or force-push occurs just to open a PR.

**Readiness.** Open ready rather than draft when requested delivery and all applicable review gates allow it. Use an actual PR tool's supported `draft: false`, `gh` without `--draft`, or Origin `--status open`. If a required independent verdict is unavailable, report BLOCKED and do not represent the change as merge-ready; do not manufacture approval or quietly weaken the gate. Read back created PR status and URL before reporting it. Convert draft to ready only under the applicable grant and current evidence.

**Babysit.** Creating a PR does not start babysitting or merging. Report the URL and continue assigned build work. Start [Babysit](babysit.md) only when requested or explicitly included in the existing owner lifecycle. A delegated owner returns its URL and receipts to the parent; an Autopilot owner may perform its expressly assigned finite babysit. Contested design uses `/skill:pstack-interrogate`, never an implicit provider substitute.

**Reply:** actual PR URL and read-back state, scope, evidence, independent-review status and any remaining operator gate. If publication was not authorized, report the local artifact instead.
