
# Child String Type

Inherits a User with string type additional properties, also has string typed additionalProperties

*This model accepts additional fields of type str.*

## Structure

`ChildStringType`

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
  "type": "CompSame",
  "name": "name6",
  "exampleAdditionalProperty": "ParentStringType_additionalProperties3",
  "company": "company6"
}
```

