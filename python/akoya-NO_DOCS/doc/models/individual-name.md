
# Individual Name

Name of responsible individual

*This model accepts additional fields of type Any.*

## Structure

`IndividualName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | `str` | Optional | First name |
| `middle` | `str` | Optional | Middle initial |
| `last` | `str` | Optional | Last name |
| `suffix` | `str` | Optional | Generational or academic suffix |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "first": "first2",
  "middle": "middle2",
  "last": "last4",
  "suffix": "suffix4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

