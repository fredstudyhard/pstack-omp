---
name: pstack-create-verification-skill
description: "Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /skill:pstack-create-verification-skill, \"make a control skill for this repo\", \"make a driver skill for this repo\", or when a project has no scripted way to prove UI/CLI/service behavior."
---

# Create a verification skill

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); it governs tools, roles, authority, budgets and verification throughout this skill.

Generate a project-local `.omp/skills/verify-<project>/SKILL.md`, using the actual stable project slug and `name: verify-<project>`. It must launch the app, exercise real user behavior and capture evidence. Invoke its discovered `skill://verify-<project>` name or concrete file, not a guessed generic verification command.

## 1. Interview the repo, not the user

Answer these from the codebase and only ask the user what you cannot observe:

- **Surface:** what does a user actually touch? A web UI, a CLI/TUI, a desktop app, an API, a mobile app, a library? A repo can have several; pick the primary one and note the rest.
- **Run:** how does the app start locally? Prefer the repo's own documented dev command (package scripts, Makefile, README quickstart). Note ports, env vars, seed data, auth.
- **Drive:** how can an agent interact with it programmatically? Existing harnesses first — Playwright/Cypress specs, expect scripts, PTY helpers, curl-able endpoints, a debug port. Only then pick a generic recipe: browser/CDP for web and Electron, a tmux/PTY harness for CLI/TUI, plain HTTP for services.
- **Observe:** what evidence can be captured? Screenshots, terminal transcripts, response bodies, logs, exit codes, DB state.
- **Isolate:** can two instances run side by side (ports, data dirs, profiles)? If not, say so in the generated skill: refusing to double-drive a shared instance beats corrupting the user's session.

If the checkout doesn't build or start as-is, fix that first (or report it precisely) before generating; a skill written against a broken base teaches wrong steps. When an irrelevant missing asset blocks startup (a static dir the API never serves, a sample config), the generated skill may create it, clearly marked as verification scaffolding, and remove it in cleanup.

## 2. Generate the skill

Write `.omp/skills/verify-<project>/SKILL.md` with YAML frontmatter (`name: verify-<project>` and a description naming the app, surface and trigger). Ground every section below in inspected source and observed commands; leave no placeholders. For native browser operations read `xd://eval/browser` before using `eval`, and read captured images with `read`. State authorization boundaries; generated guidance grants no permission.

Include the concrete installed pstack runtime-contract path discovered during authoring (not a guessed project-relative sibling), or state the equivalent native authority/tool constraints directly so this project-owned skill remains usable without pstack. Confirm the generated name is discoverable in a fresh OMP process in the project cwd; if unavailable, record discovery NOT_RUN rather than claiming registration.

- **Launch:** the exact command that starts the app for verification, and how to tell it's ready (a log line, a prompt). Launch must reach a usable state from an empty data dir, including any migrations and seed data. Ready means usable, not just that a process answers. A database health check can pass while its init scripts are still running. Include teardown. For a short-lived CLI or TUI there is no server to keep alive: launch means build the binary (or install deps) once, then start each drive in its own isolated PTY or tmux session.
- **Doctor:** one read-only check that answers "is this instance worth driving?" — process up, right version/build, port owned by us, auth valid. An agent runs this first whenever anything looks off.
- **Drive:** the harness recipe with real selectors/commands from this repo, not examples. Prefer stable handles (ARIA labels, data attributes, prompt strings, route paths) over coordinates and tab order.
- **Evidence:** what to capture for a proof and where it goes. State the proof standards: exercise the real user path, not internal setters or test-only endpoints; capture the action and the resulting state, not just the final screen; verify side effects (files written, rows inserted, messages sent) alongside what's visible; mocks only where a production boundary already isolates the external system. When the safe path is a dry-run or test mode, verify what it actually skips by observing (files, network, git refs) rather than trusting its name: some dry-runs still touch the network or open a browser.
- **Cleanup:** how to tear down instances the run created. Never kill by process name; kill what you started. Cleanup removes instances and scratch state, never the evidence: proof artifacts survive the teardown, in a location the skill names.
- **Helpers:** any script the skill ships is executable and its invocation is shown in the skill body. A helper the reader has to reverse-engineer is not a helper.

## 3. Seed the feature map

Create `.omp/skills/verify-<project>/features/README.md` plus one file per identified user-facing feature (initially the top 3–5 from actual routes, commands, menus or docs). Follow [`references/feature-map-example/`](references/feature-map-example/): a README index and feature files answering what the feature is, how to reach and drive it, and what observable state proves it works. Preserve the example's four H2 sections and link every file from the index.

## 4. Prove the generated skill before handing it over

Run its own instructions end to end once: launch, doctor, drive ONE mapped feature (one is enough; the map exists so later runs can cover the rest), capture evidence, clean up. After cleanup, confirm the evidence still exists at the named location — a cleanup that eats the proof fails this step. Fix what fails, and run the generated cleanup after every failed iteration too, so broken attempts don't strand processes and ports. A generated skill that was never executed is a draft, not a deliverable. If you proved it in a stand-in for the real target (a container in place of a fresh VM, a local stack in place of a remote one), list every setup step the stand-in did that the target will not. Those steps stay unverified until a run on the real target covers them.

## 5. Offer the maintenance loop

Point the user at `/skill:pstack-maintain-verification-skill` for keeping the map honest as the app changes. Suggest a cadence only if they ask.
