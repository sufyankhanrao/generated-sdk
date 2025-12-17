
# Priced Transaction Response

## Structure

`PricedTransactionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transactions` | [`List[PricedTransactionResponseTransactionsItems]`](../../doc/models/priced-transaction-response-transactions-items.md) | Optional | - |

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
    }
  ]
}
```

