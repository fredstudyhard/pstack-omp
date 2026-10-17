### Authoring or modifying a skill

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md).

**Own the skill's voice and executable contract.** Do not install or modify global skills merely because a repository skill is being authored.

1. Read the target repository's existing skill conventions and applicable authoring/governance instructions. Use native OMP tool semantics and actual configured roles, with `pstack-` invocation or explicit relative paths for bundled siblings. Put reusable mechanics in one structural source rather than duplicate a tool/model catalog.
2. Validate minimal frontmatter (`name`, `description`), referenced files, cross-skill resolution, authority boundaries and entrypoint/runtime-contract links. Resolve helper paths relative to the loaded skill tree, not a user-home store.
3. For structural changes, exercise representative task cases using [Eval](eval.md) within an approved budget. A subjective wording-only change may explain why a behavior experiment is unnecessary; do not fabricate one.
4. Run [Opening a PR](opening-a-pr.md) only when requested or already authorized.

When in doubt, delete prose that changes no decision. Explain confusing rules only. Point at structural sources per `/skill:pstack-principle-encode-lessons-in-structure`; delegate to skills by path rather than restate them. Propose a missing repeated workflow without silently creating new scope.

**Reply:** skill purpose, design decisions, observed validation and remaining dependencies.
