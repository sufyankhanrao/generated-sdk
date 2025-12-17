
# Validation Error

*This model accepts additional fields of type Any.*

## Structure

`ValidationError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loc` | List[str \| int] | Required | This is List of a container for any-of cases. |
| `msg` | `str` | Required | - |
| `mtype` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "loc": [
    "String9",
    "String0"
  ],
  "msg": "msg4",
  "type": "type8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

