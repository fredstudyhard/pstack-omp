---
name: pstack-poteto-help
description: Guides users through pstack setup, /skill:pstack-poteto-mode, and picking the skill, playbook, or principle for a task. Type /skill:pstack-poteto-help with a question.
---

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

# Poteto help

Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is not a help question. Read [`poteto-mode`](../poteto-mode/SKILL.md) and do the work under it.

This map covers 14 global primary skills and 50 internal guides. The installer compiles source-relative links and invocation examples into the deployed topology. An internal workflow is requested through `/skill:pstack-poteto-mode <workflow>` and read under its `references/library/<short-name>/GUIDE.md`, never by its retired registry name. Read the matching source before answering. Link the actual local source; public fork links require a verified remote revision. Upstream guides are provenance, not native instructions.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with `/skill:pstack-poteto-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check the state that changes the answer, and mention it only when it does:

- For model or routing questions, read [`setup-pstack`](../setup-pstack/SKILL.md). OMP owns role/model configuration; this bundle supplies no model sheet.
- No project `verify` or `verify-*` skill or other app harness means agents have no scripted way to drive the app. Mention `/skill:pstack-create-verification-skill` when the question is about proving a change works.

If native discovery or a required role is missing, offer `/skill:pstack-setup-pstack` for a read-only diagnosis. Do not mutate configuration or imply that pstack can activate a provider.

## Get set up

1. Read the installed fork's root README for its native installation procedure; do not offer upstream plugin commands.
2. Read [`/skill:pstack-setup-pstack`](../setup-pstack/SKILL.md) for a read-only capability and discovery diagnosis.
3. Offer one task prompt with a goal and a falsifiable acceptance check, using `/skill:pstack-poteto-mode` and [`references/prompting.md`](references/prompting.md).

For cost questions, explain worker, review and iteration costs. Bound the dispatch count, deadline and observable usage before billed work. Model/effort selection belongs to the host configuration; the skill neither changes it nor supplies an override sheet.

## Start a task with `/skill:pstack-poteto-mode`

`/skill:pstack-poteto-mode` matches the task to a playbook, copies the playbook's steps into the todo list, and runs the other skills as the steps need them. A step it skips stays in the list as `skip: <reason>`. A good prompt states the goal and how to tell it's done. It doesn't list skills, because a hand-written sequence tends to drop or reorder steps the playbook would keep. Read [`references/prompting.md`](references/prompting.md) before you help word one.

Invoke `/skill:pstack-poteto-mode` for each new task unless current host evidence proves automatic routing. “New task” starts fresh playbook selection. Native delegation, budget and authority rules live in the runtime contract; no plugin hook or wake service is implied.

## Pick a skill

The default answer is `/skill:pstack-poteto-mode`, which routes to the applicable playbook and on-demand guide. Direct commands are reserved for the 14 primary entrypoints; the installed table below compiles all other entries into main-entrypoint intents. Read the guide before recommending it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`/skill:pstack-poteto-mode`](../poteto-mode/SKILL.md) |
| Check that the agent understood their goal and the problem before it starts | [`/skill:pstack-in-your-own-words`](../in-your-own-words/SKILL.md) |
| Aim a task higher before starting: more expert, more outcome-focused, not overspecified | [`/skill:pstack-sharpen`](../sharpen/SKILL.md) |
| Know how code works now, or where new code should live | [`/skill:pstack-how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`/skill:pstack-why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`/skill:pstack-teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`/skill:pstack-recall`](../recall/SKILL.md) |
| Catch up on what changed in this chat since their last message, in a few plain sentences and small visuals, with enough context to decide each action item | [`/skill:pstack-ketchup`](../ketchup/SKILL.md) |
| Know what a small diff could break outside itself | [`/skill:pstack-blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`/skill:pstack-architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`/skill:pstack-arena`](../arena/SKILL.md) |
| Run parallel checks over slices, or race workers | [`/skill:pstack-swarm`](../swarm/SKILL.md) |
| Review a bounded diff, or explicitly request deep/adversarial review | [`/skill:pstack-interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`/skill:pstack-tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`/skill:pstack-typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Strip comments before review, using a reviewer that didn't write them | [`/skill:pstack-no-comments`](../no-comments/SKILL.md) |
| Clean AI tells out of prose | [`/skill:pstack-unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`/skill:pstack-technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`/skill:pstack-bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`/skill:pstack-create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`/skill:pstack-maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`/skill:pstack-benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`/skill:pstack-figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`/skill:pstack-show-me-your-work`](../show-me-your-work/SKILL.md) |
| Diagnose native skill discovery, tools and configured role availability | [`/skill:pstack-setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`/skill:pstack-automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`/skill:pstack-reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`/skill:pstack-correct`](../correct/SKILL.md) |
| Find their way around pstack | `/skill:pstack-poteto-help` |

The source checkout retains sibling directories for maintenance; the installed internal documents live beneath poteto-mode's library. Route by the appropriate source description and concrete compiled guide, not a guessed global command. The `principle-*` sources are covered below.

Close calls:

- `/skill:pstack-how` explains what the code does. `/skill:pstack-why` explains the reasons. `/skill:pstack-teach` runs one or both and explains the result plainly.
- `/skill:pstack-arena` gives every worker the same brief and merges the best parts. `/skill:pstack-swarm` splits work into slices or a race and returns one report.
- `/skill:pstack-architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `/skill:pstack-interrogate` reviews the diff. `/skill:pstack-blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `/skill:pstack-recall` rebuilds context across recent chats. `/skill:pstack-ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `/skill:pstack-figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

Not in pstack:

- App driving uses native browser tools after reading their schema, or a real project `.omp/skills/verify-<project>/SKILL.md`; there is no implicit driver.
- Supervised native task/process controls replace foreign loop and child-CLI skills. Personal authoring is repository-source-first native SKILL.md authoring.
- pstack has no orchestrate skill. Orchestrate is a `/skill:pstack-poteto-mode` playbook. If the slash menu shows an orchestrate command, another plugin provides it.

## Playbooks and principles

Playbooks are step lists inside `/skill:pstack-poteto-mode`, not skills, so they have no slash command. Inside `/skill:pstack-poteto-mode`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs [Autopilot-full](../poteto-mode/playbooks/autopilot-full.md). "stack them, don't ship" runs [Autopilot-stack](../poteto-mode/playbooks/autopilot-stack.md). Read the selected playbook's merge rules before explaining what runs unattended.
- "run the eval playbook" runs Eval.

Without `/skill:pstack-poteto-mode`, a phrase such as "babysit this pr" can start pstack's standalone [`/skill:pstack-babysit`](../babysit/SKILL.md) skill instead. The [Playbooks section](../poteto-mode/SKILL.md#playbooks) lists every playbook and when it applies. Read [Babysit](../poteto-mode/playbooks/babysit.md) or [Shipping](../poteto-mode/playbooks/shipping.md) for the port's PR workflow.

pstack has no separate planning skill. The [Multi-phase plan playbook](../poteto-mode/playbooks/multi-phase-plan.md) writes a plan without implementing it. The Prototype playbook or `/skill:pstack-architect` explores a design in code only within the user's authorized mode.

All 24 principles remain sibling `pstack-principle-*` skills, readable by concrete path regardless of menu visibility. The [Principles index](../poteto-mode/SKILL.md#principles) lists them.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The mode stopped applying after a few turns | Check the current runtime's routing configuration through the sources under Get set up. Without automatic routing, invoke `poteto-mode` for each task. |
| A question got treated as the next step of the last task | Say "new task", or say the turn doesn't need the mode. |
| A model choice had no effect | Use [setup-pstack](../setup-pstack/SKILL.md) to inspect actual host role attribution; pstack has no override sheet. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A skill didn't load on its own | Read its description and the current runtime's skill-loading instructions. Invoke it explicitly when needed; `/skill:pstack-poteto-mode` doesn't run every skill. |
| Parallel agents overwrote each other | Give each agent its own worktree. |
| A long run moved but finished nothing | Read [Autonomous run](../poteto-mode/playbooks/autonomous-run.md), define a falsifiable finish condition and bounded supervised segment. Cross-session wake is not provided; resume from an explicit checkpoint. |
| The reply claims success from a green build | Ask for the real command, flow, stored value, or profile. That's the prove-it-works principle. |

For a run that drifts, [`references/prompting.md`](references/prompting.md) has one-line steers, and [`references/recipes.md`](references/recipes.md) has prompts to adapt.

## Make pstack my own

- [`/skill:pstack-automate-me`](../automate-me/SKILL.md) drafts a personal mode skill from the user's own history, to use alongside `/skill:pstack-poteto-mode`.
- [`/skill:pstack-reflect`](../reflect/SKILL.md) after a session turns its lessons into skill edits the user approves.
- `/skill:pstack-poteto-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Fix a misbehaving skill in its own PR, not inside the feature work where it went wrong.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then the link to that file. Keep it short unless the user asked for the whole map.
