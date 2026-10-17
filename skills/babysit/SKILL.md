---
name: pstack-babysit
description: Watch an explicitly authorized open PR, fix failing CI and agreed review findings, and stop at merge-ready within a bounded supervised OMP run.
---

# Babysit a PR

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); it governs tools, roles, authority, budgets and verification throughout this skill.

Use `gh` for authorized PR operations and native supervised process controls for bounded monitoring. Entering this skill does not authorize push, external comments, ready-state changes or merge.

Inside poteto-mode, the **Babysit** playbook ([`../poteto-mode/playbooks/babysit.md`](../poteto-mode/playbooks/babysit.md)) supersedes this skill: it owns mode declaration, the merge frontier, stack safety, and the `watch-pr` watcher. This skill stays the standalone `/skill:pstack-babysit` entry point for a single PR outside a poteto-mode run.

## When to use

- There's an open PR and the user explicitly wants it kept green, and you are not already inside a poteto-mode run (the playbook owns that case).
- The user invokes `/skill:pstack-babysit` directly.
- A subagent that opens a PR does NOT babysit — return to the parent and let the parent decide.

## Steps

1. **Fetch PR state.**

   ```bash
   gh pr view <number> --json number,title,state,mergeable,reviewDecision,statusCheckRollup,mergeStateStatus,comments,reviews
   ```

2. **Triage in priority order.**
   - Merge conflicts (`mergeStateStatus == DIRTY`): run `/skill:pstack-fix-merge-conflicts`. Rewriting history or force-push requires explicit approval; owning the branch alone is not permission.
   - Failing checks (`statusCheckRollup` entries with `conclusion: FAILURE`): run `/skill:pstack-fix-ci`. Root-cause and fix within scope; commit and push only under applicable authorization.
   - Review comments: run the **get-pr-comments** skill for the summary, then act only on feedback you actually agree with. When a comment has a single mechanical answer — a rename, a guard clause, a formatting nit — make the edit and quote the comment in the commit message. When it hinges on a judgement call, or you can't tell what's being asked, don't guess: leave it and reply with what you would have done.
   - Review-bot comments (Bugbot and similar automation): classify fix/dismiss/ask before acting, per [`bugbot-triage.md`](../poteto-mode/references/bugbot-triage.md). Ask by default on security, data, and high-severity findings.

3. **Monitor within bounds.** Before waiting, record an owner, deadline, maximum attempts and cancellation predicate. Use supervised native process handles; recheck active CI at a reasonable cadence (normally at least 60 seconds). Awaiting review can use 20–30 minute checks only within the approved segment. No detached loop, wake scheduler or idle keep-alive. When the deadline expires, checkpoint and stop.

4. **When to stop.**
   - Build is green, every comment resolved, branch merges cleanly → call it ready.
   - The approved correction/recheck budget or deadline is exhausted → summarize the unresolved state and checkpoint. The runtime contract's tighter limit wins.
   - A material product, authority or irreversible decision is required → use native `ask`; do not block on reversible implementation choices evidence can settle.

5. **Report.** Summarize fixes applied, comments addressed, comments deferred (with reason), current PR status. Cite each commit by SHA.

## Hard rules

- Don't rewrite history on a branch others may have pulled. If a rebase or force-push looks necessary, clear it with the user first.
- Don't tweak a test's expected values just to get a pass. Only change an assertion when the behaviour genuinely changed and the assertion was pinned to the old behaviour.
- Never skip hooks (`--no-verify`).
- Never bypass a failing check by marking it as not required.
- `gh pr ready` requires explicit authorization as well as green checks and no unresolved review comments. Merge is a separate authorized workflow.

## Cross-refs

- Opening a PR does not start a babysit; inside poteto-mode the Babysit playbook owns the request and starts only when asked.
- Use `interrogate` before opening if the diff is contested; once open, babysit takes over.
- Use `unslop` on any prose you write here (PR comments, commit messages, status reports).

## Provenance

Adapted from Michael Denyer's independently authored pstack workflow, informed by Cursor's public babysit behavior, not Cursor's closed-source implementation. The native OMP port retains PR triage and readiness semantics while replacing runtime scheduling.
