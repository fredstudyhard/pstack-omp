### Refactoring

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md) for native drivers and pstack sibling resolution.

**The structure changes. The behavior does not.** A discovered bug or missing feature is a separate scoped finding. Route an intentional behavior change to Feature; cross-cutting structural programs use `/skill:pstack-figure-it-out`.

1. Pin the current behavior. Read `/skill:pstack-how`, then capture a characterization test, snapshot or equivalence harness before moving structure. Typecheck and lint are not a behavioral pin.
2. Name the missing structure per `/skill:pstack-principle-model-the-domain`. Keep boring local code when its shape is already clear. Delete branches or invalid states, not merely add indirection.
3. State the target module layout, types and call graph per `/skill:pstack-principle-foundational-thinking` and `/skill:pstack-principle-redesign-from-first-principles`. Use `/skill:pstack-architect` when the shape crosses a function boundary.
4. Subtract first. Remove dead code, one-caller wrappers, redundant validators and orphan references. Apply `/skill:pstack-principle-subtract-before-you-add` and `/skill:pstack-principle-laziness-protocol`. Discard only this task's speculative edits, preserving unrelated work.
5. Move in small behavior-preserving units. Migrate every caller and delete the old API in the same wave, with no shim or parallel legacy path. Check strings, prose and back-references as well as symbols. When delegation is allowed, brief configured native implementation workers with paths, old/new names and the behavior contract, using isolated exclusive writer trees. Integrate before running checks; a leaf returns the diff to its parent.
6. Prove unchanged behavior on the real artifact. Replay the baseline or compare old/new outputs and drive the matching CLI/UI/API. Inconclusive is not PASS.
7. Confirm reduced reader load per `/skill:pstack-principle-minimize-reader-load`. Discard the task's change if it offers none.
8. Shape authorized ordered commits, subtraction then reshape then necessary cleanup, per `/skill:pstack-principle-sequence-verifiable-units`. Run [Opening a PR](opening-a-pr.md) only within publication authority.

**Reply:** structure changed, pinned behavior, equivalence evidence, reader-load delta, retained and discarded work. No new behavior.
