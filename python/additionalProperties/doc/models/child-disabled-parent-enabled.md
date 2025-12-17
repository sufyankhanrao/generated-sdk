
# Child Disabled Parent Enabled

Inherits a User with disabled additional properties, but has number typed additionalProperties

*This model accepts additional fields of type str.*

## Structure

`ChildDisabledParentEnabled`

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
  "type": "ChildDisabledParentEnabled",
  "name": "name6",
  "exampleAdditionalProperty": "ParentStringType_additionalProperties3",
  "company": "company4"
}
```

