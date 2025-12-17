
# Insurance Transaction Info

*This model accepts additional fields of type Any.*

## Structure

`InsuranceTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `insurance_transaction` | [`InsuranceTransaction`](../../doc/models/insurance-transaction.md) | Optional | Insurance transactions |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "insuranceTransaction": {
    "accountId": "accountId4",
    "amount": 123.56,
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

