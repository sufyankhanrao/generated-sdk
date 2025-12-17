
# Initial Investment

*This model accepts additional fields of type Any.*

## Structure

`InitialInvestment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `float` | Required | The minimum amount of funds the investor will place into the portfolio at the beginning of the goal tenure. This value<br><br>**Constraints**: `>= 100000` |
| `max` | `float` | Required | The maximum amount of funds the investor will place into the portfolio at the beginning of the goal tenure. This value must be more than or equal to the `min` amount. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "min": 100000.0,
  "max": 7.58,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

