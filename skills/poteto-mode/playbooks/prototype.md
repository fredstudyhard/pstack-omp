### Prototype

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md). Read images with native `read` and obtain configured designer judgment before visual implementation/approval.

**Own the decision, not production code.** The prototype is a throwaway instrument. Speed beats polish, but authority, isolation and honest evidence still apply. Read-only investigation does not authorize a prototype.

1. State the decision: layout, interaction, density, behavior, timing or approach. Without a decision, route to Feature rather than sketch aimlessly.
2. For an open visual direction, gather public references and summarize a moodboard of themes, palettes and layouts. Let the operator settle genuine preference forks; skip when direction is set. Do not upload private material or add unapproved network dependencies.
3. Build in an explicitly named isolated scratch directory, separate from production source and protected `.omp`. For visual work use plain HTML/CSS/JS or the existing light rendering stack and a supervised dev server. For behavior/timing use the smallest script exercising the fork. No production abstraction or test framework is required. Any added dependency needs current justification.
4. Compare labeled alternatives behind one switcher per `/skill:pstack-principle-exhaust-the-design-space`.
5. Drive the real matching surface. For visual decisions capture/read each variant and exercise its interaction; for behavioral decisions record timing, output or observed render. The observation is the experiment, not a claim that production tests passed.
6. Present alternatives, evidence, tradeoffs and recommendation. Retain the chosen throwaway artifact and path as requested, and stop only run-owned processes. Hand the direction to Feature or `/skill:pstack-architect` for a separately authorized real build. No automatic PR.

**Reply:** variants, screenshots or observed output/timing, tradeoffs, recommendation, scratch path and explicit throwaway status.
