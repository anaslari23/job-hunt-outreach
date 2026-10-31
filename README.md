# job-hunt-outreach

An agent skill that runs one end-to-end job hunt from your CV.

1. Reads your CV and builds a profile (titles, keywords, years of experience)
2. Finds openings on Instagram
3. Verifies every opening on LinkedIn
4. Builds a contact spreadsheet (`.xlsx`)
5. Applies on LinkedIn Easy Apply, with your approval per batch
6. Drafts and sends cold emails through Gmail, only after you say "send"

It never signs in for you, never guesses email addresses, and never invents facts about you. See [`references/safety-and-approvals.md`](references/safety-and-approvals.md).

## Contents

```
job-hunt-outreach/
├── SKILL.md            # the flow, loaded by the agent
├── references/         # step-by-step detail, read on demand
├── templates/          # email, questionnaire and report templates
└── scripts/            # spreadsheet builder and verifier (Python 3 + openpyxl)
```

## What your agent needs

The skill describes the workflow. It relies on tools the agent must have:

| Need | Used for |
|---|---|
| A browser tool (e.g. Claude in Chrome, or another browser-automation tool) | Instagram and LinkedIn steps |
| Gmail access (connector or MCP server) | Drafting and sending emails |
| Google Drive access (optional) | Finding your CV |
| Python 3 with `openpyxl` | Building the spreadsheet |

`SKILL.md` mentions Claude-style Chrome tools in a few places. In other agents, substitute whatever browser tool you have. Without a browser or Gmail tool the agent can still build the profile and spreadsheet, and will draft emails as text for you to send.

## Install

Pick your agent. In every case the folder must be named `job-hunt-outreach` and contain `SKILL.md` at its top level.

First get the files:

```bash
git clone https://github.com/<your-username>/job-hunt-outreach.git
```

### Claude Code

Personal (all projects):

```bash
mkdir -p ~/.claude/skills
cp -r job-hunt-outreach ~/.claude/skills/
```

One project only:

```bash
mkdir -p .claude/skills
cp -r job-hunt-outreach .claude/skills/
```

Restart Claude Code, then ask: "Run the job hunt skill" or invoke it by name.

### Claude.ai and Claude desktop app

1. Zip the folder so `job-hunt-outreach/` is the top level of the zip:
   ```bash
   zip -r job-hunt-outreach.zip job-hunt-outreach
   ```
2. Open Settings, then Capabilities (or Skills), and upload the zip.
3. Turn the skill on. Connect Gmail and Google Drive under Connectors if you want emailing and CV lookup.

Menu names change between releases; check Anthropic's current help pages if yours differ.

### OpenAI Codex CLI

Codex reads skills from a user directory:

```bash
mkdir -p ~/.codex/skills
cp -r job-hunt-outreach ~/.codex/skills/
```

Restart Codex. If your Codex version does not list the skill, use the fallback below. Check the [Codex docs](https://developers.openai.com/codex) for the current skills location, since it has changed between versions.

### Google Antigravity

Workspace (one project):

```bash
mkdir -p .agent/skills
cp -r job-hunt-outreach .agent/skills/
```

Global (all projects):

```bash
mkdir -p ~/.gemini/antigravity/skills
cp -r job-hunt-outreach ~/.gemini/antigravity/skills/
```

A workspace skill overrides a global one with the same name.

### Gemini CLI, Cursor, Windsurf, and other agents without skill support

Agents that do not load `SKILL.md` folders can still use this as instructions:

1. Copy the folder into your project, for example `docs/job-hunt-outreach/`.
2. Add a pointer in the agent's instruction file:

   | Agent | Instruction file |
   |---|---|
   | Codex, many others | `AGENTS.md` |
   | Gemini CLI | `GEMINI.md` |
   | Cursor | `.cursor/rules/job-hunt.mdc` |
   | Windsurf | `.windsurfrules` |

   Suggested text:

   ```
   For job hunting, follow docs/job-hunt-outreach/SKILL.md. Read files under
   references/ and templates/ only when SKILL.md points to them.
   ```

3. Start with: "Follow job-hunt-outreach/SKILL.md. Here is my CV."

## Usage

Start a chat and say:

```
Run the job hunt skill. My CV is attached.
```

The agent asks for your CV first, shows a profile summary, asks one batch of questions (CTC, notice period, relocation, sending Gmail account, resume file), then works through the steps. It stops for approval before applying and before sending any email.

## Spreadsheet scripts

```bash
pip install openpyxl
python3 scripts/build_spreadsheet.py data.json AI_Job_Outreach_Nov2026.xlsx
python3 scripts/verify_spreadsheet.py AI_Job_Outreach_Nov2026.xlsx
```

`data.json` has keys `shortlist`, `instagram_vs_linkedin`, `more_instagram_finds`, `requirements_check`, `excluded` and `notes`. Each is a list of objects whose keys are the column names in lowercase with underscores, for example `contact_email`.

## Notes and limits

- Instagram, LinkedIn and Gmail may require you to be signed in already. The agent will ask you to sign in rather than enter credentials.
- Automated activity can conflict with LinkedIn and Instagram terms. Use it at your own risk and keep volumes modest.
- Email addresses are only taken from posts or postings you can see. Nothing is guessed.

## License

MIT. See [LICENSE](LICENSE).
