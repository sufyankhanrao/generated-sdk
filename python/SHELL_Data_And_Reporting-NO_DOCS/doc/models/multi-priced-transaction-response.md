
# Multi Priced Transaction Response

## Structure

`MultiPricedTransactionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transactions` | [`List[MultiPricedTransactionResponseTransactionsItems]`](../../doc/models/multi-priced-transaction-response-transactions-items.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `request_id` | `str` | Optional | API Request Id |
| `current_page` | `int` | Optional | Current Page |
| `row_count` | `int` | Optional | Total row count matched for the given input criteria |
| `total_pages` | `int` | Optional | Calculated page count based on page size from the incoming API request and total number of rows matched for the given input criteria |

## Example (as JSON)

```json
{
  "Transactions": [
    {
      "Type": "Type2",
      "CardId": 86,
      "CardPAN": "CardPAN4",
      "CardExpiry": "CardExpiry0",
      "TransactionDate": "TransactionDate0"
    },
    {
      "Type": "Type2",
      "CardId": 86,
      "CardPAN": "CardPAN4",
      "CardExpiry": "CardExpiry0",
      "TransactionDate": "TransactionDate0"
    }
  ],
  "Error": {
    "Code": "Code4",
    "Description": "Description2"
  },
  "RequestId": "RequestId8",
  "CurrentPage": 154,
  "RowCount": 52
}
```

