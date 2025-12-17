
# Target Wealth 2

Defines the amount that the investor is willing to set as their target wealth in their portfolio at the end of the (maximum length) goal tenure. The `min`/`max` values represent the minimum and maximum target wealth values respectively. The `max` value must be more than or equal to the `min` value.

*This model accepts additional fields of type Any.*

## Structure

`TargetWealth2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `float` | Required | The minimum amount that the investor is willing to set as their target wealth in their portfolio at the end of the (minimum length) goal tenure.<br><br>**Constraints**: `>= 100000` |
| `max` | `float` | Required | The maximum amount that the investor is willing to set as their target wealth in their portfolio at the end of the (maximum length) goal tenure. This value must be more than or equal to the minimum amount target wealth. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "min": 100000.0,
  "max": 240.44,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

