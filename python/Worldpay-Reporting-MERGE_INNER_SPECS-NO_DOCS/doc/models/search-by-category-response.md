
# Search by Category Response

Search by Category response details

## Structure

`SearchByCategoryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | - |
| `deposits` | [`List[SearchTotalResponse]`](../../doc/models/search-total-response.md) | Optional | deposit items details |

## Example (as JSON)

```json
{
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "deposits": [
    {
      "date": "date6",
      "settlementCategory": {
        "code": "code6",
        "description": "description8"
      },
      "fundingMethod": "fundingMethod6",
      "traceId": "traceId4",
      "routingNumber": 10000000,
      "ddaNumber": 10000000,
      "creditedAmount": 238.68,
      "debitedAmount": 52.64
    }
  ]
}
```

