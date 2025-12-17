
# Any of Complex or String

Allows either ComplexModel or a simple string.

*This model accepts additional fields of type Any.*

## Structure

`AnyOfComplexOrString`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `age` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name4",
  "age": "age2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

