
# Loc Transaction Info

*This model accepts additional fields of type Any.*

## Structure

`LocTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loc_transaction` | [`LocTransaction`](../../doc/models/loc-transaction.md) | Optional | A line of credit transaction of type |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "locTransaction": {
    "accountId": "accountId4",
    "amount": 130.76,
    "category": "category2",
    "debitCreditMemo": "DEBIT",
    "description": "description6",
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

