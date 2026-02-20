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
>- Secure Mode

# Secure Mode

Secure Mode provides enhanced security controls for the Agent, allowing you to restrict its access to external resources and sensitive operations. When Secure Mode is enabled, several security measures are enforced to protect your environment.

## Features

### Browser URL Allowlist/Denylist

In Secure Mode, the Agent's ability to interact with external websites is governed by the browser's Allowlist and Denylist. This applies to:

- **External Markdown Images**: The Agent will only render images from URLs that are allowed.
- **Read URL Tool**: The Read URL tool will only auto-execute for allowed URLs.

### Terminal, Browser, and Artifact Review Policies

Secure Mode enforces the following behavior for terminal, browser, and artifact interactions:

- **Terminal Auto Execution**: Set to "Request Review". The Agent will always prompt for permission before executing any terminal command. The terminal allowlist is ignored when Secure Mode is enabled.
- **Browser Javascript Execution**: Set to "Request Review". The Agent will always prompt for permission before executing Javascript in the browser.
- **Artifact Review**: Set to "Request Review". The Agent will always prompt for confirmation before acting on plans laid out in artifacts.

### File System Access

Secure Mode restricts the Agent's access to the file system to ensure it only interacts with authorized files:

- **Respect .gitignore**: The Agent will respect `.gitignore` rules, preventing it from accessing ignored files.
- **Workspace Isolation**: Access to files outside the workspace is disabled. The Agent can only view and edit files within the designated workspace.

[Browser Subagent](https://antigravity.google/docs/browser-subagent)

[Sandboxing Terminal Commands](https://antigravity.google/docs/sandbox-mode)

On this Page

- Secure Mode

- Features
