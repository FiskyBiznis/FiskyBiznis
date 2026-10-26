# Third-party skills

Vendored into `.claude/skills/` on 2026-10-26. Licenses are in `third-party-licenses/`.

| Source | Commit | What was copied | License |
|---|---|---|---|
| https://github.com/addyosmani/agent-skills | `aeac41d4d005999432bb7312f7ff06383a91d59d` | `skills/*` (25 skills) and `references/` → `.claude/references/` | MIT |
| https://github.com/dietrichgebert/ponytail | `09c434ab73ca43761c5d8b0c5d341926c2fba710` | `skills/*` (6 skills: ponytail, -audit, -debt, -gain, -help, -review) | MIT |
| https://github.com/Graphify-Labs/graphify | `92741d162b2094ffc2fed58cfbd8ee823e9da62c` | `graphify/skill.md` → `graphify/SKILL.md`, plus `graphify/skills/claude/references/` | Apache-2.0 / MIT |

## Security review (2026-10-26)

No malicious content found. Checks run across all three full repos:

- Hidden Unicode (tag chars, zero-width, bidi overrides): none, except one zero-width space in graphify's `llm.py` that is used defensively to neutralise prompt-injection sentinels.
- Prompt-injection phrases: only in text warning the agent *against* following injected instructions.
- Encoded/obfuscated execution, pipe-to-shell, npm install/postinstall scripts, long base64 blobs: none.
- Outbound network: only user-configured LLM APIs and URLs the user asks graphify to ingest; ponytail's webhook is off unless a URL is set. graphify has no telemetry (query log is opt-in and local).

## Deliberately not copied

- **Hooks and plugin code** (ponytail `hooks/`, agent-skills `hooks/`). Not malicious, but they run automatically. Notably ponytail's "band" hook reads every local Claude Code transcript under `~/.claude/projects` to build a local cost ledger.
- **The graphify Python package.** The graphify skill needs the `graphify` CLI. Its Step 1 installs `graphifyy` (the official PyPI name) unpinned via `uv tool` / `pip` the first time it runs. That PyPI build was not audited here; pin it (e.g. `uv tool install graphifyy==<version>`) if that matters.
