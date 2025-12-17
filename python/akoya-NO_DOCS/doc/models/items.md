
# Items

*This model accepts additional fields of type Any.*

## Structure

`Items`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cost_basis` | `float` | Optional | Total amount of money spent acquiring this lot including any fees or commission expenses incurred. |
| `current_value` | `float` | Optional | Lot market value |
| `original_purchase_date` | `datetime` | Optional | Lot acquired date. |
| `position_type` | [`PositionType`](../../doc/models/position-type.md) | Optional | LONG, SHORT. |
| `purchased_price` | `float` | Optional | Original purchase price. |
| `quantity` | `float` | Optional | Lot quantity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "costBasis": 179.8,
  "currentValue": 247.76,
  "originalPurchaseDate": "2016-03-13T12:52:32.123Z",
  "positionType": "LONG",
  "purchasedPrice": 31.42,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

