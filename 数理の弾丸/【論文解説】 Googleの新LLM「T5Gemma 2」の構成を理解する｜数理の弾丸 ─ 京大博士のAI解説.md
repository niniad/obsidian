---
title: "【論文解説】 Googleの新LLM「T5Gemma 2」の構成を理解する｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/ne1aa866e0fb3"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2025-12-28
created: 2026-03-14
description: "T5Gemma 2は2025年12月18日にGoogle DeepMindが発表した新しいLLMです。最近のLLMの中では非常に珍しく、エンコーダ・デコーダ型のアーキテクチャが採用されています。  事前学習済みのモデルがHuggingFace（またはKaggle）経由でダウンロードできます。モデル名はt5gemma-2-{e}-{d}という表記になっており、eがエンコーダ側のパラメータ数、dがデコーダ側のパラメータ数を表します。  T5Gemma 2 - a google CollectionWe’re on a journey to advance and democra"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/239476398/rectangle_large_type_2_53d6671f764573b636a82fd6ee8ca575.jpeg?width=1280)

## 【論文解説】 Googleの新LLM「T5Gemma 2」の構成を理解する

参加中

![画像](https://assets.st-note.com/img/1766913417-3sPZuK4zOSjyGLTxteo0hCvi.png?width=1200)

[T5Gemma 2](https://blog.google/technology/developers/t5gemma-2/) は2025年12月18日にGoogle DeepMindが発表した新しいLLMです。最近のLLMの中では非常に珍しく、エンコーダ・デコーダ型のアーキテクチャが採用されています。

事前学習済みのモデルがHuggingFace（またはKaggle）経由でダウンロードできます。モデル名はt5gemma-2-{e}-{d}という表記になっており、eがエンコーダ側のパラメータ数、dがデコーダ側のパラメータ数を表します。

要素技術はGoogleによる既存のモデル Gemma 3（こちらはデコーダ型LLMです）から引き継いでいる部分も多くありますが、エンコーダの双方向注意による長文脈理解の可能性を示唆する非常に興味深いモデルだと思っています。

モデルアーキテクチャは下図の通りです：

ここから先は有料部分です

![画像](https://assets.st-note.com/img/1766911901-fHtXmWTdiF0k47GDr3QCKnVO.png?width=1200)

T5Gemma 2のアーキテクチャ

左側のブロックがエンコーダ、右側のブロックがデコーダです。エンコーダにはSigLIP画像エンコーダ\[Zhai+ 2023\]が搭載されおり、画像・テキストの両方を入力することができます。また、エンコーダ・デコーダともに、Gemma 3のパラメータ値で初期化してから事前学習を行なっています。

![画像](https://assets.st-note.com/img/1766912293-30nZC6LvWAToYm7atfqSsruI.png?width=1200)

アーキテクチャ要素の中でGemma 3から引き継いでいる部分を整理します：

- Positional Interpolation（Chen et al., 2023）
- Grouped Query Attention（Ainslie et al., 2023；Dehghani et al., 2023）
- RMSNormを用いた事前・事後ノルム（Zhang and Sennrich, 2019）
- RoPEによる位置エンコーディング（Su et al., 2024）
- 5:1の比率で交互に配置されたローカルおよびグローバルアテンション層

最後の点について、ここでローカルと言っているのはSliding Window Attentionのことです。

![画像](https://assets.st-note.com/img/1766912249-fhORe87VHvnYLdm3WxZ5zwkb.png?width=1200)

エンコーダ・デコーダいずれも、アテンションとFFNを持つブロックをいくつも積み重ねたネットワークなわけですが、そのアテンションの配置が「local×5 → global×1」を繰り返す形になっています。

![画像](https://assets.st-note.com/img/1766912456-JN3tVI7vrkago1ApU0HK8SsM.png?width=1200)

また、T5Gemma 2に固有の新たな手法は次の2つです。

- Tied embedding：エンコーダとデコーダで埋め込みを共有
- Merged cross/self-attention：デコーダの自己注意・交差注意をひとつのアテンションに統合

いずれも、大きな性能劣化なくパラメータを節約するのに有効である手法として導入されています。Merged attentionの要点は次の通りです。

- クエリはデコーダ出力から作る
- キーとバリューはデコーダ出力Dとエンコーダ出力Eの連結 \[D:E\] から作る
- デコーダ由来の部分のみ因果マスクを適用する

つまりは、デコーダでの直前の計算結果とエンコーダ出力をまるっと混ぜ合わせるアテンションであり、デコーダ由来の部分だけマスク付き自己注意と同様に因果マスク（自分より後ろの位置にあるトークンには注意を向けられない）を適用しています。

以上 T5Gemma 2 の要点を整理しました。いまのところ4B・4Bモデルが最大サイズですが、どこまでスケールできるのかや、同サイズのデコーダ型モデルとの比較が引き続き気になるところです。

---

数理の弾丸は、京大情報系の博士課程と企業のAIエンジニアを掛け持つ投稿者が、人工知能や言語にまつわる学術知をわかりやすく、誤魔化さずに伝えることを目指すYouTubeチャンネルです。