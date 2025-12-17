
# Settlement Rejects Search Response

Used for pagination

## Structure

`SettlementRejectsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | This is used to retrieve the numbers or marks used to indicate the sequence of pages |
| `details` | [`List[SettlementRejRealTimeTransaction]`](../../doc/models/settlement-rej-real-time-transaction.md) | Optional | Refers to settlement details |

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
      "processedDate": "processedDate0",
      "transactionDate": "transactionDate4",
      "resubmitDate": "resubmitDate6",
      "accountNumber": "accountNumber8",
      "ddaNumber": "ddaNumber8"
    },
    {
      "processedDate": "processedDate0",
      "transactionDate": "transactionDate4",
      "resubmitDate": "resubmitDate6",
      "accountNumber": "accountNumber8",
      "ddaNumber": "ddaNumber8"
    }
  ]
}
```

