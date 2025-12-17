
# One of Additional Properties

*This model accepts additional fields of type [ComplexModelWithStringAdditionalProperties | AnotherComplexModel](../../doc/models/containers/one-of-complex-model.md).*

## Structure

`OneOfAdditionalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | [ComplexModelWithStringAdditionalProperties](../../doc/models/complex-model-with-string-additional-properties.md) \| [AnotherComplexModel](../../doc/models/another-complex-model.md) | Required | OneOf ComplexModel and AnotherComplexModel |
| `additional_properties` | Dict[str, [ComplexModelWithStringAdditionalProperties](../../doc/models/complex-model-with-string-additional-properties.md) \| [AnotherComplexModel](../../doc/models/another-complex-model.md)] | Optional | OneOf ComplexModel and AnotherComplexModel |

## Example (as JSON)

```json
{
  "requiredProperty": {
    "name": "ABC",
    "job": "Alphabet",
    "something": "someValue"
  },
  "exampleAdditionalProperty": {
    "name": "name4",
    "age": "age2",
    "exampleAdditionalProperty": "ComplexModelWithStringAdditionalProperties_additionalProperties8"
  }
}
```

