
# Deposit Transaction Info

*This model accepts additional fields of type Any.*

## Structure

`DepositTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_transaction` | [`DepositTransaction`](../../doc/models/deposit-transaction.md) | Optional | Deposit transaction |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "depositTransaction": {
    "accountId": "accountId0",
    "amount": 1.72,
    "category": "category8",
    "debitCreditMemo": "DEBIT",
    "description": "description0",
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

