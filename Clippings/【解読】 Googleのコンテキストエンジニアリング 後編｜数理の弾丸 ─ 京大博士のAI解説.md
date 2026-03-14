---
title: "【解読】 Googleのコンテキストエンジニアリング 後編｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/ncde239de1b28"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2025-12-29
created: 2026-03-14
description:
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/239699214/rectangle_large_type_2_eea65751aad09039d0ba9dbe9119e971.jpeg?width=1280)

## 【解読】 Googleのコンテキストエンジニアリング 後編

参加中

![画像](https://assets.st-note.com/img/1767000433-AuD6nPMBVdH5JWKrZwiFepN1.png?width=1200)

前編では、Google ADKのコンテキストエンジニアリングに通じる3つの軸を整理しました。

> **ストレージとプレゼンテーションの分離**  
> 永続的な情報（ストレージ）と、エージェントの呼び出しごとに作成するワーキングコンテキストを明確に区別する。  
>   
> **明示的な変換ロジック**  
> コンテキストは、場当たり的な文字列結合ではなく、名前付け・順序付けられたプロセッサによって構築される。  
>   
> **スコープの限定**  
> すべてのモデル呼び出しは、必要最小限のコンテキストのみを参照する。エージェントはひたすら増えていく情報に溺れるのではなく、必要に応じて追加情報を取得しにいく。

前編より

この記事ではこれらの概念的な理解を、ADKの実装を確認しながら精緻にしていきます。

## ストレージとプレゼンテーションの分離

参照可能な情報全体（ストレージ）と、各コールでエージェントに渡されるワーキングコンテキスト（プレゼンテーション）を分離するという考え方です。

ストレージはセッション・メモリ・アーティファクトからなり、それぞれが独立したServiceとして実装されています。

### セッション（BaseSessionService）

セッションID、ユーザーID、状態（state）、および主情報であるイベント（event）のリストを保持するクラスです。ユーザリクエスト、思考、ツール呼び出し、モデルレスポンスなどひとつひとつの挙動を「イベント」と呼んでいます。ユーザがリクエストを飛ばしてからモデルがレスポンスを返すまでの一連のシーケンスは呼び出し（invocation）と呼ばれ、以下の構造で実装されています。

```
Session
└── Invocation
    ├── Event (User Input)
    ├── Event (Model Thought)
    └── Event (Model Response)
└── Invocation
    ├── Event (User Input)
    └── ...
```

イベントは次のような情報を含む構造化されたデータであり、エージェントとのチャット履歴をでかい文字列として管理する状態からの脱却が目指されています。

- author: 発言者 (user, agent)
- content: テキストや画像などのデータ
- actions: ツール呼び出しやその結果
- timestamp, invocation\_id 等のメタデータ

セッションデータは、ローカル環境ではSQLiteに、本番環境ではVertex AI Agent Engine管理下のDBに保管することが想定されています。

### メモリ（BaseMemoryService）

過去に終了したセッションをメモリとして保存することができます。

現状は、指定されたセッションの履歴全体を保存するadd\_session\_to\_memoryが用意されており、開発者はこれを使って過去のセッションを検索用データとして保存することができます。また、検索はsearch\_memoryとして実装されています。

現状、ユーザとのやり取りからエージェントが自発的にメモリを更新するような挙動は実装されておらず、過去セッションの永続化のみ対応している状態です。

### アーティファクト（BaseArtifactService）

プロンプトに含めるには大きすぎるデータ（ユーザの添付したドキュメント、画像など）を管理する層です。アーティファクトには例えば次のようなものが含まれます。

- ユーザーがチャット画面などを通じて提供したPDFや画像などのファイル
- コード実行ツールが生成したプロット画像やデータファイル
- 外部APIから取得した長大なJSONデータやPDF

これらはプロンプトからは分離され、エージェントにはこれらのファイルそのものではなく場所（URI）が渡されます。これにより、エージェントにいきなり巨大な情報を渡すのではなく、必要に応じて参照させるという形を取ることができます。

## 明示的な変換ロジック

入力・出力の処理ロジックは独立したミニマムな処理のリストとして定義されています。処理を小さいパーツに分けることで出し入れ・差し替えを容易にし、コンテキスト処理の肥大化・ブラックボックス化を防いでいます。

```ruby
36:68:src/google/adk/flows/llm_flows/single_flow.py
class SingleFlow(BaseLlmFlow):
  def __init__(self):
    super().__init__()
    self.request_processors += [
        basic.request_processor,
        auth_preprocessor.request_processor,
        request_confirmation.request_processor,
        instructions.request_processor,
        identity.request_processor,
        contents.request_processor,
        context_cache_processor.request_processor,
        _nl_planning.request_processor,
        _code_execution.request_processor,
        _output_schema_processor.request_processor,
    ]
    self.response_processors += [
        _nl_planning.response_processor,
        _code_execution.response_processor,
    ]
```

## スコープの限定

ADK は「各エージェントは、タスク遂行に必要な最小限のコンテキストしか見ない」という原則をデフォルトとして実装しています。マルチエージェント（特に並列実行やサブエージェント呼び出し時）では、会話履歴が一本のリストではなく、 **ブランチ（枝）** として管理されます。

各イベントには branch 属性が付与され、履歴を取得する \_get\_contents 関数は、現在のエージェントのブランチに属さないイベントを自動的に除外します。例えば、エージェントAがサブエージェントBとCを並列に動かしているとき、Bの履歴にはAとBの会話だけが含まれ、Cの会話（兄弟エージェントの動き）はデフォルトで見えないようになっています。

また、エージェントを定義する際の引数 include\_contents によって、各ターンでエージェントに渡されるコンテキストの範囲を制御することができます。

```swift
chat_agent = Agent(
    name="アシスタントエージェント",
    include_contents={default|none},
    instruction="あなたは優秀なアシスタントです。"
)
```

- default の場合：\_get\_contents 関数が呼び出され、セッション内の有効な全イベントがエージェントに渡される
- none の場合：
	- イベントリストを後ろから逆順にスキャンする
		- 開始点、つまり「ユーザーの発言」または「他エージェントからの依頼」が見つかるまで遡る
		- 開始点から現在までのイベントだけを切り出して \_get\_contents に渡す

## まとめ

この記事では、Google ADKで実践されているコンテキストエンジニアリングのプラクティスについて要点を整理しました。エージェントロジックを組む際に参考になる点も多くあると思うので、 [前編](https://note.com/mathbullet/n/n6b18b2cb379c) の内容と併せてぜひ活用してください！

---

数理の弾丸は、京大情報系の博士課程と企業のAIエンジニアを掛け持つ投稿者が、人工知能や言語にまつわる学術知をわかりやすく、誤魔化さずに伝えることを目指すYouTubeチャンネルです。