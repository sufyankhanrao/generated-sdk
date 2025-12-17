
# Bank Card Rejects Search Response

Used for pagination

## Structure

`BankCardRejectsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | This is used to retrieve the numbers or marks used to indicate the sequence of pages |
| `details` | [`List[BankCardRejRealTimeTransaction]`](../../doc/models/bank-card-rej-real-time-transaction.md) | Optional | Refers to settlement details |

## Example (as JSON)

```json
{
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  },
  "details": [
    {
      "processDate": "processDate0",
      "batchNumber": 100000,
      "batchAmount": 1000000000.0,
      "saleCount": 66,
      "saleAmount": 18.34
    }
  ]
}
```

