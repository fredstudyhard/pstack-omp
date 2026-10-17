# Security

Do not publish secrets, exploit details or private data in public issues. Use this fork's [security reporting surface](https://github.com/fredstudyhard/pstack-omp/security) if private reporting is available. This fork does not claim that GitHub private vulnerability reporting is enabled. If it is unavailable, ask the maintainer for a private channel without posting technical vulnerability details.

## Scope

The native `skills/` tree, portable helpers, installer, dependency acquisition and bounded synthetic smoke tooling are in scope. Unintended capability use, secret exfiltration, broken ownership/path boundaries and supply-chain weaknesses merit review. Prompt instructions do not themselves enforce an OS sandbox or grant authority.

Foreign plugin hooks, CI workflows, model registries and subprocess-agent shims are not active components of this fork. Issues in OMP itself belong with its maintainers; upstream-only defects should follow the owning upstream project's security policy rather than being attributed to this adaptation.

## Supported source

The maintained native branch is `omp-native`, currently `0.9.90-omp.2`. There is no plugin auto-update or maintained backport release line. Review fixes as candidates, verify their source identity and applicable behavior, then explicitly install. See [security design](docs/omp-security.md) and [maintenance/rollback](docs/omp-maintenance.md).
