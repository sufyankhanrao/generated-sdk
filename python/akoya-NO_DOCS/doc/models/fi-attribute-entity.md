
# Fi Attribute Entity

Data provider-specific attribute

*This model accepts additional fields of type Any.*

## Structure

`FiAttributeEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of attribute |
| `value` | `str` | Optional | Value of attribute |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name6",
  "value": "value8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

