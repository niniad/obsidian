---
title: ".envファイルの送り合いから脱却する【dotenvx】｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/n4429a12f8aea"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2025-12-31
created: 2026-03-14
description: "このツイートの引用元でdotenvxなるツールを知りまして、そこからしばらく使っていたのですが結構良いと思ったので共有します。JS/TSのプロジェクトでは環境変数の注入にdotenvを使うのがデファクトだと思いますが、同じ開発チームによるセキュア版とのことです。                             ありそうでなかったやつだ… これ使うのは躊躇するのにDMとかで.env送るのは躊躇しない俺の謎脳 https://t.co/HwdjBUxdJt — 数理の弾丸⚡️YouTubeでAI解説 (@_mathbullet) December 3, 2025"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/240282960/rectangle_large_type_2_ab3ad2d71bb4840399fc1b61680f176f.jpeg?width=1280)

## .envファイルの送り合いから脱却する【dotenvx】

参加中

![画像](https://assets.st-note.com/img/1767170392-9rRd0ho5FNxKLEcUnt67Aauw.png?width=1200)

このツイートの引用元で [dotenvx](https://dotenvx.com/) なるツールを知りまして、そこからしばらく使っていたのですが結構良いと思ったので共有します。JS/TSのプロジェクトでは環境変数の注入に [dotenv](https://github.com/motdotla/dotenv) を使うのがデファクトだと思いますが、同じ開発チームによるセキュア版とのことです。

## dotenvxとは

dotenvxは環境変数の注入・共有を安全に行うためのツールです。複数名で開発する際には特に、.envファイルをDMなどで送り合うという便利だが不安な運用が放置されがちです。dotenvxを使うことで、開発メンバー間で解読用の鍵を共有し、その鍵さえ持っていればシームレスに環境変数を共有できるようになります。

基本的な運用方式は下図のとおりです。

![画像](https://assets.st-note.com/img/1767171532-DJUncxH8qvz6X75TLIBgpZsy.png?width=1200)

環境変数が記載された.envファイルは、暗号化された状態でGitHubリポジトリなどのリモートにプッシュしてしまいます。そして、.envを解読するための秘密鍵は世間に公開されないよう、開発メンバーのローカルのみで保持します。

この方式によって、新たに環境変数を追加した際に.envをコッソリ渡す、みたいなことをすることなく、.envをメンバーと共有することができます（コッソリ共有する必要があるのは秘密鍵を最初に渡すときだけになります）。

## 基本的な使い方

npxやbrewなど各種インストール方法が [こちら](https://dotenvx.com/docs/install) に記載されています。brewなら下記コマンドでいけます：

```
brew install dotenvx/brew/dotenvx
```

例えば下記が記載された.envファイルがあるとします。

```python
# .env
SAMPLE_KEY=12345abcde
```

.envにはAPIキーなどの認証情報を書くわけなので、常識的にはこのファイルは絶対にリモートへプッシュしてはいけないわけなのですが、dotenvxを使う場合はこれを暗号化してプッシュしてしまいます。

暗号化は次のコマンドで行います。

```
dotenvx encrypt
```

すると、.envファイルが次のように書き変わり、同時に秘密鍵が記載された.env.keysが生成されます。

```python
#/-------------------[DOTENV_PUBLIC_KEY]--------------------/
#/            public-key encryption for .env files          /
#/       [how it works](https://dotenvx.com/encryption)     /
#/----------------------------------------------------------/
DOTENV_PUBLIC_KEY={公開鍵}

# .env
SAMPLE_KEY=encrypted:{暗号化されたキー}
```

.env.keysは.envを解読するための秘密鍵なので、これは絶対にプッシュしてはいけません。開発メンバー間で大事に共有・秘匿する必要があります。

.env.keysを持っていれば、例えば次のコマンドで変数の値を読み出すことができます（.env.keysがないとエラーになります）。

```javascript
❯ dotenvx get SAMPLE_KEY
12345abcde
```

また、dotenv（よく使われている環境変数の注入ライブラリ）と同様、プロセス環境変数として注入されているわけなので、process.env.SAMPLE\_KEYでも取得可能です。

例えば下記の内容でindex.jsを作成したとします。

```javascript
console.log(\`サンプルキー: ${process.env.SAMPLE_KEY}\`);
```

下記のように実行すれば値を取得できます。要はdotenvと同じ使用感です。

```
❯ dotenvx run -- node index.js
[dotenvx@1.51.4] injecting env (2) from .env
サンプルキー: 12345abcde
```

基本的な使い方は以上です。環境変数は開発の過程で追加されたり値が変わったりすることもあると思います。その際にリモートへプッシュして共有するだけで済むのはかなり体験が良いと思います。暗号化し忘れるのだけメチャクチャ怖いので、pre-commitまたはpre-pushとして暗号化を差し込むのは必須だと思います。

また、.env.keysを保持するという運用は開発環境にかぎった話で、本番環境ではAWSなりAzureなりの環境変数設定で DOTENV\_PRIVATE\_KEY という名前で鍵の値を登録するのが基本想定です。

## 注意点まとめ

上記の繰り返しになりますが、なんやかんや注意すべき点はあるので整理します。

- 暗号化は勝手に行われるわけではないので、pre-commitまたはpre-pushとして暗号化を差し込むのは必須
- .env.keysファイル（秘密鍵）を絶対に公開しない
- 本番環境では、環境に.env.keysを置くのではなくDOTENV\_PRIVATE\_KEYという名前で秘密鍵の値を登録する（Azure Key Vaultなどキー管理用のサービスを利用する）

## 細々としたコマンド

環境変数を.envファイルに書き込む（暗号化なし）：

```cpp
dotenvx set API_KEY "xxxx"
```

環境変数を.envファイルに書き込む（暗号化あり）：

```cpp
dotenvx set API_KEY "xxxx" --encrypt
```

環境変数の値を標準出力：

```javascript
dotenvx get {変数名}
```

## まとめ

この記事では、dotenvxによる安全な環境変数の共有・管理について要点を整理しました。他にも良いツールがあればぜひ教えて欲しいです〜！

---

数理の弾丸は、京大情報系の博士課程と企業のAIエンジニアを掛け持つ投稿者が、人工知能や言語にまつわる学術知をわかりやすく、誤魔化さずに伝えることを目指すYouTubeチャンネルです。