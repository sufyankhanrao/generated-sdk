
# Investment Balance List

*This model accepts additional fields of type Any.*

## Structure

`InvestmentBalanceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_name` | `str` | Optional | Name of the balance. |
| `balance_description` | `str` | Optional | Description of balance. |
| `balance_type` | [`InvestmentBalanceType`](../../doc/models/investment-balance-type.md) | Optional | The type of an investment balance. AMOUNT or PERCENTAGE. |
| `balance_value` | `float` | Optional | Value of balance name. |
| `balance_date` | `datetime` | Optional | Date as of this balance. |
| `currency` | [`CurrencyEntity`](../../doc/models/currency-entity.md) | Optional | Indicates the currency code used by the account. May also include currency rate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "balanceName": "balanceName0",
  "balanceDescription": "balanceDescription6",
  "balanceType": "AMOUNT",
  "balanceValue": 220.9,
  "balanceDate": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

