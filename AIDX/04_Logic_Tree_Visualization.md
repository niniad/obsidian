# 時価総額1兆円目標：ロジックツリー（純利益×PERベース）

時価総額1兆円達成に向けた、「利益」と「期待」の分解構造です。

```mermaid
graph TD
    %% Root Goal
    Root["時価総額1兆円 (2030)"] --- L1_Income["連結純利益 (実績)"]
    Root --- L1_PER["PER (評価/期待)"]

    %% Net Income Branch
    L1_Income --- L2_Revenue["売上収益の質の高い成長"]
    L1_Income --- L2_Margin["純利益率の向上 (収益性追求)"]
    
    L2_Revenue --- L3_Shift["高成長軸へのシフト (地球環境/ウェルネス) [事実]"]
    L2_Revenue --- L3_SynRev["事業間クロスセルの創出 [仮説]"]
    
    L2_Margin --- L3_COGS["売上原価の削減 (製造/物流最適化)"]
    L2_Margin --- L3_SGA["販管費の抑制 (全業務30%効率化) [事実]"]

    %% PER Branch
    L1_PER --- L2_Growth["将来成長期待 (g)"]
    L1_PER --- L2_Risk["リスク/予測可能性 (Ke)"]
    L1_PER --- L2_Return["株主還元の規律 (配当性向)"]

    L2_Growth --- L3_Inno["デジタルによる新ビジネス創出 [仮説]"]
    L2_Growth --- L3_PMI["M&A回収の加速 (デジタルPMI) [仮説]"]

    L2_Risk --- L3_Vis["経営の可視化 (透明性による不信解消) [仮説]"]
    L2_Risk --- L3_Stability["ROIC経営による規律の維持 [事実]"]

    L2_Return --- L3_Div["累進配当 / 性向35% [事実]"]

    %% AIDX Intervention Points (Styles)
    style L3_SGA fill:#f9f,stroke:#333,stroke-width:2px
    style L3_COGS fill:#f9f,stroke:#333,stroke-width:2px
    style L3_Vis fill:#f9f,stroke:#333,stroke-width:2px
    style L3_Inno fill:#f9f,stroke:#333,stroke-width:2px

    subgraph AIDX_Intervention ["AIDXの主要介入ポイント"]
        L3_SGA
        L3_COGS
        L3_Vis
        L3_Inno
    end
```

---

## ツリーの解説

### 1. 収益の柱（左側：純利益）
「利益率10%」「業務効率化30%」という経営ノルマを達成し、純利益の絶対額を増やす。
- **AIDXの役割**: 販管費と原価の両面を削り、利益弾力性を高める。

### 2. 期待の柱（右側：PER）
「稼いだ利益」への評価を高める、未来への投資。
- **AIDXの役割**: 200社の不透明性を「データ」で解消し（PERディスカウントの除去）、事業間を繋いだ新サービスで成長期待（g）を上積みする。

---

## 関連ドキュメント
- [[01_Net_Income_Structure]]
- [[02_PER_Expectation_Growth]]
- [[03_Efficiency_Drivers]]
