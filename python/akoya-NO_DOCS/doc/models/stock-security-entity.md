
# Stock Security Entity

Information about the stock security specific to the type of security

*This model accepts additional fields of type Any.*

## Structure

`StockSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units_street` | `float` | Optional | Units in the FI's street name, positive quantity |
| `units_user` | `float` | Optional | Units in user's name directly, positive  quantity |
| `reinvest_dividends` | `bool` | Optional | Reinvest dividends |
| `stock_type` | [`StockType`](../../doc/models/stock-type.md) | Optional | - |
| `myield` | `float` | Optional | Current yield |
| `yield_as_of_date` | `datetime` | Optional | Yield as-of date |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "unitsStreet": 117.56,
  "unitsUser": 92.52,
  "reinvestDividends": false,
  "stockType": "STOCK",
  "yield": 211.18,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

