
# Investment Transaction Info

*This model accepts additional fields of type Any.*

## Structure

`InvestmentTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `investment_transaction` | [`InvestmentTransaction`](../../doc/models/investment-transaction.md) | Optional | Investment Transactions |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "investmentTransaction": {
    "accountId": "accountId2",
    "amount": 139.34,
    "category": "category0",
    "debitCreditMemo": "DEBIT",
    "description": "description2",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

