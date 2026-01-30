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
- [Editor](https://antigravity.google/docs/editor)
>- Tab

# Antigravity Editor: Tab & Navigation

This guide covers the core navigation and completion tools: **Supercomplete**, **Tab-to-Jump**, and **Tab-to-Import**.

## Supercomplete

Supercomplete provides code suggestions in a region near your current cursor position.

![Supercomplete](https://antigravity.google/assets/image/docs/editor/supercomplete.png)

### How it Works

- **File-Wide Suggestions**: Suggestions can modify code throughout the document, handling tasks like changing variable names or updating separate function definitions simultaneously.
- **Accepting**: Press `Tab` to accept the changes.

## Tab-to-Jump

Tab-to-Jump is a fluid navigation tool that suggests the next logical place in your document to move your cursor to.

![Tab-to-Jump](https://antigravity.google/assets/image/docs/editor/tab_to_jump.png)

### How it Works

- A "Tab to jump" icon will appear offering to move your cursor to where your next logical edit will be. Pressing `Tab` instantly moves your cursor to that location.
- **Accepting**: Press `Tab` to accept the jump.

## Tab-to-Import

Tab-to-Import handles missing dependencies without breaking your flow.

![Tab-to-Import](https://antigravity.google/assets/image/docs/editor/tab_to_import.png)

### How it Works

- **Detection**: If you type a class or function that isn't imported, Antigravity suggests the import.
- **Action**: Press `Tab` to complete the word and instantly add the import statement to the top of the file.

## Settings

In your settings, you can customize the behavior of these features:

- **Enable/Disable Features**: You can individually turn off Autocomplete, Tab-to-Jump, Supercomplete, or Tab-to-Import.
- **Tab Speed**: Controls the responsiveness of suggestions.
- `Slow`: Waits for more context before suggesting.
- `Default`: Offers a balanced pace.
- `Fast`: Provides rapid-fire suggestions.
- **Highlight Inserted Text**: When enabled, text inserted via Tab is highlighted to track changes easily.
- **Clipboard Context**: When enabled, Antigravity uses the contents of your clipboard to improve completion accuracy.
- **Allow Gitignored Files**: Enables Tab features (suggestions and jumping) within files listed in your `.gitignore` file. Tab will only ignore gitignored files if git is installed.

[Editor](https://antigravity.google/docs/editor)

[Command](https://antigravity.google/docs/command)

On this Page

- Antigravity Editor: Tab & Navigation

- Supercomplete

- Tab-to-Jump

- Tab-to-Import

- Settings
