
# Simple Model

*This model accepts additional fields of type [ComplexModel | AnotherComplexModel](../../doc/models/containers/simple-model-additional-properties.md).*

## Structure

`SimpleModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | `str` | Required | The required property |
| `additional_properties` | Dict[str, [ComplexModel](../../doc/models/complex-model.md) \| [AnotherComplexModel](../../doc/models/another-complex-model.md)] | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "requiredProperty": "requiredProperty2",
  "exampleAdditionalProperty": {
    "name": "name2",
    "age": "age0",
    "exampleAdditionalProperty": {
      "name": "name4",
      "job": "job8",
      "exampleAdditionalProperty": "AnotherComplexModel_additionalProperties0"
    }
  }
}
```

