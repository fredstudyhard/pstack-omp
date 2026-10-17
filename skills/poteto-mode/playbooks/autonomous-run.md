### Autonomous run

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md).

**Own the exit predicate and supervised continuation.** This is finite active-session work, not cloud wake or blanket autonomy.

1. State a checkable completion predicate, target/identity, original scope, existing external-action grants and operator-only gates. Separate task completion from segment stop conditions.
2. Establish observable dispatch/call/time limits, deadline, usage reserve and cancellation before work. Without a monetary budget use at most two independent workers, one review round, one integration correction round and a 15-minute supervised segment as the runtime default, subject to stricter host limits. This is not a currency guarantee. Do not activate a billed provider without an approved plan. No cron, hidden keep-alive, cache warming or wake loop.
3. Make the smallest evidence-justified change each iteration. Integrate before testing, prove the actual predicate and keep only warranted improvements, preserving unrelated changes. Use `/skill:pstack-principle-sequence-verifiable-units`. Commit only within authority.
4. Handle in-scope blockers, flaky verification and review noise causally. Record out-of-scope defects as findings rather than create unsolicited fixes, issues or PRs. Native `ask` is for material product, authority or irreversible decisions evidence cannot settle. Auth failure stops dependent actions; do not switch identity or runtime to evade it.
5. Log each iteration via `/skill:pstack-show-me-your-work` under `<repository>/.audit/pstack/<task>/`. External waits have an owner, cadence normally at least 60 seconds, finite deadline/attempt count and terminal/cancel predicate. Use an owned supervised process with captured handle, or bounded one-shot status reads. Native `wait` is only for pending owned work when no independent work remains. No extra sleep/watch layer.
6. Finish only when the goal predicate is evidenced. A plateau invites a different hypothesis within limits, not relaxed acceptance. At exhausted calls/time/reserve, operator cancel, safety gate or genuine dead end, use [Pause safely](pause-safely.md) to preserve goal, artifacts, pending items and exact resume command. Resume explicitly under OMP when the operator returns; do not claim completion at the boundary.

**Reply:** predicate, limits, iterations, retained/discarded work, real final predicate state, blocked gates and portable checkpoint if unfinished.
