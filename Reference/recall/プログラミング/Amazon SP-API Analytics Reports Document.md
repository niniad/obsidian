---
title: Amazon SP-API Analytics Reports Document
tags:
  - "プログラミング"
createdAt: Tue Nov 25 2025 09:48:32 GMT+0900 (日本標準時)
updatedAt: Tue Nov 25 2025 09:49:57 GMT+0900 (日本標準時)
---


Concise summary


## ブランド分析レポートの概要と利用可能なレポートタイプ
- ブランド分析のSelling Partner APIロールを持ち、Amazonブランド登録に登録されている出品者が利用可能なレポートには、GET_BRAND_ANALYTICS_SEARCH_CATALOG_PERFORMANCE_REPORT、GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT、GET_BRAND_ANALYTICS_MARKET_BASKET_REPORT、GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORTがあります。
- これらのレポートは、リクエストのみ可能で、レポート出力タイプはJSONです。
- 各レポートには、reportOptions値を指定できます。例えば、reportPeriodを指定してレポートのレポート期間を決定できます。

## ベンダー向けレポートとその基本パラメーター
- ブランド分析のSelling Partner APIロールを持ち、Amazonブランド登録に登録されている出品者とベンダーが利用可能なレポートがあります。
- レポートには、GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT、GET_VENDOR_REAL_TIME_INVENTORY_REPORT、GET_VENDOR_REAL_TIME_TRAFFIC_REPORTなどのレポートタイプがあります。
- 各レポートタイプには、reportPeriod、dataStartTime、dataEndTimeなどのパラメーターを指定して、レポートの日付境界やレポート期間を指定できます。

## ベンダー小売分析レポートの内容と出力形式
- ベンダー小売分析レポート（vendorRealTimeSalesReport、vendorSalesReport、vendorNetPureProductMarginReport）には、ベンダーの商品カタログ全体の集計レベルとASINレベルのデータが含まれます。
- レポート出力タイプはJSONで、リクエストのみ可能です。
- レポートには、注文/出荷済みの収益やユニット数などの主要な小売売上指標が含まれます。
- ベンダー小売分析レポートは、リクエストのみ可能で、レポート出力タイプはJSONです。

## レポートの詳細パラメーターと制約条件
- レポートには、詳細ページビューなどの小売トラフィック指標や、在庫と運用の健全性指標が含まれます。
- ベンダー予測レポート、ベンダー在庫レポート、セラー販売およびトラフィックレポートなどのレポートが利用可能で、それぞれのレポートには、reportOptions値を指定できます。
- このレポートをリクエストする際に指定されるdataStartTime値は、リクエスト日から遡って2年以内でなければなりません。
- reportOptions値には、dateGranularityとasinGranularityを指定できます。dateGranularityのデフォルトはDAY、asinGranularityのデフォルトはPARENTです。
- dateGranularityがWEEKまたはMONTHの場合、dataStartTimeおよびdataEndTimeの値は自動的に調整されます。




## Sources
- [website](https://developer-docs.amazon.com/sp-api/lang-ja_JP/docs/report-type-values-analytics)
