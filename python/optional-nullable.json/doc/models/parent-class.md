
# Parent Class

## Structure

`ParentClass`

## Inherits From

[`GrandParentClass`](../../doc/models/grand-parent-class.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mclass` | `int` | Optional | **Default**: `23` |
| `precision` | `float` | Optional | - |
| `big_decimal` | `float` | Optional | - |
| `parent_optional_nullable_with_default_value` | `str` | Optional | **Default**: `"Has default value"` |
| `parent_optional` | `str` | Optional | - |
| `parent_required_nullable` | `str` | Required | - |
| `parent_required` | `str` | Required | **Default**: `"not nullable and required"` |

## Example (as JSON)

```json
{
  "Grand_Parent_Required_Nullable": "Grand_Parent_Required_Nullable6",
  "Grand_Parent_Required": "not nullable and required",
  "class": 23,
  "Parent_Optional_Nullable_With_Default_Value": "Has default value",
  "Parent_Required_Nullable": "Parent_Required_Nullable8",
  "Parent_Required": "not nullable and required",
  "Grand_Parent_Optional": "Grand_Parent_Optional0",
  "precision": 235.58,
  "Big_Decimal": 90.14,
  "Parent_Optional": "Parent_Optional0"
}
```

