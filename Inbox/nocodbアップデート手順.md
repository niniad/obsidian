# 意思決定記録

## 2026-02-15: NocoDB アップデート手順の確立

### 背景
v0.301.2 へのアップデートを試みたところ、スタンドアロンバイナリに既知のバグ（ipaddr.js パッケージ不足、GitHub Issue #12939）があり起動不可。v0.301.1 にロールバックして復旧。

### 教訓・手順
NocoDB をアップデートする際は以下を必ず実施すること：

1. **GitHub Issues を確認** — 対象バージョンのスタンドアロンバイナリで起動不具合がないか確認
   - https://github.com/nocodb/nocodb/issues で「standalone」「binary」「ERR_MODULE_NOT_FOUND」等を検索
2. **noco.db をバックアップ** — `sqlite3 noco.db ".backup 'G:/マイドライブ/backup/nocodb/noco_backup_YYYYMMDD.db'"`
3. **旧バイナリをリネーム保存** — `Noco-win-x64.exe` → `Noco-win-x64-旧バージョン.exe`（ロールバック用）
4. **新バイナリで起動テスト** — 起動ログを確認、API でベース一覧が返ることを確認
5. **失敗時はロールバック** — 旧バイナリに戻して起動

### 現在の状態
- バージョン: v0.301.1（安定稼働）
- インストール先: `C:\Users\ninni\nocodb\Noco-win-x64.exe`
- DB: `C:\Users\ninni\nocodb\noco.db`
- Docker版は v0.301.2 のバグの影響なし
