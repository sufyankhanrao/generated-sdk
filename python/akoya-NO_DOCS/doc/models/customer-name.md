
# Customer Name

*This model accepts additional fields of type Any.*

## Structure

`CustomerName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | `str` | Optional | First or given name. This data element may contain first & last name if not separated. |
| `middle` | `str` | Optional | - |
| `last` | `str` | Optional | - |
| `prefix` | `str` | Optional | Name prefix, e.g. Mr. |
| `suffix` | `str` | Optional | Generational or academic suffix |
| `company` | `str` | Optional | Company name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "first": "first2",
  "middle": "middle2",
  "last": "last4",
  "prefix": "prefix4",
  "suffix": "suffix4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

