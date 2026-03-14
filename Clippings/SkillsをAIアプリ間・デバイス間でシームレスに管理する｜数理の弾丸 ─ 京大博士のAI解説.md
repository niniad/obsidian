---
title: "SkillsをAIアプリ間・デバイス間でシームレスに管理する｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/n108e6d279aa0"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2026-02-08
created: 2026-03-14
description: "こちらの動画で紹介したSkillsの管理における私の実践について、他の方でも同じ方法を実践できるレベルで詳しく説明したいと思います。    Skillsの管理で主に意識していることは以下の通りです：    Claude Code や Cursor など、アプリケーションを切り替えても同じSkillsが使えること    複数のPCで開発をしていて、PCを切り替えても同じSkillsが使えること    Skillsがバージョン管理されていること    上記の運用をAIが認識していて、Skillsの追加や更新を依頼したときに意図通り挙動すること    もちろんSkillsの品質を維持するとか"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/250105574/rectangle_large_type_2_700cac9b5a6195fc8c88a92985eee834.jpeg?width=1280)

## SkillsをAIアプリ間・デバイス間でシームレスに管理する

参加中

![画像](https://assets.st-note.com/img/1770532520-yfn3DtucK2oqVUTrPgajZJbS.png?width=1200)

こちらの動画で紹介したSkillsの管理における私の実践について、他の方でも同じ方法を実践できるレベルで詳しく説明したいと思います。

![](https://www.youtube.com/watch?v=_lfcwMvgveY)

Skillsの管理で主に意識していることは以下の通りです：

- Claude Code や Cursor など、アプリケーションを切り替えても同じSkillsが使えること
- 複数のPCで開発をしていて、PCを切り替えても同じSkillsが使えること
- Skillsがバージョン管理されていること
- 上記の運用をAIが認識していて、Skillsの追加や更新を依頼したときに意図通り挙動すること

もちろんSkillsの品質を維持するとか、Skillsが膨大になりすぎないといった観点での管理も必要だと思いますが、今回は上記に注目して私の運用方法を説明したいと思います。

メンバーシップ未加入の方はこちらからぜひご検討をお願いいたします！

## 要点

端的に何をすればいいかを先に記載しておきます。

- アプリケーションを切り替えても同じSkillsが使えること  
	→ 各AIアプリのスキル格納場所（~/.claude/skillsや~/.cursor/skillsなど）から、~/.agents/skills へのシンボリックリンクを定義する
- PCを切り替えても同じSkillsが使えること  
	→ ~/.agents/skills を chezmoi でバージョン管理・リモート同期する
- 上記の運用をAIが認識  
	→ グローバルのCLAUDE.mdに運用方法を記載しておく

下記に具体手順を記載します。正直この記事を丸ごとAIに投げてセットアップしてもらうえばそれで良い気もしますが笑

## 全体像

まず、この運用の全体像を図で示します。

![画像](https://assets.st-note.com/img/1770532482-PJq1HF9Xe5UZ3tRScx4VBaNE.png?width=1200)

Skillsの実体は ~/.agents/skills/ に一元化されており、各AIアプリケーションのSkillsやコマンドの格納場所からシンボリックリンクで参照しています。そして ~/.agents/ 自体は chezmoi で管理されているので、Git によるバージョン管理とリモート同期が可能です。

以下、それぞれの層について詳しく説明します。

## シンボリックリンクによるアプリ間共有

Claude Code は ~/.claude/skills/ を、Cursor は ~/.cursor/skills/ をSkillsの格納場所として参照します。それぞれのディレクトリに同じファイルをコピーして配置すると、片方を更新したときにもう片方も手動で更新する必要があり、管理が煩雑になります。

そこで、Skillsの実体を ~/.agents/skills/ という共通ディレクトリに集約し、各アプリの格納場所からはシンボリックリンクを張ります。

### セットアップ手順

```ruby
# 共通ディレクトリを作成
mkdir -p ~/.agents/skills
mkdir -p ~/.agents/commands

# 以下、Claude Codeの場合
# Skills/Commandsディレクトリをシンボリックリンクに置き換える
# 既にディレクトリが存在する場合は中身を ~/.agents/ に移動してから削除
ln -s ~/.agents/skills ~/.claude/skills
ln -s ~/.agents/commands ~/.claude/commands
```

この設定により、~/.agents/skills/ にSkillを追加・編集するだけで、Claude Code と Cursor の両方に即座に反映されます。他のAIアプリケーションを使う場合も、同じ要領でシンボリックリンクを追加するだけです。

シンボリックリンクを張る前に、既存の ~/.claude/skills/ や ~/.cursor/skills/ にファイルが存在する場合は、先に ~/.agents/skills/ へ移動しておきましょう。シンボリックリンクの作成時に既存のディレクトリがあるとエラーになります。

## chezmoi によるバージョン管理とリモート同期

### chezmoi とは

[chezmoi](https://www.chezmoi.io/) （シェモア）は、ホームディレクトリの dotfiles（設定ファイル）を Git で管理するためのツールです。~/.local/share/chezmoi/ にソースディレクトリを持ち、ここを Git リポジトリとして管理します。chezmoi apply を実行すると、ソースディレクトリの内容がホームディレクトリの対応する場所に反映されます。

### ソースディレクトリの構成

私の chezmoi ソースディレクトリは以下のような構造です（無関係のdotfilesについては省略しています）。

```ruby
~/.local/share/chezmoi/
├── .git/                          ← Gitリポジトリ
├── .chezmoiignore                 ← chezmoi管理から除外するファイル
├── dot_agents/
│   ├── skills/
│   │   ├── chezmoi/
│   │   │   └── SKILL.md
│   │   ├── git-commit/
│   │   │   └── SKILL.md
│   │   ├── ux-principles/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── no-dead-ends.md
│   │   └── ...（他のスキル）
│   └── commands/
│       ├── chezmoi-pull.md
│       └── chezmoi-push.md
└── dot_claude/
    ├── CLAUDE.md                  ← グローバル設定
    └── symlink_commands           ← ~/.claude/commands のシンボリックリンク定義
```

dot\_agents/skills/ 配下に各スキルのディレクトリが配置されています。

### スキルの編集フロー

スキルを追加・編集する際は、常に chezmoi のソースディレクトリ側で作業します。

```ruby
# 新しいスキルを追加する場合
mkdir -p ~/.local/share/chezmoi/dot_agents/skills/my-new-skill
vim ~/.local/share/chezmoi/dot_agents/skills/my-new-skill/SKILL.md

# 既存スキルを編集する場合
vim ~/.local/share/chezmoi/dot_agents/skills/git-commit/SKILL.md

# 編集後、実体に反映
chezmoi apply
```

### リモート同期

chezmoi のソースディレクトリは通常の Git リポジトリなので、GitHub 等にリモートリポジトリを用意して同期できます。

PC-A で変更した場合：

```javascript
cd ~/.local/share/chezmoi
git add -A
git commit -m "update skills"
git push
```

PC-B で反映する場合：

```javascript
cd ~/.local/share/chezmoi
git pull
chezmoi apply
```

初めてのマシンにセットアップする場合は以下のコマンドだけで完了します。

```swift
chezmoi init <GitHubのリポジトリURL>
chezmoi apply
```

その後、シンボリックリンクの設定（前述の ln -s コマンド）を行えば、同じ環境が再現されます。

## CLAUDE.md への運用ルールの記載

ここまでの仕組みを整えても、AIエージェントがこの運用を知らなければ意味がありません。例えば「新しいスキルを作って」と依頼したとき、AIが ~/.claude/skills/ に直接ファイルを作成してしまうと、chezmoi の管理外になり、次回の chezmoi apply で上書き・消失するリスクがあります。

Claude Code にはグローバルの CLAUDE.md（~/.claude/CLAUDE.md）という仕組みがあり、ここに記載した内容はすべての会話で自動的にコンテキストとして読み込まれます。つまり、Skillsの管理ルールをここに書いておけば、AIは常にその運用を認識した状態で作業してくれます。

私の ~/.claude/CLAUDE.md には、以下のようなセクションを設けています。

```typescript
## スキル・コマンド管理

スキルとコマンドは chezmoi のソースディレクトリで一元管理する。

### ディレクトリ構成

~~~
~/.local/share/chezmoi/dot_agents/skills/     ← スキルの編集・追加はここ
  ↓ chezmoi apply
~/.agents/skills/                              ← chezmoiが生成する実体
  ↑ symlink
~/.claude/skills/                              ← Claude Codeが参照するパス
~~~

### ルール

1. スキル・コマンドの新規作成・編集は必ず ~/.local/share/chezmoi/dot_agents/ 配下で行う
   - ~/.agents/ や ~/.claude/ を直接編集しない
   - 直接編集してしまった場合は chezmoi add で取り込む
2. 編集後は chezmoi apply で実体に反映する
3. 別マシンへの同期は chezmoi init && chezmoi apply で行う
```

ポイントは以下の3つです：

1. ディレクトリ構成を図示して、どこが編集場所でどこが参照場所かを明示している
2. 「ここに編集しろ」「ここを直接触るな」というルールを明記している
3. 間違えて直接編集してしまった場合のリカバリ方法（chezmoi add）も書いている

これにより、AIに「スキルを追加して」「このスキルを修正して」と依頼したとき、AIは ~/.local/share/chezmoi/dot\_agents/skills/ 配下で作業し、最後に chezmoi apply を実行する、というフローを勝手に踏んでくれます。

## まとめ

この運用で行っていることを改めて整理すると、以下の3つです。

1. ~/.agents/skills/ を共通のSkills格納場所とし、各AIアプリのディレクトリからシンボリックリンクを張る
2. ~/.agents/ を chezmoi で管理し、Gitベースのバージョン管理とリモート同期を実現する
3. CLAUDE.md に運用ルールを記載し、AIエージェントが正しい場所でスキルを編集するようにする

それぞれは単純な仕組みですが、組み合わせることで「どのアプリでも、どのPCでも、同じSkillsが使える。そしてAIもその運用を理解している」という状態を作れます。

---

YouTubeチャンネルでは研究・実装に関するコアな内容を発信しています。こちらもぜひよろしくお願いします。