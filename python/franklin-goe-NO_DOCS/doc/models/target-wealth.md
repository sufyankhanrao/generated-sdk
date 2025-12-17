
# Target Wealth

*This model accepts additional fields of type Any.*

## Structure

`TargetWealth`

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
  "max": 123.12,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

