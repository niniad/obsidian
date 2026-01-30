# SP-API FBA Inventory API v1

**Source URL**: `https://developer-docs.amazon.com/sp-api/docs/fba-inventory-api-v1-reference` (404 - Constructed from Search Summary)

## Endpoint
`GET /fba/inventory/v1/summaries`

## Description
Returns a list of inventory summaries. Validates real-time availability.

## Key Parameters
- `granularityType`: "Marketplace"
- `granularityId`: Marketplace ID
- `details`: "true" (to get quantities)
- `startDateTime`: To get changes since time.
- `sellerSkus`: To filter by SKU.

## Response Fields (likely)
- `asin`
- `fnSku`
- `sellerSku`
- `condition`
- `inventoryDetails`:
    - `fulfillableQuantity`
    - `inboundWorkingQuantity`
    - `inboundShippedQuantity`
    - `inboundReceivingQuantity`
    - `reservedQuantity`
