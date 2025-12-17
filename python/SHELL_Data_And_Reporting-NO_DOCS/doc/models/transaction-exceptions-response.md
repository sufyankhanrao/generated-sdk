
# Transaction Exceptions Response

## Structure

`TransactionExceptionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_exceptions` | [`List[CardExceptions]`](../../doc/models/card-exceptions.md) | Optional | - |
| `transaction_exceptions` | [`List[TransactionExceptions]`](../../doc/models/transaction-exceptions.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `request_id` | `str` | Optional | API Request Id |

## Example (as JSON)

```json
{
  "CardExceptions": [
    {
      "AccountId": 224,
      "AccountNumber": "AccountNumber4",
      "AccountShortName": "AccountShortName6",
      "CardId": 130,
      "CurrencyCode": "CurrencyCode2"
    }
  ],
  "TransactionExceptions": [
    {
      "SalesItemId": 113.2,
      "CardId": 104,
      "ProductId": 220,
      "TransactionGUID": "TransactionGUID2",
      "TransactionDate": "TransactionDate6"
    },
    {
      "SalesItemId": 113.2,
      "CardId": 104,
      "ProductId": 220,
      "TransactionGUID": "TransactionGUID2",
      "TransactionDate": "TransactionDate6"
    }
  ],
  "Error": {
    "Code": "Code4",
    "Description": "Description2"
  },
  "RequestId": "RequestId8"
}
```

