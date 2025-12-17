
# Child Enabled Parent Disabled

Inherits a User with disabled additional properties, but has number typed additionalProperties

*This model accepts additional fields of type float.*

## Structure

`ChildEnabledParentDisabled`

## Inherits From

[`ParentDisabled`](../../doc/models/parent-disabled.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company` | `str` | Required | - |
| `additional_properties` | `Dict[str, float]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "Comp",
  "id": {
    "key1": "val1",
    "key2": "val2"
  },
  "company": "company6",
  "exampleAdditionalProperty": 55.04
}
```

