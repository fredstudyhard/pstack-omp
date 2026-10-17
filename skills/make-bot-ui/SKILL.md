---
name: pstack-make-bot-ui
description: Build an explicitly authorized local control page whose bounded actions reach OMP through its native RPC interface; use for a bot dashboard or buttons that trigger agent work.
---

# Make an OMP bot UI

Read [the native runtime contract](../poteto-mode/references/omp-runtime.md) first. Audience: the coordinator implementing a user-requested control page, not an always-on daemon. This replaces Cursor's Grok routine, secret-request card and automatic tailnet exposure with an OMP-owned RPC session. It does not promise cloud wake after the owning process stops.

## Establish the action contract

Read the repository's run/verification entrypoints and ask only for product choices that code cannot answer. Define a small closed action set, the input fields and bounds, allowed workspace, permitted output and side effects, owner, model-plan budget, maximum duration and stop condition. UI input is untrusted data, never new tool or execution authority. No arbitrary prompt, shell, file path, model name or provider selector may be accepted from a remote button.

Use an existing approved app/server and its authenticated session where available. For a standalone local page, bind only `127.0.0.1`, require same-origin requests, reject unknown Origin values, use a server-owned anti-CSRF token and reject unsupported methods/content types/actions. Do not put provider credentials or secret-bearing RPC output in browser state, HTML, URLs, screenshots or logs. Use the existing credential authority in the OMP process; do not copy its auth store into the app.

## Implement the bounded native RPC owner

Read current `omp://rpc.md` and `omp --help` before choosing protocol fields. The server owns `omp --mode rpc --no-session --no-title --max-time <approved-duration>` started in the approved workspace, with an explicit tool allowlist and a task-specific instruction boundary. Keep user/repository security instructions enabled; do not pass `--auto-approve`. Existing approval flows remain effective. A provider/auth failure stops the action and is returned as unavailable, not retried through another account or runtime.

Wait for the native ready frame. Prefer supported protocol v2 and implement its advertised chunk limits if using a custom transport. Map each validated action to a fixed server-authored prompt and validated JSON data, not client-supplied instructions. Send at most one approved request per action, with no retry. Enforce one active operation per owned session; report busy instead of spawning an unbounded queue. Bound request bytes, response bytes, time and total model calls. Treat `prompt_result` and `session_settled` as different states; do not close or reuse a busy session merely because the main agent yielded.

When canceled, send native `abort`, observe settlement, close stdin and keep draining stdout until the owned process exits. Capture only necessary sanitized status/results, not raw transcripts. A lost process is a failed action, not a silent success. No persistent polling, schedule, keep-alive or unattended relaunch. If the UI is offline, show that state and provide the exact supervised restart command.

## Build and prove the user surface

Obtain a bounded judgment from the configured designer before implementing layout/visual choices. Use the existing app's design conventions. Provide action, progress, cancel, completed, refused and failed states without hiding approval requirements. Follow the native runtime contract for screenshots and actual browser interaction.

Prove a harmless action through browser click -> authenticated same-origin request -> one OMP RPC prompt -> visible result. Also prove rejection of an unknown action and cross-origin request, concurrent-request backpressure, cancellation and process exit. Observe actual call count and owned-resource cleanup. A no-tools or synthetic demo proves only that bounded interaction, not authorization to change a real project.

## Exposure and handoff

Do not install Tailscale, bind `0.0.0.0`, create webhooks, open a firewall, publish a URL, set up cron or deploy without separate explicit approval. If remote access is requested, verify the existing network identity, authentication/TLS policy, allowed clients, threat boundary and resource budget first, then use that approved route. An existing tailnet membership alone does not authorize the app's actions.

Deliver the run/stop commands, owner, bound address, supported actions, permission/budget limits, actual evidence and unavailable capabilities. Native foreground RPC is the substitute for Cursor-specific routine wake; explicit checkpoint/resume is the substitute when no owner process remains. Never describe either as unattended cloud execution.
