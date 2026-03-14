---
title: "GPT OSSのファインチューニング with unsloth｜数理の弾丸 ─ 京大博士のAI解説"
source: "https://note.com/mathbullet/n/nba59419658ec"
author:
  - "[[数理の弾丸 ─ 京大博士のAI解説]]"
published: 2026-01-14
created: 2026-03-14
description: "unslothは大規模モデルの軽量な学習・推論をサポートするPythonライブラリです。様々な大規模モデルの最適化版や、量子化・LoRAなどの学習効率化手法、推論エンジンとの連携などを提供しています。  これ永遠に言ってるんですが、とにかくunslothはドキュメントが充実しています。Colab実装も大量に公開されていて、気になる手法をすぐに試すことができます。  OpenAIのGPT OSS 20BはLLMでいうと中の下くらいのパラメータサイズですが、素朴にロードするとそれだけで14GBくらいのメモリを使います。Colabの最小GPUであるT4は16GBなので、学習時に消費するメモリ"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/243652048/rectangle_large_type_2_7f0eb1707050ecca4cc5a66b28ba0b34.jpeg?width=1280)

## GPT OSSのファインチューニング with unsloth

参加中

![画像](https://assets.st-note.com/img/1768317112-2xI8s5ESXBp4H9uOC3vncJfL.png?width=1200)

unslothは大規模モデルの軽量な学習・推論をサポートするPythonライブラリです。様々な大規模モデルの最適化版や、量子化・LoRAなどの学習効率化手法、推論エンジンとの連携などを提供しています。

これ永遠に言ってるんですが、とにかくunslothは [ドキュメント](https://unsloth.ai/docs) が充実しています。 [Colab実装](https://unsloth.ai/docs/get-started/unsloth-notebooks) も大量に公開されていて、気になる手法をすぐに試すことができます。

OpenAIのGPT OSS 20BはLLMでいうと中の下くらいのパラメータサイズですが、素朴にロードするとそれだけで14GBくらいのメモリを使います。Colabの最小GPUであるT4は16GBなので、学習時に消費するメモリまではカバーしきれません。Unsloth（というか量子化やLoRAなどの軽量化手法）を使うことで、T4でも20B級のLLMの学習を行うことができます。

T4でGPT OSS 20Bの学習を行うノートブックは [こちら](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb) にunsloth公式のものが公開されています。上から動かしていけば普通に動くのですが、挙動をちゃんと追うには必要な前提知識が結構あります。そこでこの記事では、単に公式実装をなぞっていくのではなく、コードの挙動や入出力を理解するために必要な前提を整理し、公式コードでは書かれていない派生的な内容も含めて解説していきます。

---

そもそものGPT OSSについてはこちらの動画で解説しています：

![](https://www.youtube.com/watch?v=v1UvR2-zy1w)

---

## 主なツール構成

ノートブック冒頭で必要なライブラリをひととおりインストールしています。

```python
%%capture
import os, importlib.util
!pip install --upgrade -qqq uv
if importlib.util.find_spec("torch") is None or "COLAB_" in "".join(os.environ.keys()):    
    try: import numpy, PIL; get_numpy = f"numpy=={numpy.__version__}"; get_pil = f"pillow=={PIL.__version__}"
    except: get_numpy = "numpy"; get_pil = "pillow"
    !uv pip install -qqq \
        "torch>=2.8.0" "triton>=3.4.0" {get_numpy} {get_pil} torchvision bitsandbytes "transformers==4.56.2" \
        "unsloth_zoo[base] @ git+https://github.com/unslothai/unsloth-zoo" \
        "unsloth[base] @ git+https://github.com/unslothai/unsloth" \
        git+https://github.com/triton-lang/triton.git@0add68262ab0a2e33b84524346cb27cbb2787356#subdirectory=python/triton_kernels
elif importlib.util.find_spec("unsloth") is None:
    !uv pip install -qqq unsloth
!uv pip install --upgrade --no-deps transformers==4.56.2 tokenizers trl==0.22.2 unsloth unsloth_zoo
```

呪文みたいですが、Colab環境かどうかで条件分岐するようになっているためやや入り組んで見えています。

メインで使用するのはunslothと [trl](https://github.com/huggingface/trl) です。trlはhuggingfaceが提供するファインチューニング・強化学習ライブラリです。

## モデルの定義

unslothのLLMは基本的にFastLanguageModelのインスタンスとして定義します。次の部分です（見やすさのためコメントアウトは除いてあります）。

```python
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gpt-oss-20b",
    dtype = dtype,
    max_seq_length = max_seq_length,
    load_in_4bit = True,
    full_finetuning = False,
)
```

load\_in\_4bit = True によって、モデルパラメータが4bitに低精度化されてロードされます。GPT OSSはMoEのパラメータは元々4bitなので、注意機構を中心にパラメータが低精度化されることになります。

ちなみに、8bitに低精度化するload\_in\_8bitという引数もあります。load\_in\_4bitとload\_in\_8bitを両方TrueにするとRunTimeErrorになります（この引数設計は改善の余地が大きい気がしています）。

full\_finetuning = False によって、モデルパラメータは凍結されます。つまり、モデルの全パラメータは requires\_grad=False に設定さ、このまま学習を実行しても、どのパラメータも更新されません（勾配が計算されません）。公式実装では、いまロードしたモデルにLoRAアダプタを適用します。これにより、追加されたLoRAアダプタが学習パラメータとして振る舞います。

## LoRAアダプタの適用

LoRAについてはこちらの動画をぜひご覧ください。動画内でのΔWをここではLoRAアダプタと呼んでいます。

![](https://www.youtube.com/watch?v=aNGDdUFGE5Q)

LoRAアダプタの適用は次で行います。参考になることが多く書いてあるので公式のコメントアウトもそのまま残しています。

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 8, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```

主なパラメータについて説明します。

target\_modules = \["q\_proj", "k\_proj", "v\_proj", "o\_proj", "gate\_proj", "up\_proj", "down\_proj",\] の部分でLoRAアダプタを適用する線形変換を指定しています。最後の3つはMoE部分の線型変換で、それ以外は注意機構を構成する線形変換です。

主なところで言うと、r はランクを表す引数であり、これを小さくするほどLoRAアダプタは小さくなります（＝学習パラメータが小さくなる）。また、lora\_alpha はLoRAアダプタを元のパラメータに足すときの重みであり、これを大きくするほどLoRAによるファインチューニングの影響が大きくなります。

use\_gradient\_checkpointing はGradient Checkpointingを有効にするかどうかの引数です。Gradient Checkpointingは、LLM内部で計算された中間状態を保存せず、逆伝播時に再計算することでメモリを節約する手法です。

この後、学習用データをGPT OSS用に整形する処理が入り、学習の設定を定義・実行しています。データの整形についてはここでは深入りしませんが、GPT OSSは [Harmony format](https://cookbook.openai.com/articles/openai-harmony) という独自の入出力フォーマットを採用しているので、それに合わせた整形を行なっています。

## 学習の設定

学習はtrlで行います。config を記述するクラスと、trainer クラスを使います。

```javascript
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 30,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none",
    ),
)
```

割とよくある深層学習の学習設定という感じです。公式コードは試験的に動かす意味合いが大きいので、学習を早めに打ち切るためにmax\_steps = 30と設定していますが、num\_train\_epochs =..., という形でエポック数を指定するのが普通だと思います。

## 損失のマスキング

LLMの学習においては、教師データサンプルの入力・出力テキストをまるっとモデルに入力して出力を得るのが一般的です。すると入力（プロンプト）にあたる位置についても何らかの予測トークンが得られることになりますが、これらは損失計算に含めたくないわけです。LLMに正しく予測して欲しいのは出力にあたる位置のトークンだけだからです。

そのため、たいていのLLM学習ライブラリでは、学習データを構成するテキストのどの部分を損失計算に考慮し、どの部分を考慮外とするかを定義するユーティリティが提供されています。

unslothでは次のように書きます。

```javascript
from unsloth.chat_templates import train_on_responses_only

gpt_oss_kwargs = dict(instruction_part = "<|start|>user<|message|>", response_part="<|start|>assistant<|channel|>final<|message|>")

trainer = train_on_responses_only(
    trainer,
    **gpt_oss_kwargs,
)
```

gpt\_oss\_kwargs は、instruction（入力）部分とresponse（出力）部分を示すマーカを格納しています。これとtrainerを引数としてtrain\_on\_responses\_onlyに渡すことで、出力位置のテキストのみを考慮した損失計算が行われるようになります。

ノートブックのこれ以降の部分では、実際に学習を行い、学習前後の出力テキストを比較しています。Colab無料ユーザでも使えるT4で実行可能なので、ぜひやってみてください。

---

数理の弾丸は、京大情報系の博士課程と企業のAIエンジニアを掛け持つ投稿者が、人工知能や言語にまつわる学術知をわかりやすく、誤魔化さずに伝えることを目指すYouTubeチャンネルです。