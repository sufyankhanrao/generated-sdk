
# Search Settled Transactions Response

Resource is used to retrieve the settled transactions details

## Structure

`SearchSettledTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | This is used to retrieve the numbers or marks used to indicate the sequence of pages. |
| `settlements` | [`List[SearchSettledTransactionsResponseSettlements]`](../../doc/models/search-settled-transactions-response-settlements.md) | Optional | Used to retrieve settled transaction details |

## Example (as JSON)

```json
{
  "paginationResponse": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "settlements": [
    {
      "fraudFields": {
        "fraudScore": 100.0,
        "fraudRule": "fraudRule2",
        "fraudResponseCode": {
          "code": "code6",
          "shortDescription": "shortDescription4",
          "longDescription": "longDescription8"
        },
        "fraudRuleResult": {
          "code": "code2",
          "shortDescription": "shortDescription0",
          "longDescription": "longDescription4"
        },
        "fraudResponseTime": "fraudResponseTime4"
      }
    },
    {
      "fraudFields": {
        "fraudScore": 100.0,
        "fraudRule": "fraudRule2",
        "fraudResponseCode": {
          "code": "code6",
          "shortDescription": "shortDescription4",
          "longDescription": "longDescription8"
        },
        "fraudRuleResult": {
          "code": "code2",
          "shortDescription": "shortDescription0",
          "longDescription": "longDescription4"
        },
        "fraudResponseTime": "fraudResponseTime4"
      }
    },
    {
      "fraudFields": {
        "fraudScore": 100.0,
        "fraudRule": "fraudRule2",
        "fraudResponseCode": {
          "code": "code6",
          "shortDescription": "shortDescription4",
          "longDescription": "longDescription8"
        },
        "fraudRuleResult": {
          "code": "code2",
          "shortDescription": "shortDescription0",
          "longDescription": "longDescription4"
        },
        "fraudResponseTime": "fraudResponseTime4"
      }
    }
  ]
}
```

