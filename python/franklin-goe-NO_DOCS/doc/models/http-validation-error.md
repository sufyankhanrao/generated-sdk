
# Http Validation Error

*This model accepts additional fields of type Any.*

## Structure

`HttpValidationError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | [`List[ValidationError]`](../../doc/models/validation-error.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "detail": [
    {
      "loc": [
        "String7",
        "String8",
        "String9"
      ],
      "msg": "msg2",
      "type": "type4",
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

