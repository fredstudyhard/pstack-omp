# Finding and Evidence Contract

Applies to normal and adversarial review. Follow the shared procedure in [Interrogate](../SKILL.md); this reference defines findings and verdicts, not a second review workflow.

## Native reviewer schema

Each actionable finding contains:

- `title`: imperative, concise fix target.
- `body`: bug, trigger and impact in one paragraph, with concrete code-path evidence and no unstated assumptions.
- `priority`: `P0` release-blocking, `P1` high, `P2` medium, `P3` informational.
- `confidence`: a number from `0.0` to `1.0`.
- `file_path`, `line_start`, `line_end`: patch-anchored location spanning at most ten lines.

A concrete suggestion is optional. Attribute independently raised findings to actual reviewer identities when relevant, without replacing these fields with a severity label or a vague function reference.

## Evidence bar

An actionable finding must be introduced by the reviewed change, supported by a concrete execution path and impact, actionable with a discrete fix or check, free of unstated assumptions, and proportionate to the repository's existing quality bar. Do not report style preferences, pre-existing defects or speculation as change findings. Structural concerns require demonstrated costs or violated requirements, not merely a different preferred implementation.

In adversarial synthesis, speculative suggestions, style nits and pre-existing issues may be accounted for as Noted or Dismissed candidates with a rationale, but never promoted into actionable findings or correctness blockers without meeting this bar. Multiple reviewers agreeing increases corroboration, not correctness; a single well-supported finding can be decisive.

## Verdict and coverage

Return `overall_correctness: correct` only after the scoped review is complete and no blocking bug remains; otherwise a completed review with a blocking bug uses `overall_correctness: incorrect`. Explain intent/requirement compliance, revision/base, files reviewed, checks actually run, missing proof and residual risk. Distinguish reported prior verification from observed results.

If evidence required to finish the review is unavailable, report `review_status: incomplete` and the exact missing prerequisite instead of issuing an unsupported correctness verdict. A required independent reviewer/family gate that cannot be satisfied is **BLOCKED**, even if direct inspection finds no defects. Absence of findings is not proof of correctness or satisfaction of that gate. A changed revision/base invalidates any verdict whose applicability no longer holds.
