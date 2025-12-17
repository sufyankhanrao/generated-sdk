
# Deposit Balance

*This model accepts additional fields of type Any.*

## Structure

`DepositBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_account` | [`DepositBalances`](../../doc/models/deposit-balances.md) | Optional | Data elements included with balances specific to deposit accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "depositAccount": {
    "accountId": "accountId0",
    "accountType": "accountType0",
    "accountNumberDisplay": "accountNumberDisplay6",
    "currency": {
      "currencyCode": "currencyCode0",
      "currencyRate": 27.48,
      "originalCurrencyCode": "originalCurrencyCode4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
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

