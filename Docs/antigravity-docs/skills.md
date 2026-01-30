[Google Antigravity](https://antigravity.google/)

Product

Use Cases keyboard\_arrow\_down

Pricing

Blog

Resources keyboard\_arrow\_down

Download download

menu

Product  Use Cases keyboard\_arrow\_down

Built for developers in the agent-first era

Explore how Google Antigravity helps you build

[See overview](https://antigravity.google/use-cases)

[workspaces Professional keyboard\_arrow\_right](https://antigravity.google/use-cases/professional) [code\_blocks Frontend keyboard\_arrow\_right](https://antigravity.google/use-cases/frontend) [stacks Fullstack keyboard\_arrow\_right](https://antigravity.google/use-cases/fullstack)

Pricing  Blog  Resources keyboard\_arrow\_down

Everything you need to stay up-to-date and get help

[Documentation keyboard\_arrow\_right](https://antigravity.google/docs) [Changelog keyboard\_arrow\_right](https://antigravity.google/changelog) [Support keyboard\_arrow\_right](https://antigravity.google/support) [Press keyboard\_arrow\_right](https://antigravity.google/press) [Releases keyboard\_arrow\_right](https://antigravity.google/releases)

[Home expand\_more](https://antigravity.google/docs/home)

[Getting Started](https://antigravity.google/docs/get-started)

[Agent expand\_more](https://antigravity.google/docs/agent)

[Models](https://antigravity.google/docs/models)

[Agent Modes / Settings](https://antigravity.google/docs/agent-modes-settings)

[Rules / Workflows](https://antigravity.google/docs/rules-workflows)

[Skills](https://antigravity.google/docs/skills)

[Task Groups](https://antigravity.google/docs/task-groups)

[Browser Subagent](https://antigravity.google/docs/browser-subagent)

[Secure Mode](https://antigravity.google/docs/secure-mode)

[Sandboxing](https://antigravity.google/docs/sandbox-mode)

Tools expand\_more

[MCP](https://antigravity.google/docs/mcp)

[Artifacts expand\_more](https://antigravity.google/docs/artifacts)

[Task List](https://antigravity.google/docs/task-list)

[Implementation Plan](https://antigravity.google/docs/implementation-plan)

[Walkthrough](https://antigravity.google/docs/walkthrough)

[Screenshots](https://antigravity.google/docs/screenshots)

[Browser Recordings](https://antigravity.google/docs/browser-recordings)

[Knowledge](https://antigravity.google/docs/knowledge)

[Editor expand\_more](https://antigravity.google/docs/editor)

[Tab](https://antigravity.google/docs/tab)

[Command](https://antigravity.google/docs/command)

[Agent Side Panel](https://antigravity.google/docs/agent-side-panel)

[Review Changes + Source Control](https://antigravity.google/docs/review-changes-editor)

[Agent Manager expand\_more](https://antigravity.google/docs/agent-manager)

[Workspaces expand\_more](https://antigravity.google/docs/workspaces)

[Playground](https://antigravity.google/docs/playground)

[Inbox](https://antigravity.google/docs/inbox)

[Conversation View expand\_more](https://antigravity.google/docs/conversation-view)

[Browser Subagent View](https://antigravity.google/docs/browser-subagent-view)

[Panes](https://antigravity.google/docs/panes)

[Review Changes + Source Control](https://antigravity.google/docs/review-changes-manager)

[Changes Sidebar](https://antigravity.google/docs/changes-sidebar)

[Terminal](https://antigravity.google/docs/terminal)

[Files](https://antigravity.google/docs/files)

[Browser expand\_more](https://antigravity.google/docs/browser)

[Chrome Extension](https://antigravity.google/docs/chrome-extension)

[Allowlist / Denylist](https://antigravity.google/docs/allowlist-denylist)

[Separate Chrome Profile](https://antigravity.google/docs/separate-chrome-profile)

[Plans](https://antigravity.google/docs/plans)

[Settings](https://antigravity.google/docs/settings)

[FAQ](https://antigravity.google/docs/faq)

- side\_navigation
- [Agent](https://antigravity.google/docs/agent)
>- Skills

# Agent Skills

Skills are an [open standard](https://agentskills.io/home) for extending agent capabilities. A skill is a folder containing a `SKILL.md` file with instructions that the agent can follow when working on specific tasks.

## What are skills?

Skills are reusable packages of knowledge that extend what the agent can do. Each skill contains:

- **Instructions** for how to approach a specific type of task
- **Best practices** and conventions to follow
- **Optional scripts and resources** the agent can use

When you start a conversation, the agent sees a list of available skills with their names and descriptions. If a skill looks relevant to your task, the agent reads the full instructions and follows them.

## Where skills live

Antigravity supports two types of skills:

| Location | Scope |
| --- | --- |
| `<workspace-root>/.agent/skills/<skill-folder>/` | Workspace-specific |
| `~/.gemini/antigravity/global_skills/<skill-folder>/` | Global (all workspaces) |

**Workspace skills** are great for project-specific workflows, like your team's deployment process or testing conventions.

**Global skills** work across all your projects. Use these for personal utilities or general-purpose tools you want everywhere.

## Creating a skill

To create a skill:

1. Create a folder for your skill in one of the skill directories
2. Add a `SKILL.md` file inside that folder

```
            .agent/skills/
└─── my-skill/
    └─── SKILL.md

```

Every skill needs a `SKILL.md` file with YAML frontmatter at the top:

```
            ---
name: my-skill
description: Helps with a specific task. Use when you need to do X or Y.
---

# My Skill

Detailed instructions for the agent go here.

## When to use this skill

- Use this when...
- This is helpful for...

## How to use it

Step-by-step guidance, conventions, and patterns the agent should follow.

```

### Frontmatter fields

| Field | Required | Description |
| --- | --- | --- |
| `name` | No | A unique identifier for the skill (lowercase, hyphens for spaces). Defaults to the folder name if not provided. |
| `description` | Yes | A clear description of what the skill does and when to use it. This is what the agent sees when deciding whether to apply the skill. |

Tip: Write your description in third person and include keywords that help the agent recognize when the skill is relevant. For example: "Generates unit tests for Python code using pytest conventions."

## Skill folder structure

While `SKILL.md` is the only required file, you can include additional resources:

```
            .agent/skills/my-skill/
├─── SKILL.md       # Main instructions (required)
├─── scripts/       # Helper scripts (optional)
├─── examples/      # Reference implementations (optional)
└─── resources/     # Templates and other assets (optional)

```

The agent can read these files when following your skill's instructions.

## How the agent uses skills

Skills follow a **progressive disclosure** pattern:

1. **Discovery**: When a conversation starts, the agent sees a list of available skills with their names and descriptions
2. **Activation**: If a skill looks relevant to your task, the agent reads the full `SKILL.md` content
3. **Execution**: The agent follows the skill's instructions while working on your task

You don't need to explicitly tell the agent to use a skill—it decides based on context. However, you can mention a skill by name if you want to ensure it's used.

## Best practices

### Keep skills focused

Each skill should do one thing well. Instead of a "do everything" skill, create separate skills for distinct tasks.

### Write clear descriptions

The description is how the agent decides whether to use your skill. Make it specific about what the skill does and when it's useful.

### Use scripts as black boxes

If your skill includes scripts, encourage the agent to run them with `--help` first rather than reading the entire source code. This keeps the agent's context focused on the task.

### Include decision trees

For complex skills, add a section that helps the agent choose the right approach based on the situation.

## Example: A code review skill

Here's a simple skill that helps the agent review code:

```
            ---
name: code-review
description: Reviews code changes for bugs, style issues, and best practices. Use when reviewing PRs or checking code quality.
---

# Code Review Skill

When reviewing code, follow these steps:

## Review checklist

1. **Correctness**: Does the code do what it's supposed to?
2. **Edge cases**: Are error conditions handled?
3. **Style**: Does it follow project conventions?
4. **Performance**: Are there obvious inefficiencies?

## How to provide feedback

- Be specific about what needs to change
- Explain why, not just what
- Suggest alternatives when possible

```

[Rules / Workflows](https://antigravity.google/docs/rules-workflows)

[Task Groups](https://antigravity.google/docs/task-groups)

On this Page

- Agent Skills

- What are skills?

- Where skills live

- Creating a skill

- Skill folder structure

- How the agent uses skills

- Best practices

- Example: A code review skill
