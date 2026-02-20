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
- [Browser](https://antigravity.google/docs/browser)
>- Allowlist / Denylist

# Allowlist / Denylist

The browser uses a two-layer security system to control which URLs can be accessed:

- **Denylist** \- Deny dangerous/malicious URLs
- **Allowlist** \- Explicitly allow trusted URLs

## How It Works

### Denylist

The denylist is maintained and enforced using the Google Superroots’s BadUrlsChecker service (See documentation). When the browser attempts to navigate to a URL, the hostname is checked against the server-side denylist via RPC.

**NOTE:** If the server is unavailable, access is denied by default.

### Allowlist

The allowlist is a local text file that you can edit to explicitly trust specific URLs.

![Allowlist](https://antigravity.google/assets/image/docs/browser-allowlist.png)

The allowlist is initialized with just localhost, and can be edited at anytime.

When the browser attempts to navigate to a non-allowlisted URL, it will prompt you with an “always allow” button, which if clicked will add the URL to the allowlist and enable the browser to open and interact with the web page. An example situation is shown below:

![Always Allow](https://antigravity.google/assets/image/docs/always-allow-url.png)

You can also add/remove URLS from the allowlist manually. However, the denylist always takes precedence: you cannot allowlist a URL that appears on the denylist.

[Chrome Extension](https://antigravity.google/docs/chrome-extension)

[Separate Chrome Profile](https://antigravity.google/docs/separate-chrome-profile)

On this Page

- Allowlist / Denylist

- How It Works
