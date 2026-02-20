### 方法2：【中級者向け・最も確実な無料策】GitHub ActionsとPlaywright（ブラウザ自動操作）を組み合わせる方法

これは、**本物のブラウザ（Chrome）そのものをプログラムで動かして**情報を取得する方法です。人間がブラウザで操作するのとほぼ同じ動きをするため、Amazonのブロックを回避できる可能性が格段に上がります。

GitHub Actionsの無料枠（月2000分）を使えば、1時間に1回程度の実行なら十分に継続無料で運用できます。

#### ステップバイステップ・マニュアル

これはプログラムがスプレッドシートを読み書きするための「鍵」を発行する作業です。

1. **Google Cloudでプロジェクト作成:** [Google Cloud Console](https://www.google.com/url?sa=E&q=https%3A%2F%2Fconsole.cloud.google.com%2F)にアクセスし、新しいプロジェクトを作成します（名前は自由）。
    
2. **APIの有効化:**
    
    - 左上のメニューから「APIとサービス」>「ライブラリ」に進みます。
        
    - 「**Google Drive API**」と検索して有効化します。
        
    - 同様に、「**Google Sheets API**」と検索して有効化します。
        
3. **サービスアカウントの作成:**
    
    - 「APIとサービス」>「認証情報」に進みます。
        
    - + 認証情報を作成 > サービスアカウント を選択。
        
    - アカウント名を入力し（例: github-actions-writer）、「作成して続行」をクリック。
        
    - 「ロールを選択」で編集者を選び、「続行」>「完了」。
        
4. **キーの取得:**
    
    - 作成したサービスアカウントのメールアドレスをクリックします。
        
    - 「キー」タブ > 鍵を追加 > 新しい鍵を作成 を選択。
        
    - キーのタイプでJSONを選び、「作成」。キーファイル（JSON形式）がPCにダウンロードされます。**このファイルは絶対に他人に渡さないでください。**
        
5. **スプレッドシートの共有設定:**
    
    - 順位を記録したいスプレッドシートを開きます。
        
    - 右上の共有ボタンをクリックします。
        
    - 先ほど作成したサービスアカウントのメールアドレス（例: ...iam.gserviceaccount.com）を「ユーザーやグループを追加」欄に貼り付け、権限を編集者にして共有します。
        

6. [GitHub](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2F)でアカウントを作成し、新しいリポジトリを作成します（名前は自由）。
    

7. 作成したリポジトリで、Add file > Create new file をクリックします。
    
8. ファイル名を main.py とし、以下のPythonコードを貼り付けます。
    

codePython

```
# main.py
import gspread
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random
import os
import json

# --- 設定項目 ---
# 1. Googleスプレッドシートのキー (URLの .../d/【この部分】/edit...)
SPREADSHEET_KEY = 'YOUR_SPREADSHEET_KEY'

# 2. 各要素を特定するためのセレクタ
SELECTORS = {
    'item_container': '[data-component-type="s-search-result"]',
    'sponsored_product_label': 'span[data-component-type="s-sponsored-label"]',
    'asin': '[data-asin]',
}

# --- 関数定義 ---

def get_amazon_ranking(page, target_asin):
    """ブラウザでページを開き、HTMLを解析して順位を返す"""
    result = {'organic_rank': '3ページ以内になし', 'sponsored_product_rank': '3ページ以内になし'}
    organic_counter = 0
    sponsored_counter = 0

    for i in range(1, 4):
        search_url = f"{page.url}&page={i}"
        if i > 1:
            page.goto(search_url, wait_until='networkidle', timeout=60000)
        
        print(f"{i}ページ目の解析を開始...")
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        items = soup.select(SELECTORS['item_container'])
        if not items:
            print("商品リストが見つかりません。ページの構造が変わった可能性があります。")
            break
            
        for item in items:
            asin_elem = item.select_one(SELECTORS['asin'])
            current_asin = asin_elem['data-asin'] if asin_elem and 'data-asin' in asin_elem.attrs else None
            if not current_asin: continue

            is_sponsored = item.select_one(SELECTORS['sponsored_product_label']) is not None
            
            if is_sponsored:
                sponsored_counter += 1
                if current_asin == target_asin and result['sponsored_product_rank'] == '3ページ以内になし':
                    result['sponsored_product_rank'] = sponsored_counter
            else:
                organic_counter += 1
                if current_asin == target_asin and result['organic_rank'] == '3ページ以内になし':
                    result['organic_rank'] = organic_counter
        
        time.sleep(random.uniform(2, 5)) # ページ遷移の間にランダムな待機
        
    return result

# --- メイン処理 ---
def main():
    # サービスアカウントキーを環境変数から読み込む
    gcp_sa_key_str = os.environ.get('GCP_SA_KEY')
    if not gcp_sa_key_str:
        raise ValueError("環境変数 GCP_SA_KEY が設定されていません。")
    
    credentials = json.loads(gcp_sa_key_str)
    gc = gspread.service_account_from_dict(credentials)
    
    # スプレッドシートを開く
    spreadsheet = gc.open_by_key(SPREADSHEET_KEY)
    settings_sheet = spreadsheet.worksheet("設定")
    results_sheet = spreadsheet.worksheet("結果")
    
    # 調査リストを取得 (ヘッダーを除く)
    search_list = settings_sheet.get_all_records()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # headless=Falseにするとブラウザの動きが見える
        page = browser.new_page()

        for item in search_list:
            asin = item.get('ASIN')
            keyword = item.get('キーワード')
            if not asin or not keyword: continue

            print(f"--- 調査開始: ASIN={asin}, キーワード={keyword} ---")
            initial_url = f"https://www.amazon.co.jp/s?k={keyword}"
            page.goto(initial_url, wait_until='networkidle', timeout=60000)
            
            rank_data = get_amazon_ranking(page, str(asin))

            # 結果をスプレッドシートに書き込み
            new_row = [
                str(asin), keyword,
                rank_data['organic_rank'],
                rank_data['sponsored_product_rank'],
                datetime.now().strftime('%Y/%m/%d %H:%M')
            ]
            results_sheet.append_row(new_row)
            print(f"結果を書き込みました: {new_row}")
            time.sleep(random.uniform(5, 10)) # 次のキーワードへ行く前に長めに待機

        browser.close()

if __name__ == '__main__':
    main()
```

1. Commit new fileで保存します。
    

2. リポジトリのSettingsタブ > Secrets and variables > Actions を選択。
    
3. New repository secretをクリック。
    
4. **Name:** GCP_SA_KEY と入力します。
    
5. **Secret:** ステップ1でダウンロードした**JSONファイルの中身を全てコピー**して貼り付けます。
    
6. Add secretをクリック。
    

7. リポジトリのActionsタブをクリックします。
    
8. set up a workflow yourself をクリック。
    
9. ファイル名を scrape.yml に変更し、元々書いてある内容を全て消して、以下のコードを貼り付けます。
    

codeYaml

```
# .github/workflows/scrape.yml
name: Amazon Rank Scraper

on:
  schedule:
    - cron: '30 * * * *' # 毎時30分に実行 (例)
  workflow_dispatch: # 手動でも実行できるようにする

jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
      - name: リポジトリのコードをチェックアウト
        uses: actions/checkout@v3

      - name: Pythonのセットアップ
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Playwrightのブラウザをインストール
        run: |
          pip install playwright
          python -m playwright install --with-deps

      - name: Pythonライブラリのインストール
        run: |
          pip install gspread beautifulsoup4 pandas

      - name: スクレイピング実行
        env:
          GCP_SA_KEY: ${{ secrets.GCP_SA_KEY }} # Secretを環境変数として渡す
        run: python main.py
```

1. Commit changesをクリックして保存します。
    

これで全ての準備が完了です。設定した時間（この例では毎時30分）になると、GitHub Actionsが自動的にPythonスクリプトを実行し、結果をGoogleスプレッドシートに書き込んでくれます。

**この方法は、これまで試した中で最も強力かつ、継続的に無料で運用できる確実な方法です。**