# Deep and Adversarial Review

Load only for the explicit deep/adversarial mode selected in [Interrogate](../SKILL.md). Its shared procedure and [finding/evidence contract](review-contract.md) remain mandatory. The deliverable is a synthesized judgment, never automatically applied changes.

## Select authorized coverage

Deep review adds the relevant [rubric](rubric.md), [code-quality lens](code-quality-review.md) and [lead judgment framework](lead-judgment.md). A single reviewer can provide that depth. Multi-model review is a separate opt-in coverage choice, not an automatic consequence of loading these lenses.

For requested multi-model review, the adversarial signal comes from independent model diversity, not assigned personas. Select eligible configured native reviewer roles for the requested independent families; do not enumerate every configured model by default. Launch permitted independent reviews in one native `task` batch only when actual host delegation gates permit, with explicit read-only scopes and approved finite budget, deadline and stop conditions. Use `council-a` and `council-b` only for an explicit council request or the host's escalation trigger. Never invent roles, hard-code provider models, activate a provider or bypass host fanout restrictions.

A fresh independent reviewer must not be the author. Record actual transcript identities and effort when required; role names do not prove model family. A specifically required model/family unavailable, unverified or falling back makes that gate **BLOCKED**. Do not replace it with the author, a continuous advisor, test results or another family and call the gate passed. Other investigation may continue with partial coverage clearly labeled. A requested independent verdict cannot silently become a local comparison when delegation is disallowed.

When host policy requires fail-closed isolation, collect bounded evidence first and obtain a fresh no-tools review of that packet. Only label a verdict as the designated model/family verdict when the transcript establishes the required identity and effort without fallback; otherwise label it fallback/unverified and keep the required gate blocked.

## Give reviewers the same evidence

Build each prompt from [reviewer-prompt.md](reviewer-prompt.md). Supply the same stated intent and requirements/non-goals, pinned revision/base, diff or files, necessary surrounding interfaces, known verification and missing facts, shared finding contract, relevant rubric and quality lens. Do not substitute a summary for available code. Model and effort resolve through the host's configured roles. Keep evidence bounded and exclude unrelated private context.

## Synthesize and judge

Parse every reviewer's candidates and merge duplicates without losing evidence or attribution. Note independent agreement and explicit disagreement. Independently corroborated findings are useful signal; investigate lone findings on their merits, especially security or correctness bugs, rather than voting them down. The lead verifies concrete paths against the shared evidence bar and owns the final verdict, not a neutral aggregation of model opinions.

Read [lead-judgment.md](lead-judgment.md), then place each candidate into one bucket with contributing reviewer identities and a one-line rationale:

- **Act On:** substantiated correctness, security or maintainability issues against actual goals that would block a real PR; use the shared finding schema.
- **Consider:** legitimate, evidence-backed issues whose remediation tradeoff merits attention but is not established as blocking; use the shared schema if presented as actionable findings.
- **Noted:** technically valid but non-actionable or context-dependent observations, premature optimization or low-impact suggestions; keep separate from findings.
- **Dismissed:** wrong, stylistic, pre-existing, unsupported or missing-context claims; state why.

Do not let the demanding quality lens override the evidence bar or authorize edits. Its structural simplifications and rubrics remain available without turning preferences, arbitrary file-size thresholds or speculative improvements into correctness blockers.

## Extended output

Keep the shared verdict and coverage fields, then add:

### Intent

The stated intent and applicable requirements/non-goals.

### Reviewers

One bullet per reviewer: label, actual model identity (or unverified), reviewed revision/base, finding count and coverage/gate status. State any required family that could not run.

### Act On / Consider / Noted / Dismissed

Candidates grouped as above, preserving evidence, rationale and attribution. Empty groups may be stated briefly; no findings is valid.

### Agreement Map

Where reviewers independently agreed or explicitly diverged, and what the evidence supports. Never equate consensus, an advisor's ongoing feedback or a role label with an independent-family gate passing.
