
# Get Transactions Response

Get transactions response properties

## Structure

`GetTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `transactions` | [`List[Transaction]`](../../doc/models/transaction.md) | Optional | Contains the transaction objects, each of which describes the transaction details for a purchase event. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Transactions": [
    {
      "TransactionId": 34,
      "SaleId": 160,
      "ClientId": 92,
      "Amount": 30.14,
      "Settled": false
    }
  ]
}
```

