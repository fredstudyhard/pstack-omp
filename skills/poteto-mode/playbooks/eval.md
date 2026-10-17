### Eval

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md). Establish the approved provider plan, observable call/time ceiling and stop conditions before candidates run. No child runtime or home-session discovery.

**Own experiment design, blinding and synthesis.**

**Blinding rules.** Candidate-visible directories, filenames and prompts contain none of eval, test, judge, experiment, rubric, score, compare, benchmark, candidate or arena as experiment labels. Preserve genuine task code/test requirements rather than falsify source. Use project-shaped sanitized labels, one organic goal prompt, no disclosure of other variants and no chain-eliciting request for private reasoning. Judge sees outputs by sanitized label, never model identity. One judge scores two variants together on one scale. Host safety/authority instructions are never hidden or weakened to achieve blinding.

1. Frame the variant and observable success. Write 3–6 concrete judge-only criteria and keep the rubric separate from candidate context.
2. Create authorized per-candidate isolated working directories with realistic skeleton, skill variant and context. Candidate-visible names stay sanitized; coordinator metadata lives outside those directories in the named task evidence path.
3. Author one organic user prompt, with no measurement leakage or self-report demands. Ask for normal design notes only; assess behavior from artifacts and actual file reads.
4. Read `/skill:pstack-arena`. Dispatch bounded native candidates with configured distinct roles/identities when available and permitted, identical prompt and exclusive outputs. Do not hardcode model names or change presets. If the required comparison cannot run, report the experiment BLOCKED rather than claim diversity from labels.
5. Dispatch a fresh blinded non-author judge with the required different-family identity when available. Identity must be established from actual host evidence. If unavailable, keep the independent promotion gate closed; local exploratory assessment is explicitly not that verdict.
6. Verify observable instruction following from explicitly supplied current-session `history://<id>` or `agent://<id>` records and artifacts. These URIs are not cold-session persistence. For an earlier run read only an explicitly named authorized export/checkpoint. Never scan user-home transcripts or discover sibling sessions. Grade files actually read and resulting code, not candidate claims. Missing transcript access makes that criterion NOT_RUN, not a fabricated pass.
7. Read every output end to end and compare against the blinded verdict. Investigate disagreement as possible bias or rubric ambiguity and synthesize. Save sanitized output references, rubric, revisions, actual identities, limits and verdict under `<repository>/.audit/pstack/<task>/`; exclude raw private transcripts and secrets.

**Reply:** variant, rubric, per-output notes, verified identities or limitations, judge verdict, synthesis and promotion recommendation. Required unavailable independence means no promotion acceptance.
