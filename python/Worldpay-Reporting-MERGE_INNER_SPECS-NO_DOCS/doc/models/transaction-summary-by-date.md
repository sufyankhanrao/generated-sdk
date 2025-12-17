
# Transaction Summary by Date

## Structure

`TransactionSummaryByDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | Pagination response details |
| `details` | [`List[DailySummaryDetails]`](../../doc/models/daily-summary-details.md) | Optional | Object is used for daily summary details |

## Example (as JSON)

```json
{
  "paginationResponse": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "details": [
    {
      "merchantId": "merchantId6",
      "totalSalesAmount": 98.92,
      "totalSalesCount": 194,
      "totalSettledSalesAmount": 113.66,
      "creditSalesAmount": 199.6
    }
  ]
}
```

