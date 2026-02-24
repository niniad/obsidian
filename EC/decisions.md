# 意思決定記録（EC / プロジェクト全体）

## 2026-02-25: Obsidian vault リファクタリング

### 背景
Reference/recall/ が Recall アプリの書き出しで 2000+ ファイルに肥大化し、本来の「API仕様・技術リファレンス」用途から逸脱。コンテンツ重複・root 直下の迷子フォルダ・Notion ハッシュ残存など多数の問題があった。目的は AI プロンプト参照に適した長期管理可能な構成への整理。

### 変更内容

**Reference/recall/ の解体・再配置:**
- `recall/Amazonノウハウ/` → `ec/Amazon知識/`
- `recall/{マーケティング,コピーライティング,セールスライティング,ブランディング,販売促進,フレームワーク}` → `ec/マーケティング/`
- `recall/1688/` → `ec/仕入れ/1688/`
- `recall/プロンプト/` → `ec/プロンプト/recall/`
- `recall/マニュアル/` → `ec/マニュアル/recall/`
- `recall/{本,読書,書籍超要約}/` → `private/Books/`
- `recall/論文・公文書/` → `private/Papers/recall/`
- `recall/{スクリーンタイム,デジタルデトックス,社会}/` → `private/研究/`
- `recall/{子育てQ&A,子育て支援サービス,家庭のこと}/` → `private/子育て/`
- `recall/{自己啓発,仕事術,問題解決,目標}/` → `private/学び/`
- `recall/AW/`, `recall/DX/` → `aw/`
- `recall/imports/` → `Reference/AMC/`
- 低価値 (Organization, Person, Movie, Podcast 等) → `archive/recall-misc/`
- `recall/快適物販/`（ec/ 完全重複） → 削除
- `recall/ソース/`（不要） → 削除

**その他の整理:**
- `ec/マニュアル・ノウハウ/` → `ec/マニュアル/`（リネーム）
- root 直下の `books/`, `papers/`, `clippings/` → `private/` に統合（重複除去）
- Notion ハッシュ付き重複ファイル 18件 削除
- `inbox/lovevery/*.py` → `projects/tmp/lovevery/`（Obsidian 外に退避）

### 実行後の vault 構成

```
obsidian/
├── ec/
│   ├── 商品開発/
│   ├── プロンプト/        ← recall/プロンプト/ 統合済み
│   ├── マニュアル/        ← 旧マニュアル・ノウハウ/ + recall/マニュアル/
│   ├── Amazon知識/        ← recall/Amazonノウハウ/ 移動済み
│   ├── マーケティング/    ← recall 各種マーケティング系 統合済み
│   ├── 仕入れ/            ← recall/1688/ 移動済み
│   └── *.md（goal.md, decisions.md, system-architecture.md 等）
├── aw/                    ← recall/{AW, DX} 統合済み
├── private/
│   ├── Books/             ← root books/ + recall/{本,読書,書籍超要約} 統合済み
│   ├── Papers/            ← root papers/ + recall/論文・公文書 統合済み
│   ├── Clippings/
│   ├── lovevery/
│   ├── 研究/              ← recall/{スクリーンタイム,デジタルデトックス,社会}
│   ├── 子育て/            ← recall 子育て系
│   └── 学び/              ← recall 自己啓発系
├── Reference/
│   └── AMC/               ← recall/imports/ 移動済み（本来の用途に戻す）
├── inbox/
├── archive/
│   ├── weekly-journals-2024/
│   └── recall-misc/       ← 低価値 recall コンテンツ
└── tmp/
```

---

## 2026-02-20: ファイル管理・プロジェクト整理の全体方針

### 背景
projects/ 配下のリポジトリが21個に増加し、重複・空・スコープ不明確なものが混在。obsidian vault に164MBのPDFが含まれ git が肥大化。ファイル管理の全体方針が未定義だった。

### 決定事項

#### 1. ファイル管理の役割分担

| ツール | 役割 | 検索方法 |
|---|---|---|
| Obsidian | 思考・メモ（md テキストのみ） | Obsidian 内検索 |
| Google Drive (G:\マイドライブ) | ファイル原本の保管庫（PDF, xlsx, 動画等） | Drive ウェブ全文検索 |
| Eagle (Drive上) | EC クリエイティブ資産の管理（商品画像、ベンチマーク） | タグ + ビジュアル |
| NocoDB | DB レコードの添付ファイル（内部ストレージで自己完結） | API / UI |
| GCS → BigQuery | データパイプライン（SP-API, Ads API 生データ） | SQL |

#### 2. Obsidian vault の構成

```
obsidian/
├── Inbox/        ← 一時保管（定期的に振り分け）
├── EC/           ← EC事業（Amazon個人事業）
├── AW/           ← 本業（AirWater）+ 旧AIDX統合
├── Private/      ← プライベート（Books, Papers, Clippings, lovevery）
├── Reference/    ← API仕様・技術リファレンス（SP-API, Ads, AMC, NocoDB）
└── Archive/      ← 不要になったもの
```

- PDF・画像は vault に置かない（Google Drive に保管し、md からリンク）
- Notion ハッシュ付きファイル名は除去済み
- 日付は ISO 形式（YYYY-MM-DD）

#### 3. Google Drive の構成

```
G:\マイドライブ\
├── AW/           ← AirWater IR資料（有報、株主総会、決算等のPDF）
├── 仕事/         ← EC実務データ（スプレッドシート、CSV）
├── 商品開発/     ← 商品開発の実務ファイル
├── 代行会社共有/  ← 輸入代行会社との共有資料
├── プライベート/  ← 個人ファイル
├── 家族共有/      ← 家族共有ドキュメント
├── Books/        ← 書籍PDF
├── ノート/       ← 手書き日誌PDF
├── Eagle.library/ ← Eagle クリエイティブ資産
└── backup/       ← NocoDB バックアップ等
```

- Drive URL はファイルID ベースなのでフォルダ再編成してもリンク切れない
- ローカルマウント (G:\) 経由で Claude Code から直接読める

#### 4. プロジェクト整理の結果

**削除・統合したリポジトリ:**
- gcp-main-project-477501 → goal.md, system_architecture.md を obsidian/EC/ に移動、スクリプト・Excel を freee/ に移動
- amazon-creative-ops → amazon-creative-workflow に統合
- pu-apron-creative → 削除（中身なし）
- figma-template → 削除（空）
- create-product-planning-skills → 削除（空）
- streamlit-app → 削除（scaffold のみ）
- nocodb → 削除（スキルでカバー）
- amazon_marketing_cloud → obsidian/Reference/AMC に移動

**残プロジェクト:**
- EC: amazon-creative-workflow, product-planning, spapi-to-gcs-daily, amazon-ads-to-gcs-daily, fetch-customs-exchange-rate, freee
- インフラ: n8n
- プライベート: life-plan, self-data-collection, kindle_to_pdf
- 設定: my-settings, obsidian
- 要整理: refactoring-awi-files（AW業務ファイル4,259件、Google Drive移行を検討）

#### 5. Obsidian 画像管理（GCS + 自動アップロード）

- **バケット**: `gs://obsidian-assets`（asia-northeast1、公開読み取り）
- **公開URL形式**: `https://storage.googleapis.com/obsidian-assets/{path}`
- **サービスアカウント**: `obsidian-assets@main-project-477501.iam.gserviceaccount.com`
- **プラグイン**: S3 Image Uploader（HMAC キーでGCSのS3互換APIに接続）
- **画像ペースト時の動作**: 自動でGCSにアップロード → URLに置換
- **BigQuery カタログ**: `assets.v_image_catalog` でURL一覧・検索可能
- **プレビュー**: GCS Console（https://console.cloud.google.com/storage/browser/obsidian-assets）

#### 6. Obsidian Git 自動同期

- **プラグイン**: Obsidian Git (v2.37.1)
- **自動バックアップ**: 10分間隔でコミット＆プッシュ
- **自動プル**: 10分間隔 + 起動時プル
- **コミットメッセージ**: `vault backup: YYYY-MM-DD HH:mm:ss`

#### 7. PC 移行時の手順

1. Google アカウントでログイン → Drive, Eagle 自動復元
2. `C:\Users\ninni\nocodb\` をコピー → NocoDB 復元
3. `git clone` → obsidian, 各プロジェクト復元
