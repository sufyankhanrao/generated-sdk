
# Complex Model

*This model accepts additional fields of type [AnotherComplexModel](../../doc/models/another-complex-model.md).*

## Structure

`ComplexModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `age` | `str` | Required | - |
| `additional_properties` | [`Dict[str, AnotherComplexModel]`](../../doc/models/another-complex-model.md) | Optional | - |

## Example (as JSON)

```json
{
  "name": "name2",
  "age": "age0",
  "exampleAdditionalProperty": {
    "name": "name4",
    "job": "job8",
    "exampleAdditionalProperty": "AnotherComplexModel_additionalProperties0"
  }
}
```

