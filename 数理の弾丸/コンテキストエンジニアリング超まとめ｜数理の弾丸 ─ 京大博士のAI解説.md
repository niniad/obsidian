---
title: "コンテキストエンジニアリング超まとめ｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/n6cc01bcfa868"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2026-01-03
created: 2026-03-14
description: "コンテキストエンジニアリング関連の論文・テックブログ・ホワイトペーパーなどの文献を時系列でまとめます。いまのところコンテキストエンジニアリングという領域は探索期であり、さまざまな観点からのノウハウが散在している状態です。情報を得るのも結構大変だと思うので、このリストが少しでも助けになれば幸いです。   2025-07    2025-07-02：Context Engineering    著者：LangChain    リンク：https://blog.langchain.com/context-engineering-for-agents/    概要：エージェントの各ステップで、"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/241127824/rectangle_large_type_2_10f6fdd11c5c6106b5bb01ce686a62c9.jpeg?width=1280)

## コンテキストエンジニアリング超まとめ

参加中

![画像](https://assets.st-note.com/img/1767442263-Tgu2rqLNMvGIVWahBzEXQUbs.png?width=1200)

![画像](https://assets.st-note.com/img/1767444515-QTsySfXDP3cRWuJpOBaZw1nF.png?width=1200)

コンテキストエンジニアリング関連の論文・テックブログ・ホワイトペーパーなどの文献を時系列でまとめます。いまのところコンテキストエンジニアリングという領域は探索期であり、さまざまな観点からのノウハウが散在している状態です。情報を得るのも結構大変だと思うので、このリストが少しでも助けになれば幸いです。

## 2025-07

- 2025-07-02：Context Engineering
	- 著者：LangChain
		- リンク： [https://blog.langchain.com/context-engineering-for-agents/](https://blog.langchain.com/context-engineering-for-agents/)
		- 概要：エージェントの各ステップで、限られたコンテキストウィンドウに「次の一手に必要な情報」を過不足なく入れるための設計領域としてコンテキストエンジニアリングを定義し、代表的戦略を write / select / compress / isolate の4類型に整理します。あわせて、これらを支える実装観点として LangGraph の設計上の意図（状態・メモリ・ツール結果等の扱い）に言及します。
- 2025-07-17：A Survey of Context Engineering for Large Language Models
	- 著者：Lingrui Mei et al.
		- リンク： [https://arxiv.org/abs/2507.13334](https://arxiv.org/abs/2507.13334)
		- 概要：推論時に与える情報（information payload）を体系的に最適化する「prompt設計を超えた」領域としてコンテキストエンジニアリングを定義し、基礎要素を context retrieval & generation / context processing / context management に分解した体系化を提示します。さらに、それらが RAG、メモリ＋ツール統合推論、マルチエージェント等のシステム実装に統合される様式を整理し、1400本超の文献分析を通じて、複雑なコンテキスト理解能力と長文出力生成能力の非対称性（理解側は伸びるが、同等に洗練された長文出力生成は限定的）というギャップを課題として指摘します。

## 2025-08

ここから先は有料部分です

- 2025-08-09：Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code
	- 著者：Muhammad Haseeb
		- リンク： [https://arxiv.org/abs/2508.08322](https://arxiv.org/abs/2508.08322)
		- 概要：意図明確化（Intent Translator）・外部知識注入（Elicitによる検索）・文書統合（NotebookLM）・マルチエージェント実装（Claude Code）を組み合わせたコンテキストエンジニアリングワークフローを提示し、複数ファイル規模のコード生成での信頼性向上を主張します。
- 2025-08-23：Anemoi: A Semi-Centralized Multi-agent System Based on Agent-to-Agent Communication MCP server from Coral Protocol
	- 著者：Xinxing Ren et al.
		- リンク： [https://arxiv.org/abs/2508.17068](https://arxiv.org/abs/2508.17068)
		- 概要：「コンテキストエンジニアリング＋中央集権プランナ」型の一般的マルチエージェントシステムが抱えるプランナ性能依存とエージェント間協調の弱さを問題化し、A2A通信による構造化協調で改善する半中央集権型のマルチエージェントシステムを提案します。

## 2025-09

- 2025-09-02：Context Engineering for Trustworthiness: Rescorla Wagner Steering Under Mixed and Inappropriate Contexts
	- 著者：Rushi Wang et al.
		- リンク： [https://arxiv.org/abs/2509.04500](https://arxiv.org/abs/2509.04500)
		- 概要：関連情報と不適切情報が混在する「poisoned context」状況でLLMが少量の不適切信号にも影響され得る点をテストベッドで分析し、Rescorla–Wagner型の定式化を踏まえた2段階ファインチューニング（RW-Steering）で不適切信号の無視を促す手法を提案します。
- 2025-09-22：OnePiece: Bringing Context Engineering and Reasoning to Industrial Cascade Ranking System
	- 著者：Sunhao Dai et al.
		- リンク： [https://arxiv.org/abs/2509.18091](https://arxiv.org/abs/2509.18091)
		- 概要：産業用の段階的（cascade）検索・ランキングに対し、構造化した入力拡張（structured context engineering）と潜在表現上の段階的推論（block-wise latent reasoning）を統合する枠組みを提案し、オンライン指標の改善を報告します。
- 2025-09-25：AOT\*: Efficient Synthesis Planning via LLM-Empowered AND-OR Tree Search
	- 著者：Xiaozhuang Song et al.
		- リンク： [https://arxiv.org/abs/2509.20988](https://arxiv.org/abs/2509.20988)
		- 概要：レトロシンセシス計画で、LLMが生成する合成経路候補をAND-OR木探索に組み込み、報酬割当と検索の設計に「retrieval-based context engineering」を用いることで、探索反復回数やコストを抑えつつ解探索性能を高めることを目的としています。
- 2025-09-25：QuantMind: A Context-Engineering Based Knowledge Framework for Quantitative Finance
	- 著者：Haoxue Wang et al.
		- リンク： [https://arxiv.org/abs/2509.21507](https://arxiv.org/abs/2509.21507)
		- 概要：金融の非構造テキスト・表・数式を知識へ抽出して索引化し、柔軟な検索戦略とマルチホップ推論で根拠追跡可能な生成を目指す2段構成の枠組みを提示し、ドメイン特化のコンテキストエンジニアリングが有効であることをユーザスタディで示すとしています。
- 2025-09-29：Effective context engineering for AI agents
	- 著者：Anthropic Applied AI team
		- リンク： [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
		- 概要：コンテキストエンジニアリングを「推論時に投入されるトークン集合を、制約下で目的挙動に最適化するためのキュレーション／維持戦略」としてプロンプトエンジニアリングと区別し、コンテキストは有限資源で逓減効果がある（長文化で想起精度が下がる等）という前提を置きます。その上で、埋め込み検索などの事前取得に加えて、軽量な参照（ファイルパス、保存クエリ、リンク等）を保持し、ツールで実行時に必要分だけロードする just-in-time 戦略、長時間タスク向けの compaction（要約して新しいコンテキストへ再初期化）、structured note-taking、multi-agent 構成などを中心に、実務上の設計指針を整理します。

## 2025-10

- 2025-10-06：Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
	- 著者：Qizheng Zhang et al.
		- リンク： [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618)
		- 概要：LLMアプリケーション（エージェント等）における重み更新ではなく入力コンテキストの適応に焦点を当て、要約の簡潔さに偏ることで知識が落ちる問題（brevity bias）や、反復的な書き換えで詳細が失われる問題（context collapse）を指摘します。Dynamic Cheatsheet の適応メモリを踏まえ、生成・内省・キュレーションのモジュール過程で「進化するプレイブック」としてコンテキストを蓄積・整理する ACE を提案し、オフライン（システムプロンプト等）とオンライン（エージェントメモリ等）の双方で性能・コスト面の改善を報告しています。
- 2025-10-08：Haystack Engineering: Context Engineering for Heterogeneous and Agentic Long-Context Evaluation
	- 著者：Mufei Li et al.
		- リンク： [https://arxiv.org/abs/2510.07414](https://arxiv.org/abs/2510.07414)
		- 概要：既存の needle-in-a-haystack ベンチマークが、実運用で生じるノイズ（偏った検索に起因する異質なディストラクタや、エージェント的ワークフローにおける誤りの連鎖）を捉えにくいと主張し、ノイズ文脈を系統的に構成する haystack engineering の必要性を述べます。Wikipedia のハイパーリンクネットワークに基づく HaystackCraft を提示し、異種リトリーバ（疎・密・ハイブリッド・グラフ系）やエージェント的操作（反省・クエリ更新・早期停止など）が長文脈推論に与える影響を評価しています。
- 2025-10-13：What Generative Search Engines Like and How to Optimize Web Content Cooperatively
	- 著者：Yujiang Wu et al.
		- リンク： [https://arxiv.org/abs/2510.11438](https://arxiv.org/abs/2510.11438)
		- 概要：生成系検索（Generative Engines）の普及に伴う Generative Engine Optimization（GEO）の需要を背景に、生成エンジンが好む性質を学習し、Webコンテンツを書き換える AutoGEO を提案します。フロンティア LLM に「好み」を説明させて規則を抽出し、その規則をプロンプト型 GEO（AutoGEO\_API）の文脈として利用する方法と、規則ベース報酬として小型モデル（AutoGEO\_Mini）を学習する方法を示し、GEO-Bench 等で効果を検証しています。
- 2025-10-14：A Survey of Vibe Coding with Large Language Models
	- 著者：Yuyao Ge et al.
		- リンク： [https://arxiv.org/abs/2510.12399](https://arxiv.org/abs/2510.12399)
		- 概要：コードを逐一読むのではなく、AI生成実装を出力観察で検証する開発様式として “Vibe Coding” を位置づけ、その生産性低下や協働上の課題を踏まえて体系的サーベイを行います。1000本超の研究を俯瞰し、コーディング用 LLM、エージェント、環境、フィードバック機構などの構成要素を整理し、さらに人・プロジェクト・エージェントの関係を制約付き MDP で定式化し、開発モデルの分類（会話反復、計画駆動、テスト駆動、文脈強化等）を提示します。成功要因として、エージェント能力だけでなく体系的なコンテキストエンジニアリングと環境整備・協働モデルを挙げています。
- 2025-10-23：ImpossibleBench：Measuring LLMs’ Propensity of Exploiting Inconsistencies Between Specifications and Unit Tests
	- 著者：Ziqian Zhong et al.
		- リンク： [https://arxiv.org/abs/2510.20270](https://arxiv.org/abs/2510.20270)
		- 概要：LLMエージェントがタスク達成の「近道」を見つけて評価をすり抜ける（例：失敗テストの削除）挙動を問題視し、これを定量化する ImpossibleBench を提案します。仕様（自然言語）と単体テストが直接矛盾する “impossible” 変種を既存ベンチ（LiveCodeBench, SWE-bench 等）から作り、合格が仕様違反を意味する状況で「チート率」を測定します。加えて、プロンプト設計やテストアクセス、フィードバックループ等のコンテキストエンジニアリングがチート率に与える影響分析や、監視ツール開発の試験場としての有用性を示します。
- 2025-10-25：Context Engineering for AI Agents in Open-Source Software
	- 著者：Seyedmoein Mohsenimofidi et al.
		- リンク： [https://arxiv.org/abs/2510.21413](https://arxiv.org/abs/2510.21413)
		- 概要：ソフトウェア開発用 AI エージェントに対して、プロジェクト固有の構造・規約・ワークフロー等の十分なコンテキスト提供が課題であるとし、ツール固有の設定 Markdown（例：自動でプロンプトに追加されるファイル）や [AGENTS.md](http://agents.md/) の動向に着目します。466 の OSS プロジェクトを対象に、AI 設定ファイルの採用状況、記載内容、提示形式、時間変化を予備的に調査し、構造の標準化がまだ確立していないことや、記述スタイルの多様性（記述的・規範的・禁止的・説明的・条件付き等）を報告します。
- 2025-10-25：Hollywood Town: Long-Video Generation via Cross-Modal Multi-Agent Orchestration
	- 著者：Zheng Wei et al.
		- リンク： [https://arxiv.org/abs/2510.22431](https://arxiv.org/abs/2510.22431)
		- 概要：長尺動画生成に向け、映画制作に着想を得た階層・グラフ型のマルチエージェント枠組み OmniAgent を提案し、専門分化とスケーラブルな協調を狙います。さらに、個々のエージェントが必要な文脈を持たない場合に一時的なグループ討議を行う仕組み（ハイパーグラフノード）を導入し、個別メモリ負担を抑えつつ十分なコンテキスト共有を可能にすると述べます。DAG から限定リトライ付きの有向サイクルへ移行して、後段からのフィードバックで反復的に改善する設計も提案しています。
- 2025-10-31：Context Engineering 2.0: The Context of Context Engineering
	- 著者：Qishuo Hua et al.
		- リンク： [https://arxiv.org/abs/2510.26493](https://arxiv.org/abs/2510.26493)
		- 概要：コンテキストエンジニアリングを「エージェント時代の新概念」とみなしがちな見方に対し、関連実践は 20 年以上の系譜を持つと主張し、歴史的段階（1990年代以降）を整理します。文脈が人間—人間だけでなく人間—機械相互作用の中で重要になってきたという問題設定のもと、概念の位置づけ、体系的定義、実践上の主要設計論点を提示し、今後の発展可能性を論じます。

## 2025-11

- 2025-11-21：How agents can use filesystems for context engineering
	- 著者：Nick Huang
		- リンク： [https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/)
		- 概要：エージェント失敗要因のうち「適切なコンテキストにアクセスできない」問題に焦点を当て、コンテキストエンジニアリングを「次のステップに必要な情報を適切にコンテキストへ入れる」作業として位置づけます。ファイルシステムを読み書きする道具立てを与え、長い履歴・中間生成物・メモ等を外部化して必要時に再参照できるようにする設計意図と、その有効性を解説します。
- 2025-11-22：Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction
	- 著者：Debashish Chakraborty et al.
		- リンク： [https://arxiv.org/abs/2511.17908](https://arxiv.org/abs/2511.17908)
		- 概要：RAG において長大・ノイズの多い文脈が有効注意範囲を超えると精度が落ちる一方、既存の事前フィルタがヒューリスティックで統計的制御がない点を課題とします。conformal prediction を用いた coverage（関連証拠を一定割合で残す保証）付きフィルタリングにより、関連性を保ちつつ不要文脈を削減する枠組みを提示し、NeuCLIR と RAGTIME で検証します。ターゲット coverage を満たしながら文脈量を 2〜3 倍削減し、NeuCLIR での下流の事実性指標（ARGUE F1）が改善または安定することを報告しています。
- 2025-11-24：Concept than Document: Context Compression via AMR-based Conceptual Entropy
	- 著者：Kaize Shi et al.
		- リンク： [https://arxiv.org/abs/2511.18832](https://arxiv.org/abs/2511.18832)
		- 概要：RAG 等での長文脈入力が冗長性と計算負荷を増やし推論精度も損ねる問題に対し、AMR（Abstract Meaning Representation）グラフを用いた教師なし文脈圧縮を提案します。AMR ノードの概念的重要度を node-level entropy（conceptual entropy）で推定し、重要ノードを選別して意味を保った凝縮コンテキストを構成します。PopQA と EntityQuestions で、文脈長を大幅に短縮しつつ精度が既存手法を上回ると報告しています。
- 2025-11-25：Interactive AI NPCs Powered by LLMs: Technical Report for the CPDC Challenge 2025
	- 著者：Yitian Huang et al.
		- リンク： [https://arxiv.org/abs/2511.20200](https://arxiv.org/abs/2511.20200)
		- 概要：CPDC 2025（Commonsense Persona-Grounded Dialogue Challenge）参加の技術報告として、GPU Track と API Track の双方で有効だった統一的枠組みを述べます。コンテキストエンジニアリングとして、動的なツール選別（tool pruning）や persona clipping による入力圧縮、加えてパラメータ正規化・関数マージ等の後処理と手動調整プロンプトを組み合わせ、ツール呼び出し安定性・実行信頼性・ロールプレイ誘導を改善したとします。GPU Track では SFT ではなく GRPO による強化学習で報酬最適化し、小標本過学習を抑えつつタスク指向対話性能を向上させたと報告しています。
- 2025-11-26：Effective harnesses for long-running agents
	- 著者：Anthropic（Engineering at Anthropic）
		- リンク： [https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
		- 概要：長時間タスクでは複数のコンテキストウィンドウを跨ぐ必要があり、各セッション開始時に「直前までの記憶がない」ことが根本課題になると整理します。その上で、初回に環境を整える initializer agent と、各セッションで増分の前進と次回のための明確な成果物（アーティファクト）を残す coding agent の二段構成により、セッション間の断絶を埋めるハーネス設計を述べています。
- 2025-11-28：Resolving Evidence Sparsity: Agentic Context Engineering for Long-Document Understanding
	- 著者：Keliang Liu et al.
		- リンク： [https://arxiv.org/abs/2511.22850](https://arxiv.org/abs/2511.22850)
		- 概要：長文書（複数ページ・複数モダリティ）では手がかりが分散し冗長入力が判断を阻害するため、単ページ中心の VLM の性能が低下する点を課題とします。RAG によるページ選別でも冗長性が残るとして、SLEUTH（retriever と 4 つの協調エージェント）による coarse-to-fine の多エージェント枠組みを提案します。取得ページからテキスト・視覚手がかり（表・図等）を抽出・選別し、クエリ分析に基づく推論戦略の構築を経て、証拠密度の高いマルチモーダル文脈を合成し、複数ベンチで性能向上（SOTA）を報告しています。
- 2025-11：Context Engineering: Sessions & Memory
	- 著者：Kimberly Milam and Antonio Gulli
		- リンク： [https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory)
		- 概要：本ホワイトペーパーは、ステートフルでインテリジェントなLLMエージェントを構築する上での「セッション」と「メモリ」の重要な役割を探求します。LLMが対話を記憶し、学習し、パーソナライズできるようにするために、開発者はコンテキストウィンドウ内で情報を動的に組み立て管理する必要があり、このプロセスを「コンテキストエンジニアリング」と呼びます。

## 2025-12

- 2025-12-03：Invasive Context Engineering to Control Large Language Models
	- 著者：Thomas Rivasseau
		- リンク： [https://arxiv.org/abs/2512.03001](https://arxiv.org/abs/2512.03001)
		- 概要：長文脈ほど jailbreak の確率が高まるなど、嗜好学習・プロンプト・入出力フィルタだけでは濫用耐性が十分でないという問題意識を示します。学習を伴わず、コンテキスト内に制御文（control sentences）を挿入する invasive context engineering を提案し、これを chain-of-thought に一般化して scheming を抑制できる可能性を述べます。
- 2025-12-04：Architecting efficient context-aware multi-agent framework for production
	- 著者：Google Developers Blog
		- リンク： [https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/)
		- 概要：本番運用のマルチエージェントで、単に長いコンテキストを渡すのでなく、セッション・メモリ・成果物などを階層化し「コンパイルされたコンテキスト」として組み立てる設計を扱います。変換プロセッサ、圧縮・キャッシュ、スコープ付きハンドオフ等を用いて、コストと信頼性を両立させる方針が述べられています。
- 2025-12-05：Everything is Context: Agentic File System Abstraction for Context Engineering
	- 著者：Xiwei Xu et al.
		- リンク： [https://arxiv.org/abs/2512.05470](https://arxiv.org/abs/2512.05470)
		- 概要：課題が微調整からコンテキストエンジニアリング（外部知識・メモリ・ツール・人間入力をどのように取得・構造化・統治するか）へ移ったとし、プロンプト/RAG/ツール統合が断片化し追跡可能性や説明責任が弱い点を問題視します。Unix の “everything is a file” に着想を得て、文脈アーティファクトを永続的かつ統治可能に扱うファイルシステム抽象（マウント、メタデータ、アクセス制御の統一）を提案します。AIGNE 上で Context Constructor/Loader/Evaluator を備える検証可能パイプラインとして実装し、メモリエージェントと MCP ベースの GitHub アシスタントを例示します。
- 2025-12-15：Memory in the Age of AI Agents
	- 著者：Yuyang Hu et al.
		- リンク： [https://arxiv.org/abs/2512.13564](https://arxiv.org/abs/2512.13564)
		- 概要：基盤モデルエージェントにおける記憶（memory）研究が急増する一方、動機・実装・評価が多様で用語も曖昧になっているとして、最新の見取り図を与えることを目的とします。agent memory の範囲を明確化し、LLM memory、RAG、コンテキストエンジニアリングなど近接概念との区別を示した上で、forms・functions・dynamics の統一的観点から整理します。
- 2025-12-18：PAACE: A Plan-Aware Automated Agent Context Engineering Framework
	- 著者：Kamer Ali Yuksel
		- リンク： [https://arxiv.org/abs/2512.16970](https://arxiv.org/abs/2512.16970)
		- 概要：計画・ツール利用・内省・外部知識との相互作用を含む多段ワークフローでは、コンテキストが急速に肥大化し注意希釈や推論コスト増を招くとして、単純な要約やクエリ依存圧縮では plan-aware な性質を十分扱えないと指摘します。PAACE を、次に実行する k タスクへの関連度モデリング、計画構造解析、指示の共同洗練、機能保存型圧縮などで、エージェント状態として進化する文脈を最適化する統一枠組みとして提案します。
- 2025-12-26：Context Engineering Lessons from Building Azure SRE Agent
	- 著者：sanchitmehta（Microsoft）
		- リンク： [https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200)
		- 概要：多数のツール／専門エージェントを増やすよりも、「いつ・何を・どの形式でコンテキストに入れるか」を徹底的に設計することが、運用上の信頼性に直結したという経験則をまとめます。結果としてツールとエージェント編成を絞り込み、プロダクションでの成果に繋げた、という観点からコンテキストエンジニアリングの実務上の要点を提示します。
- 2025-12-27：Monadic Context Engineering
	- 著者：Yifan Zhang, Mengdi Wang
		- リンク： [https://arxiv.org/abs/2512.22431](https://arxiv.org/abs/2512.22431)
		- 概要：既存のエージェント実装が命令的かつ場当たり的であり、状態管理・エラー処理・並行性で脆弱になりがちだと問題提起します。Functor/Applicative Functor/Monad といった代数的構造を基盤に、ワークフローを「計算的コンテキスト」として扱い、状態伝播や短絡的エラー処理、非同期実行などの横断的関心事を抽象の性質として内在化させる Monadic Context Engineering を提案します。
		- 補足：モナド（monad）は圏論に由来し、関数型プログラミング言語の基礎として広く活用されている概念です。
- 2025-12-29：AI Meets Brain: A Unified Survey on Memory Systems from Cognitive Neuroscience to Autonomous Agents
	- 著者：Jiafeng Liang et al.
		- リンク： [https://arxiv.org/abs/2512.23343](https://arxiv.org/abs/2512.23343)
		- 概要：認知神経科学とAIエージェントの両観点での「記憶」を橋渡しするサーベイ。メモリの保管や更新、攻撃・防御など各トピックで整理。

## 変更ログ

- 2026-01-03: 初版を公開
- 2026-01-05：「2025-12-29：AI Meets Brain: A Unified Survey on Memory Systems from Cognitive Neuroscience to Autonomous Agents」を追加

## 高評価して応援しよう！

- [
	#コンテキストエンジニアリング
	](https://note.com/hashtag/%E3%82%B3%E3%83%B3%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0)