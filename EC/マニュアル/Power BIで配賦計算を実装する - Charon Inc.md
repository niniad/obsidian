# Power BIで配賦計算を実装する - Charon Inc.

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0010.png?fit=1762%2C1020&ssl=1)

業績評価や原価計算、予算管理など、いわゆる管理会計という業務において避けて通れないのが**配賦(Allocation)**です。

実務上はExcelを使って配賦計算をされている企業が多いのではないかと思います。共通費を部門別に配賦する、といったレベルであればExcelでも十分に自動化が可能です。

しかし、「外部倉庫からの出庫手数料や配送料を、商品種類別に重みづけしてから販売先別品番別の出荷数量を基準に配賦し、品番別の実際の利益を顧客別商品別に分析できるようにしてよ」みたいなことを上司に言われた場合、これをExcelで自動化するのはなかなか大変です。

このような作業はPower BIなどのBIツールで自動化させるべきです。

今回の記事ではサンプルデータを使って配賦の考え方からPower BIでの実装方法まで詳しく解説していきます。Power BIをある程度マスターしてしまえば、上記のような一見複雑にみえる処理も完全に自動化することができます。

[Power BIのサンプルファイル](https://charon-inc.co.jp/download/power-bi-allocation-sample-pbix-file/)もご用意していますので、手っ取り早くイメージを掴みたい方はこちらを。

## 配賦計算の例

以下の例を考えてみましょう。

販売管理システムから品番別の売上明細、会計システムから販管費の仕訳データがそれぞれ出力されてきたとします。このとき、外注倉庫への支払手数料を各売上明細に出荷数量を基準として配賦し、物流コストを勘案した利益を算出する処理を自動化してみたいと思います。

### 売上明細データ (Sample)

いわゆる売上伝票の明細データです。

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0001.png?fit=1732%2C926&ssl=1)

### 仕訳データ (Sample)

いわゆる仕訳データです。物流費以外にもいろいろな科目が含まれています。

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0002.png?fit=1190%2C806&ssl=1)

今回は「出荷数量基準」で配賦していきますので、配賦の計算式は以下のようになります。

**物流コスト配賦金額=(出荷数量/当月出荷数量合計) x 当月物流コスト合計**

配賦元のテーブル（仕訳データ）と配賦先のテーブル（売上明細データ）に、それぞれいくつかの列を追加するだけで簡単に実装することができます。ここからステップバイステップで実装方法を解説していきます。

### 配賦元（仕訳データ）に項目を追加

まずは配賦元である仕訳データで列を2つの列を追加します。

**年月 (Year Month)：**月単位で配賦計算を行っていくのが一般的だと思いますので、まずは物流コストを月別に集計するためのキーとして年月(Year Month)を追加します。

Syntax Highlighter

1

```
Year Month = FORMAT([日付],"YY/MM")
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0003.png?fit=1418%2C906&ssl=1)

**金額 (Amount)：**今回のサンプルの仕訳データは貸借で列が分かれているので、借方-貸方で純額を集計しやすいようにしておきます。借方発生額だけを集計してしまうと会計システム側で赤黒の伝票が入ったときに誤った金額を集計してしまうためです。

Syntax Highlighter

1

```
Amount = [借方]-[貸方]
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0006.png?fit=1762%2C882&ssl=1)

### 配賦先（売上明細データ）に計算式を追加

次に配賦先である売上明細テーブルに列を追加していきます。計算の過程が見えるように、上記の計算式を以下のように各列に分解して実装していきます。

**年月 (Year Month)：**仕訳データ同様、売上明細側にもYear Month列を追加します。

Syntax Highlighter

1

```
Year Month = FORMAT([日付],"YY/MM")
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0004.png?fit=1762%2C882&ssl=1)

当月出荷数量合計 (Qty Total)：当月のすべての品番の出荷数量を集計し、配賦率計算の分母として使います。

Syntax Highlighter

1

```
QtyTotal =
```

2

```
var YearMonth=[Year Month]
```

3

```
var QtyTTL=
```

4

```
    CALCULATE(sum(factSalesLine[数量]),
```

5

```
        ALL(factSalesLine),
```

6

```
        factSalesLine[Year Month]=YearMonth)
```

7

8

```
RETURN QtyTTL
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0005.png?fit=1758%2C1062&ssl=1)

**当月物流コスト合計 (Dist.Cost Total) ：**当月の物流コストを仕訳データ側から集計してきて売上明細のテーブルに表示させます。

Syntax Highlighter

1

```
Dist. Cost Total =
```

2

```
var YearMonth=[Year Month]
```

3

```
var DistCostTTL=CALCULATE(SUM(factGeneralLedger[Amount]),
```

4

```
    factGeneralLedger[Year Month]=YearMonth,
```

5

```
    factGeneralLedger[科目コード]="5110")
```

6

7

```
RETURN DistCostTTL
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0007.png?fit=1758%2C1120&ssl=1)

**配賦率 (Allocation %) ：**売上明細の出荷数量を当月出荷数量合計で割って配賦率を求めます。

Syntax Highlighter

1

```
Allocation % =
```

2

```
var Qty=[数量]
```

3

```
var AllocationRate=DIVIDE(Qty,factSalesLine[QtyTotal])
```

4

5

```
RETURN AllocationRate
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0008.png?fit=1758%2C1120&ssl=1)

**物流コスト配賦金額 (Dist. Cost Allocated)：**配賦率に当月物流コスト合計を乗じて配賦金額を計算します。

Syntax Highlighter

1

```
Dist. Cost Allocated = [Allocation %] * [Dist. Cost Total]
```

![](https://i0.wp.com/charon-inc.co.jp/wp-content/uploads/2024/05/PowerBI-Allocation-img-0009.png?fit=1758%2C1120&ssl=1)

### 行をまたがって集計するやつがポイント

合計列の取得方法は少し気を付ける必要があります。今回はCalculate関数を使って合計値を計算しています。技術的には以下の内容がポイントとなります。

**当月出荷数量合計：**月単位で出荷数量の合計を集計するためvarで自レコードの年月を切り出して、それと合致する条件で合計数量を集計しています。同じテーブル内のデータを集計する必要があるため、5行目のAll関数で行コンテキストを無視（？）しています。

Syntax Highlighter

1

```
QtyTotal =
```

2

```
var YearMonth=[Year Month]
```

3

```
var QtyTTL=
```

4

```
    CALCULATE(sum(factSalesLine[数量]),
```

5

```
        ALL(factSalesLine),
```

6

```
        factSalesLine[Year Month]=YearMonth)
```

7

8

```
RETURN QtyTTL
```

**当月物流コスト合計：**同様にvarで自レコードの年月を切り出して、同じ月の物流コスト合計を仕訳テーブルから集計しています。また、仕訳テーブルには物流委託費以外の科目も含まれるので、5行目で科目コードを絞っています。

Syntax Highlighter

1

```
Dist. Cost Total =
```

2

```
var YearMonth=[Year Month]
```

3

```
var DistCostTTL=CALCULATE(SUM(factGeneralLedger[Amount]),
```

4

```
    factGeneralLedger[Year Month]=YearMonth,
```

5

```
    factGeneralLedger[科目コード]="5110")
```

6

7

```
RETURN DistCostTTL
```

### 分析とアクション

ここまで作成したレポートにいくつかのメジャーを追加し、品目別・得意先別にそれぞれ利益率を分析してみました。

売上総利益は全て同じですが、物流費を配賦してみると品目別に大きく利益率が異なることがわかります。

入出荷の回数や出荷の個数によって物流費（の中でもいわゆるハンドリングチャージ）が変動する契約になっているとすると、以下のような手を打つことで利益率を大きく改善できるかもしれません。

- 得意先との取り決めにより、モバイル冷蔵庫については最低受注数量（MOQ）を定め、小口の受注が何度も行われないようにする
- 仕入先との取り決めにより、入庫時の荷姿を変更し個単位ではなくケース単位で出荷処理を行うことで配送費を下げる

このように、いままで見えなかったデータが見えてきたら、何をすべきかが見えてきます。

### サンプルファイル

今回の記事で利用したPower BIファイルのサンプルは以下のページからダウンロードいただけます。

[https://charon-inc.co.jp/download/power-bi-allocation-sample-pbix-file/](https://charon-inc.co.jp/download/power-bi-allocation-sample-pbix-file/)

## まとめ

### Calculate関数 超重要

・・ということで、Power BIでは少しの計算式を入れてあげるだけで、一見複雑に見える配賦計算も簡単に実装することができます。Calculate関数の使い方さえある程度理解してしまえばDAX側でできることが一気に広がります。

PowerBIの開発を行うとき、データを取ってくるときに処理をするのか、データを取ってきた後に処理をするのかを常に意識する必要があります。PowerBIの言葉で言うとPower Query側で実装するのか、DAX側で実装するのか、ということです。

実は配賦の処理自体はどちら側でも実装できるのですが、慣れてしまえば今回のようにDAX側で処理するほうが簡単です。

### データドリブン？

粗利だけを見ていると利益を稼いでいるように見える品目も、物流コストを勘案すると実はあまり儲かっていない、ということは実務上よくあります。適切な配賦基準を設定することで本当の利益を把握することができます。

“データドリブン経営”みたいな言葉が叫ばれて久しい昨今ですが、このような取り組みがきちんとできている企業はまだまだ多くはないのかもしれません。

配賦計算は管理会計における基本的かつ重要なツールです。できるだけPower BIなどで自動化できるようにしておきたいものですね。

当社ではERP/CRM + Power BIの導入により管理会計を高度化するサービスを提供しております。お気軽にご相談を。

/ Categories: [Power BI](https://charon-inc.co.jp/blog/category/power-bi/) / Tags: [Accounting](https://charon-inc.co.jp/blog/tag/accounting/), [Allocation](https://charon-inc.co.jp/blog/tag/allocation/), [Managirial Accounting](https://charon-inc.co.jp/blog/tag/managirial-accounting/), [原価計算](https://charon-inc.co.jp/blog/tag/%e5%8e%9f%e4%be%a1%e8%a8%88%e7%ae%97/), [管理会計](https://charon-inc.co.jp/blog/tag/%e7%ae%a1%e7%90%86%e4%bc%9a%e8%a8%88/), [配賦計算](https://charon-inc.co.jp/blog/tag/%e9%85%8d%e8%b3%a6%e8%a8%88%e7%ae%97/)