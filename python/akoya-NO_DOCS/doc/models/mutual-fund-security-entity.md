
# Mutual Fund Security Entity

Information about the mutual fund security specific to the type of security

*This model accepts additional fields of type Any.*

## Structure

`MutualFundSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mutual_fund_type` | [`MutualFundType`](../../doc/models/mutual-fund-type.md) | Optional | Mutual fund type |
| `units_street` | `float` | Optional | Units in the FI's street name, positive quantity |
| `units_user` | `float` | Optional | Units in user's name directly, positive  quantity |
| `reinvest_dividends` | `bool` | Optional | Reinvest dividends |
| `reinvest_capital_gains` | `bool` | Optional | Reinvest capital gains |
| `myield` | `float` | Optional | Current yield reported as portion of the fund's assets |
| `yield_as_of_date` | `datetime` | Optional | As-of date for yield value |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "mutualFundType": "OPENEND",
  "unitsStreet": 101.68,
  "unitsUser": 108.4,
  "reinvestDividends": false,
  "reinvestCapitalGains": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

