# Verification entrypoints and coverage boundaries

This distribution contains procedures, not a universal certification of future applications. Keep source validation, native discovery, scenario execution and integration acceptance separate.

## Source and behavior

From the repository root:

```sh
bun run doctor
bun run check
bun run test
python3 examples/issue-desk/verification/scripts/verify.py
```

The source checker validates all 64 canonical entries, the 14-primary/50-internal split, runtime-contract references and both source and materialized Markdown links. Behavioral suites cover installer ownership/path boundaries, internal-guide collision/local-edit refusal, portable helpers and the maintained synthetic application. The example verifier drives the real CLI, checks filtering-before-pagination, persisted add/done transitions, refusal/error invariants and protected file preservation; it does not pin incidental diagnostic wording.

Optional helper dependency acquisition is explicit, lockfile-pinned and lifecycle-disabled; see [maintenance](omp-maintenance.md). Helper typechecking additionally needs the declared development toolchain; it is not copied to the runtime installation.

## Native availability

After an authorized installation:

```sh
python3 tools/discovery.py --cwd <supported-working-directory>
```

This resolves all 14 primary skills and 50 internal-guide URIs in fresh native readers with exact installed-source identity, then proves all 50 internal names unavailable as global skills. Repeat in every supported working directory; one cwd does not establish precedence or discovery elsewhere. A concrete file read alone does not prove registry availability. Restart existing sessions to pick up registry changes.

For disable/re-enable acceptance, disable owned skills, prove their names unavailable in a fresh reader, check unrelated user/project skills still resolve, then restore reviewed source and repeat affected discovery. Never delete or move protected `.omp` paths as cleanup.

## Actual workflow acceptance

Use `python3 tools/demo.py` to create a separate synthetic buggy workspace. Enter OMP there with the printed prompt. Observe the actual defect, repair, CLI output and persisted state; a passing test suite alone is not a completed agent experience.

`tools/live-smoke.py` supports explicitly scoped, finite synthetic journeys. Each prompt must name its target, permitted writes, model/call/time budget and expected evidence. It uses the committed smoke overlay without editing user settings. Its owned process group is terminated on deadline. Do not use it with credentials, private history, real customer data or unapproved external outputs. Local `.audit/` summaries and project checkpoints are not automatically publishable records.

For native task review, inspect actual worker outputs and reproduce findings. Separate author and reviewer contexts; do not label same-family contexts as cross-family review. For pause/pickup, record portable relative artifacts and content fingerprints, then use a fresh session to reconstruct state and perform only pending work.

## Limits

- Availability/source review does not prove every workflow's project-specific execution. The [API inventory](omp-capabilities.json) describes shipped procedures, not scenario PASS labels.
- Product authentication, shared-resource writes, live PR mutation, deployment, external services and other platforms require their own approved target and acceptance evidence.
- A missing scanner is NOT_RUN, not PASS. Use the applicable bounded manual/deterministic security gate; do not implicitly install a scanner or label absence as success.
- A required unavailable model-family reviewer stays blocked. No role label, local sketch, parent acceptance or test run can counterfeit that verdict.
- Foreground RPC control-page authoring is not a predeployed hosted service. Portable checkpoint plus explicit pickup is not unattended cloud wake.
- No hidden scheduler, autonomous merge, always-on routing hook or second model registry is installed.

Source identities, changes and security design are documented in [provenance](../tools/omp-provenance.json), [porting](omp-porting.md), [security](omp-security.md) and [maintenance](omp-maintenance.md). Keep internal evaluation matrices, raw evidence and council/model outputs local; publish accepted records only through the applicable human-adoption and sanitization gate.
