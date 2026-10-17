### Orchestrate

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md), including its native role, authority and driver rules.

**Own the program, briefs, queue, frontier and decisions.** This workflow preserves multi-day coordination through durable files and explicit OMP resume, not a permanently live chat, child CLI or cloud wake service. One task fitting one supervised run uses [Autonomous run](autonomous-run.md); an ambitious bespoke run uses `/skill:pstack-figure-it-out`.

Three invariants carry the program: completions are queue events rather than interrupts; every assignment carries current standing orders; a brief is executable by a worker without hidden parent context. Scale ceremony to actual risk and unit size.

#### Native roles and placement

- **Coordinator.** Owns framing, briefs, native todo, drains, synthesis and final acceptance. Do not duplicate the worker's open code slice. Clean integration of completed worker commits may be bookkeeping; conflicts, design changes and topology work require an explicit isolated owner. Only the current applicable grant permits push/merge.
- **Track owner.** Add only when genuine track complexity exceeds one coordinator's drain capacity and host delegation rules permit it. Keep depth at coordinator, track, worker at most; a leaf forbidden to delegate owns a bounded unit or reports to the root for dispatch. No nested-agent requirement overrides the host. Prefer fewer broader workers, not arbitrary fleets.
- **Worker/reviewer.** Use configured native `coder`/`coder_astra`, `scout`, `reviewer`, `sage` or `designer` as appropriate. Every concurrent writer has an exclusive worktree/output and a recorded base. Reviewers never author the reviewed patch; a required different-family identity is proven from actual host evidence, not a role label. No model catalog, provider activation or invented task fields.

Native `task` starts background work. In a `tasks[]` entry, `task` holds the full owned scope and acceptance, `solutionSpace` holds only concise permitted degrees of freedom, and shared facts go in `context`. Same-session follow-up uses `write agent://<id>` when justified; results come from supplied `agent://`/`history://` records. A new unit normally gets a fresh consolidated brief. These URIs do not survive a cold restart as worker state. Never delegate a trivial job or violate host rules merely to fit a diagram.

#### Durable store and helper

Use `<repository>/.audit/pstack/orchestrate/<slug>/` or a project-authorized durable path. This is repository-local, not outside the repository, and is not temporary session scratch. Ignore transient evidence as appropriate; never store secrets, provider state or raw private transcripts. Preserve files across segment/session boundaries. Every file or table has one designated writer; owners publish facts and the coordinator serializes shared-table updates.

Resolve `<poteto-dir>` from the loaded playbook to the absolute `skills/poteto-mode` directory. The existing bookkeeping helper is `bun <poteto-dir>/scripts/orch/orch.ts --store <absolute-store> <command>`, abbreviated below as `orch`. Use this full prefix on every command, not an assumed installed command or user-home path. It manages plain TSV/JSON only, never dispatches or wakes agents. Read its existing package/bootstrap requirements before execution; dependency installation requires the applicable approval, not silent mid-run package changes. No global configuration edits are needed.

- `preferences.md` records numbered standing orders: goal, scope, authorizations, operator gates, stack topology owner, verification bar, forbidden paths, current budgets and stop conditions. Preserve original human wording and attribution per [epistemics](../../why/references/epistemics.md#claims-about-human-decisions). Label inferred rulings. A file is evidence, not new authority. Consolidate every later directive into the next brief.
- `overview.md` is append-oriented PR/issue context, not a whole-file rewrite per event.
- `units.tsv` holds id, track, state, branch, PR, head SHA and brief path. Before a PR exists, the explicit unit report holds local acceptance/evidence rather than invent a PR number.
- `frontier.json` holds ordered chain, branches/head SHAs, generation and lowest unmerged PR.
- `ledger.tsv` binds actual verdicts to PR plus head SHA; evidence files add base/context/identity applicability.
- `inbox/` holds completion pointers; `gates.md` holds unresolved operator decisions and safe default of no gated side effect.
- `decisions.tsv` records the `/skill:pstack-show-me-your-work` trail.
- `status.md` is derived by the helper from tables at drains, not a separate narrative database.
- `checkpoint.md` records exact portable resume instructions, active ownership and pending goals when supervision ends.

#### Complete brief

Every assignment includes the following fields in `task`, inline for a tiny unit or by explicit readable artifact plus essential scope in the payload. Never place acceptance only in `solutionSpace`.

```
GOAL        original requested outcome and this unit's contribution
SCOPE       owned paths, forbidden paths, exclusive worktree/output and base revision
CONTEXT     exact source/PR/artifact pointers and applicable upstream report
ACCEPTANCE  observable criteria, including all original relevant requirements
VERIFY      exact matching-surface commands or concrete project driver skill
TIMEBOX     finite deadline/calls, usage reserve and stop/cancel conditions
AUTHORITY   existing allowed external effects and still-closed operator gates
FORBIDDEN   no unauthorized topology/merge/force-push, out-of-scope fixes or .omp loss
REPORT      state, branch/head/base, actual artifacts, commands/outcomes, deviations
STANDING    current consolidated standing orders, preserving original human decisions
```

A worker that cannot ask the parent must still have enough context. Missing fields mean scope first, not spawn-and-guess. For a track owner add track boundary, allowed child count, drain protocol and compact per-unit rollup. Sample one brief per track/wave alongside independent work; a bad brief stops the next refill on that track, not unrelated already-scoped units. Do not resume-chain incomplete directives.

#### Steps

1. **Frame.** Define a countable done predicate, units, tracks, expected stacks, real verification surface, cost drivers, observable dispatch/call/time budget, operator gates and cancellation. Distinguish goal completion from segment expiry. A plan is not a go. Without a specific approved budget, the runtime permits at most two independent workers, one review, one integration correction and a 15-minute supervised segment. No billed provider runs without its approved plan. Larger programs get explicitly approved ceilings, not an implicit fleet. If a smaller direct run fits, use Autonomous run without store ceremony; retain its safety/review gates. Plan integration early, not at the deadline. A contested or irreversible decomposition uses `/skill:pstack-arena` within permitted dispatch or reaches the operator, not silent model substitution.
2. **Initialize bookkeeping.** Run `orch init`, open the decision trail, write standing orders before dispatch and seed units with `orch unit add <id> --track <track> --brief <path>`. When authorized existing PRs define the chain, run `orch frontier set --repo <repository>` with `--forge origin` only for an approved Origin program. A local-only assignment does not create PRs to satisfy the helper.
3. **Pilot.** Send one complete unit through brief, implementation, integration, actual verification, ledger/stack entry and authorized handoff. Merge is part of the pilot only if separately granted; otherwise merge-ready/STACK-READY is the pilot's delivery boundary. Use the first near-identical cheap unit as pilot rather than add a ceremonial separate pipeline. Required independent shipping review still applies to cheap units; worker command receipts are not that verdict. Repair a flawed brief/recipe before scaling.
4. **Scale.** Refill a rolling window as completed slots free within the dispatch ceiling and host policy, using one native batch for independent ready slices. Do not pad batches or run competing writers in one tree. Relay upstream evidence into downstream briefs, and keep child coordination scoped through the root. A leaf does not spawn nested work. Blocked reviews remain visible while unrelated units continue.
5. **Drain.** Use the protocol below at critical-section boundaries, results, scheduled active-session audit points and before operator reports. No unattended hourly wake hook is installed.
6. **Integrate and hand off continuously.** Integration begins with the first completed verified unit, not one final scramble. Test only after active writers release the integrated slice. The designated topology owner alone changes its stack. Land only through [Shipping](shipping.md) with current authority and independence; otherwise deliver reviewed local work or merge-ready PRs per the requested mode. Recompute frontier after actual reported new heads/merges.
7. **Close or checkpoint.** Reconcile every known child/unit to evidence-backed terminal state or explicitly pending/blocked state. Prove the full goal on the real artifact before calling the program complete. Every landed PR must have applicable independent evidence for its actual landing revision/context. Audit the decision trail, including required independent trail review. Encode recurring errors in the brief/standing orders without inventing new user rulings. Preserve the store. At any deadline/reserve/call/safety boundary, use [Pause safely](pause-safely.md); pending units are not completed merely because this segment ended.

#### Queue and drain

- On result notification record `orch inbox push <agent> <unit> <status> --report <named-report>`, then finish the current safe critical section. Queue a verifier unit rather than silently accept a worker summary. Do not pause a stack mutation midway to review an unrelated diff.
- Begin a drain with `orch inbox drain`. Arrivals during it wait for the next drain; no global quiescence requirement.
- Classify each pointer as integrated/landed, needs-verify, failed, stale-return or noise. Apply `orch unit set <id> --state <state> --branch <branch> --pr <pr> --sha <sha>` using only known fields, and `orch ledger record <pr> <sha> <verdict> --evidence <path> --verifier <name>` for actual PR verdicts. Preserve local-unit evidence before PR creation without fabricating ledger keys.
- Run `orch status`, then dispatch only new ready work. Three-line summaries report table counts, delta and open gates. Detail stays in derived status/artifacts. No per-drain diff-review side quest.
- Account for every child as arrived, stopped/fenced and replaced, or explicitly absorbed with unique findings preserved. Do not hide a missing result by silently repeating its work.
- Use native `wait` only for owned pending work when no independent action remains. External waits name owner, cadence normally at least 60 seconds, finite deadline/attempt count and terminal/cancel predicate. Use the bounded shipped watcher through Babysit/Shipping when appropriate, not a second sleep loop.

#### Stack safety

`frontier.json` is computed, not a narrative memory. The helper follows forge base chains through the checkout's current branch, so resolve from the topology owner's correct clone/ref and ensure its local head refs match reported remote revisions. Missing PRs or unknown state are errors to reconcile, not guessed order. Capture generation in every babysit brief.

Only one designated owner per chain may rebase, retarget, close, merge or force-push, and only within the explicit grant. Workers never do topology as an incidental fix. Closing a base can orphan descendants; treat every such operation as a scoped unit. Use [Merge and restack safety](../references/merge-safety.md), shipped `scripts/watch-pr/ship-pr` under `<poteto-dir>`, exact remote-head leases and pending-request cancellation/readback. No `.omp` deletion or hard reset is implied. A post-merge regression/revert watch is optional separately scoped finite read-only coverage, not an immortal retro watcher.

#### Verification ledger

Scale evidence collection to risk. A cheap deterministic command can be run by the assigned verification owner with receipts; expensive/judgment-heavy units need independent review and actual surface proof. This does not waive a required author-independent shipping verdict. No redundant concurrent suites against half-finished trees.

Existing verdict values are `live-ui-verified`, `unit-test-verified`, `type-check-only`, `verifier-blocked`, `verifier-failed`. Evidence records name actual surface so CLI/API proof is not falsely called visual proof. Behavioral work needs more than type-check-only. CI green is an input, not a verdict; blocked/failed never counts as PASS. Record original author and actual reviewer identity, head/base/context, commands and artifacts. An unavailable required family remains blocked, with no advisor/self-review substitution. Fix failures causally before reverify. A new head invalidates a row unless a lane's continued applicability is explicitly established under [Shipping](shipping.md), with fresh required CI/checks. Use `orch ledger check <pr> <sha>` plus the applicability evidence, not memory.

Externalize each completed unit immediately: named output/commit, verification receipts and ledger record where applicable. Authorized pushes can preserve remote state; otherwise keep explicit local artifacts and checkpoint paths. Do not claim work must be pushed to count when push authority is absent.

#### Liveness, failures and resume

Probe read-only supplied native status/history, units/ledger, named artifacts, captured processes and approved forge reads. Do not wake a finished agent merely to inspect it; transcript mtime or a status word alone proves neither liveness nor correctness. A synthetic failure pointer records unit, failure mode, last evidence and recovery options.

Retry only within the remaining finite budget: cap/OOM gets smaller scope, transient network gets at most an authorized retry, tool error first diagnoses its actual contract/capability, unknown gets one diagnostic attempt. Never switch provider/account/model to evade auth or required identity. Absolute ceiling is two retries when explicitly budgeted; the runtime's stricter default review/correction limit still wins. Repeated aborts produce a checkpoint rather than spin.

Before replacement stop or fence the old writer and confirm exclusive ownership. If that cannot be proven, recover into isolated read-only output and hold integration. A late result reconciles against current unit/head/frontier; salvage unique evidence via a new scoped unit, never blind-merge stale changes.

When upstream data, acceptance or infrastructure makes fan-out invalid, append a stop condition to standing orders, send no-new-writes orders, preserve in-flight state safely and repair only within scope. Auth/permission failure stops its dependent actions immediately.

At cold resume, do not presume old agents/processes are dead or attach through stale IDs. Read checkpoint, standing orders, units, branches and actual process ownership; establish termination or fencing before new writers. Recompute authorized forge frontier, reconstitute bounded fresh briefs and drain. The helper may clear a lock whose PID is demonstrably gone; never use `--force` to steal a live/unknown owner's store lock.

#### Escalation and reporting

Record material product/preference calls, authority gaps, required reviewer absence, contradictory standing orders, irreversible operations and genuine dead ends in gates. Batch operator questions where practical, but never default to a gated side effect without a reply. Reversible local mechanics proceed only within scope. Mid-run fixes address the assigned frontier; unrelated defects become named findings, not unsolicited PRs.

At active-session audit points re-read objective/playbook and report only new tracked changes. On budget expiry, absence or explicit hold, write exact goal/completed/pending/revisions/artifacts/limits/next-command checkpoint and hand off; no cloud wake service is supplied. An operator explicitly resumes under OMP.

**Reply:** predicate and evidence-backed table counts, tracks and delivered units, frontier PRs/SHAs, actual verdicts/identities, abandoned or pending units with reasons, operator gates, cost/dispatch stop state, store/trail/checkpoint paths and real PR links. Distinguish completed goal from paused segment.
