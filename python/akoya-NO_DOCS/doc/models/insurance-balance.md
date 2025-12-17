
# Insurance Balance

*This model accepts additional fields of type Any.*

## Structure

`InsuranceBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `insurance_account` | [`InsuranceBalances`](../../doc/models/insurance-balances.md) | Optional | Data elements included with balances specific to insurance accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "insuranceAccount": {
    "accountId": "accountId8",
    "accountType": "accountType8",
    "accountNumberDisplay": "accountNumberDisplay4",
    "currency": {
      "currencyCode": "currencyCode0",
      "currencyRate": 27.48,
      "originalCurrencyCode": "originalCurrencyCode4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "description": "description8",
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

