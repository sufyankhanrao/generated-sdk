
# Any of Additional Properties

*This model accepts additional fields of type [ComplexModelWithStringAdditionalProperties | str](../../doc/models/containers/any-of-complex-or-string-2.md).*

## Structure

`AnyOfAdditionalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | [ComplexModelWithStringAdditionalProperties](../../doc/models/complex-model-with-string-additional-properties.md) \| str | Required | Allows either ComplexModel or a simple string. |
| `additional_properties` | Dict[str, [ComplexModelWithStringAdditionalProperties](../../doc/models/complex-model-with-string-additional-properties.md) \| str] | Optional | Allows either ComplexModel or a simple string. |

## Example (as JSON)

```json
{
  "requiredProperty": {
    "name": "name4",
    "age": "age2",
    "exampleAdditionalProperty": "ComplexModelWithStringAdditionalProperties_additionalProperties8"
  },
  "exampleAdditionalProperty": {
    "name": "name4",
    "age": "age2",
    "exampleAdditionalProperty": "ComplexModelWithStringAdditionalProperties_additionalProperties8"
  }
}
```

