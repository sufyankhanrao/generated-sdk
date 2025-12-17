
# Name

The end-user's name

*This model accepts additional fields of type Any.*

## Structure

`Name`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | `str` | Optional | First or given name. This data element may contain first & last name if not separated. |
| `middle` | `str` | Optional | - |
| `last` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "first": "first6",
  "middle": "middle6",
  "last": "last0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

