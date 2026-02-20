# SP-API Report Type Values

**Source URL**: `https://developer-docs.amazon.com/sp-api/docs/report-type-values`
*(Fetched via Agent due to missing Firecrawl Key)*

## GET_SALES_AND_TRAFFIC_REPORT
- **Granularity**: DAY, WEEK, MONTH
- **Key Fields**: orderedProductSales, revenue, unitsOrdered, claimAmount, pageViews, buyBoxPercentage.
- **Availability**: 7 days after the day closes.
- **Note**: Data might not return for ASINs with zero orders.

## GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL
- **Description**: Tab-delimited flat file containing all orders placed within a specified date range.
- **Update Frequency**: Real-time (with some lag).
