
# Child Number Type

Inherits a User with string type additional properties, but has number typed additionalProperties

*This model accepts additional fields of type str.*

## Structure

`ChildNumberType`

## Inherits From

[`ParentStringType`](../../doc/models/parent-string-type.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | `str` | Required | - |
| `additional_properties` | `Dict[str, str]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "CompDiff",
  "name": "name6",
  "exampleAdditionalProperty": "ParentStringType_additionalProperties3",
  "company": "company8"
}
```

