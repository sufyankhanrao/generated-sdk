
# Map of Array Additional Properties

*This model accepts additional fields of type Dict[str, float].*

## Structure

`MapOfArrayAdditionalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | `Dict[str, float]` | Required | - |
| `additional_properties` | `Dict[str, Dict[str, float]]` | Optional | - |

## Example (as JSON)

```json
{
  "requiredProperty": {
    "key0": 241.7
  },
  "exampleAdditionalProperty": {
    "key0": 15.48
  }
}
```

