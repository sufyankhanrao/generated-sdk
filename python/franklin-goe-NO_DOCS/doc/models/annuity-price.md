
# Annuity Price

*This model accepts additional fields of type Any.*

## Structure

`AnnuityPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `age` | `int` | Required | - |
| `value` | [`List[Value]`](../../doc/models/value.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "age": 50,
  "value": [
    {
      "year": 62,
      "rate": 5.73354,
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

