
# Balances

*This model accepts additional fields of type Any.*

## Structure

`Balances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | List[[DepositBalance](../../doc/models/deposit-balance.md) \| [LoanBalance](../../doc/models/loan-balance.md) \| [LocBalance](../../doc/models/loc-balance.md) \| [InvestmentBalance](../../doc/models/investment-balance.md) \| [InsuranceBalance](../../doc/models/insurance-balance.md) \| [AnnuityBalance](../../doc/models/annuity-balance.md)] \| None | Optional | This is List of a container for any-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accounts": [
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
    },
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
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

