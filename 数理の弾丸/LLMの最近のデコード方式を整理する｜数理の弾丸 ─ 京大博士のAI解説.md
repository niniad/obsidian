---
title: "LLMの最近のデコード方式を整理する｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/na6b31fdcf5a8"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2025-12-19
created: 2026-03-14
description: "Transformerデコーダ型のLLMは各ステップでトークンの確率分布を予測し、その確率分布からなんらかの方法でトークンを選び出すことでテキスト生成を行います。  確率分布を基にトークンを選び出す手法としてGreedy法やビームサーチがよく使われていましたが、最近はほとんど全てのモデル（または推論エンジン）でサンプリングによる生成がデフォルト・推奨値になっています（gpt-oss、DeepSeek（V3.2）、Llama など）。"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/237475534/rectangle_large_type_2_20a89780de9689ff30a0f5f835d9e64c.jpeg?width=1280)

## LLMの最近のデコード方式を整理する

[数理の弾丸 ─ 京大博士のAI解説](https://note.com/mathbullet)

2025年12月19日 21:31

参加中

![画像](https://assets.st-note.com/img/1766147374-HZmQpDtgXlzMwKk457YqbNCu.png?width=1200)

Transformerデコーダ型のLLMは各ステップでトークンの確率分布を予測し、その確率分布からなんらかの方法でトークンを選び出すことでテキスト生成を行います。

確率分布を基にトークンを選び出す手法としてGreedy法やビームサーチがよく使われていましたが、最近はほとんど全てのモデル（または推論エンジン）でサンプリングによる生成がデフォルト・推奨値になっています（ [gpt-oss](https://huggingface.co/openai/gpt-oss-120b/blob/main/generation_config.json) 、 [DeepSeek](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/generation_config.json) （V3.2）、 [Llama](https://github.com/Meta-Llama/llama/blob/main/example_chat_completion.py) など）。

ここから先は有料部分です

この記事では、LLMの出力する語彙数次元のベクトル（logit）からサンプリングによってトークンを選出する手法と、それにまつわる基本的な用語理解を目指します。

- 温度付きサンプリング
- Top-k サンプリング
- Nucleus サンプリング（Top-p サンプリング）

## サンプリングとは

与えられた確率分布を基に特定の標本（ここではトークン）を選び出すことをサンプリングと呼びます。選出は確率的に行われるので、同じ分布からサンプリングしても毎回結果が異なる可能性があります。

語彙全体を $\mathbb{V}$ とすると、LLMの出力するベクトル（ロジットベクトル）は語彙数次元 $|\mathbb{V}|$ であり、この各成分が各トークンに対する予測スコアと解釈できます。これにソフトマックス関数を適用することで、トークンの確率分布 $P(x_{\mathsf{input}})$ が得られます（ただし $x_\mathsf{input}$ を入力トークン列とします）。ソフトマックスによって、下図のようにかなりピーキーな分布になるイメージです。

![画像](https://assets.st-note.com/img/1766144838-EQIiam05SNvfXWn7lyCRp3Fw.png?width=1200)

この分布 $P(x_{\mathsf{input}})$ からトークンをサンプリングすることで次トークンを選出するというのが現状のスタンダードです。ただ、上記の分布から素朴にサンプリングするというケースは珍しく、温度・Top-K、Nucleusという3つがよく併用されます。以降でこれらについて整理します。

## 温度付きサンプリング

LLMのAPIとかでtemperature（温度）パラメータをいじることは多いと思うので、これは馴染みがある方も多いのではないかと思います。要は温度を高くすると確率の低いトークンも比較的選びやすくなり、出力がより多様で大胆になるという仕掛けです。

あるステップでのロジットベクトルを $\mathbf{z}=[z_{1}, z_{2}, \ldots , z_{|\mathbb{V}|}]$ とします。温度 $\tau>0$ を導入した確率分布 $p_\tau$ は、ロジットに対するスケーリングとして次で定義されます。

$p_\tau(i \mid x_{\mathrm{input}}) =\frac{\exp\left(z_i(x_{\mathrm{input}})/\tau\right)}{\sum_{j\in\mathbb{V}}\exp\left(z_j(x_{\mathrm{input}})/\tau\right)} \quad (i\in\mathbb{V})$

$\tau$ を大きくすることで分布が均され、より下位のトークンが選ばれやすくなることが下の図でわかると思います。

![画像](https://assets.st-note.com/img/1766144175-ArvykcMeHJhIWEiVTg2t7DSw.png?width=1200)

τ=0.2

![画像](https://assets.st-note.com/img/1766144191-9O2lsI06mMwrjNgGxzpJfF3U.png?width=1200)

τ=0.5

![画像](https://assets.st-note.com/img/1766144204-sx4w70TFWpJDXgm26GuVfnHU.png?width=1200)

τ=1.0

温度のデフォルト値はモデルによって結構まちまちで、たとえばgpt-ossやDeepSeekは1.0、Llamaは0.6となっています。

## Top-K サンプリング

Top-K サンプリングは、ロジットが上位K件以内のトークンのみを対象としてサンプリングする手法です。普通は64とか128とかそれくらいに設定すると思いますが、例示のためにK=4とすると、下図のグレーアウトされたトークンはサンプリングの対象外となるイメージです。

![画像](https://assets.st-note.com/img/1766145208-zPiIK2W1OeTchfbtSALCyrgN.png?width=1200)

Top-K はこの後に説明する Top-p にほぼほぼ代替されつつありますが、たとえば gemma3-12b-it について「もし設定するなら上位64とか」という会話があったりはします（ [link](https://huggingface.co/google/gemma-3-12b-it/discussions/25) ）。

## Top-p サンプリング（Nucleus サンプリング）

Top-p サンプリングは、上位のトークンから順に確率を累積していき、pに達するまでの範囲（これをnucleuと呼ぶことがあります）を対象としてサンプリングする手法です。

例えば下の分布で p を 0.97 に設定したとすると、上位3件のトークンのみが対象となる、という感じです。

![画像](https://assets.st-note.com/img/1766146252-ztLlJRg5xMFW90BNqhQuwYHU.png?width=1200)

藍字が確率、緑字が累積確率

## 各種モデルのデフォルト値・推奨値

主要なモデルのデコード設定を整理してみました。いずれもサンプリングによる生成が採用されています。結構モデルによって様々なのと、この設定がベストであると保証されているわけでもありません。

- gpt-oss（参照： [Hugging Face](https://huggingface.co/openai/gpt-oss-120b/discussions/21) ）
	- 温度：1.0
		- Top-p：1
		- Top-K：指定なし
- DeepSeek-V3.2（参照： [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/generation_config.json) ）
	- 温度：1.0
		- Top-p：0.95
		- Top-K：指定なし
- meta-llama/llam（公式サンプルのデフォルト、参照： [GitHub](https://github.com/Meta-Llama/llama/blob/main/example_chat_completion.py?utm_source=chatgpt.com) ）
	- 温度：0.6
		- Top-p：0.9
		- Top-K：指定なし
- Qwen3-30B-A3B-Instruct-2507（参照： [Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/generation_config.json?utm_source=chatgpt.com) ）
	- 温度：0.7
		- Top-p：0.8
		- Top-K：20
- Magistral-Small-2509（参照： [Hugging Face](https://huggingface.co/mistralai/Magistral-Small-2509/blob/main/generation_config.json?utm_source=chatgpt.com) ）
	- 温度：0.7
		- Top-p：0.95
		- Top-K：指定なし
- gemma-3-12b-it（参照： [Hugging Face](https://huggingface.co/google/gemma-3-12b-it/discussions/25) ）
	- 温度：1.0
		- Top-p：0.95
		- Top-K：64

## まとめ

この記事では、LLMの標準的なデコード方式であるサンプリングについて、既存実装を理解したり動かす際に必要な前提を整理しました。

---

数理の弾丸は、京大情報系の博士課程と企業のAIエンジニアを掛け持つ投稿者が、人工知能や言語にまつわる学術知をわかりやすく、誤魔化さずに伝えることを目指すYouTubeチャンネルです。

[**数理の弾丸⚡️京大博士のAI解説** *サイバネティック・エデュケーショナルハードコア* *youtube.com*](https://youtube.com/@mathbullet?si=cJppEHdt6a1k1oxN)

## 高評価して応援しよう！

- [
	#LLM
	](https://note.com/hashtag/LLM)