
# Loan Balance Info

*This model accepts additional fields of type Any.*

## Structure

`LoanBalanceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loan_account` | [`LoanBalances`](../../doc/models/loan-balances.md) | Optional | Data elements included with balances specific to loan accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "loanAccount": {
    "accountId": "accountId6",
    "accountType": "accountType6",
    "accountNumberDisplay": "accountNumberDisplay2",
    "currency": {
      "currencyCode": "currencyCode0",
      "currencyRate": 27.48,
      "originalCurrencyCode": "originalCurrencyCode4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
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

