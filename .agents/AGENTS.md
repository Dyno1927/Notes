# Shared agent instructions — Notes

These instructions are shared by Codex, AGY, OpenCode, and other compatible agents.

## Working agreements

- Answer the requested question or task directly and avoid unrelated features or cleanup.
- Distinguish known facts, inferences, assumptions, and hypotheses.
- Preserve existing architecture and external contracts.
- Use Pascal-Kebab-Case directories, PascalCase files, camelCase functions and variables, and PascalCase types unless tooling, APIs, schemas, or language conventions require otherwise.
- Plan before large, multi-file, architectural, or risky changes; execute small clear changes directly.
- Run relevant tests, builds, linters, formatters, and type checks after implementation.
- Documentation follows successful verification.
- Never expose credentials, tokens, or private configuration.
- Local commits are permitted; pull, push, published merges, and destructive Git operations require explicit approval.

## Project memory

- This repository contains personal learning notes and examples across C#, JavaScript, and Python.
- Preserve language-specific organization and existing explanatory style.
- Do not turn notes into production abstractions or rewrite examples merely for style.
- Verify code examples with the relevant language toolchain when practical.
