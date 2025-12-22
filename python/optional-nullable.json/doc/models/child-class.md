
# Child Class

## Structure

`ChildClass`

## Inherits From

[`ParentClass`](../../doc/models/parent-class.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `optional_nullable` | `str` | Optional | - |
| `optional_nullable_with_default_value` | `str` | Optional | **Default**: `"With default value"` |
| `optional` | `str` | Optional | - |
| `required_nullable` | `str` | Required | - |
| `required` | `str` | Required | **Default**: `"not nullable and required"` |
| `child_class_array` | [`List[ChildClass]`](../../doc/models/child-class.md) | Optional | - |

## Example (as JSON)

```json
{
  "Grand_Parent_Required_Nullable": "Grand_Parent_Required_Nullable6",
  "Grand_Parent_Required": "not nullable and required",
  "class": 23,
  "Parent_Optional_Nullable_With_Default_Value": "Has default value",
  "Parent_Required_Nullable": "Parent_Required_Nullable8",
  "Parent_Required": "not nullable and required",
  "Optional_Nullable_With_Default_Value": "With default value",
  "Required_Nullable": "Required_Nullable0",
  "Required": "not nullable and required",
  "Grand_Parent_Optional": "Grand_Parent_Optional0",
  "precision": 235.58,
  "Big_Decimal": 90.14,
  "Parent_Optional": "Parent_Optional0",
  "Optional_Nullable": "Optional_Nullable2",
  "Optional": "Optional2",
  "Child_Class_Array": [
    {
      "Grand_Parent_Optional": "Grand_Parent_Optional0",
      "Grand_Parent_Required_Nullable": "Grand_Parent_Required_Nullable6",
      "Grand_Parent_Required": "Grand_Parent_Required0",
      "class": 134,
      "precision": 235.58,
      "Big_Decimal": 90.14,
      "Parent_Optional_Nullable_With_Default_Value": "Parent_Optional_Nullable_With_Default_Value6",
      "Parent_Optional": "Parent_Optional0",
      "Parent_Required_Nullable": "Parent_Required_Nullable8",
      "Parent_Required": "Parent_Required6",
      "Optional_Nullable": "Optional_Nullable4",
      "Optional_Nullable_With_Default_Value": "Optional_Nullable_With_Default_Value0",
      "Optional": "Optional4",
      "Required_Nullable": "Required_Nullable2",
      "Required": "Required0",
      "Child_Class_Array": [
        {},
        {},
        {}
      ]
    },
    {
      "Grand_Parent_Optional": "Grand_Parent_Optional0",
      "Grand_Parent_Required_Nullable": "Grand_Parent_Required_Nullable6",
      "Grand_Parent_Required": "Grand_Parent_Required0",
      "class": 134,
      "precision": 235.58,
      "Big_Decimal": 90.14,
      "Parent_Optional_Nullable_With_Default_Value": "Parent_Optional_Nullable_With_Default_Value6",
      "Parent_Optional": "Parent_Optional0",
      "Parent_Required_Nullable": "Parent_Required_Nullable8",
      "Parent_Required": "Parent_Required6",
      "Optional_Nullable": "Optional_Nullable4",
      "Optional_Nullable_With_Default_Value": "Optional_Nullable_With_Default_Value0",
      "Optional": "Optional4",
      "Required_Nullable": "Required_Nullable2",
      "Required": "Required0",
      "Child_Class_Array": [
        {},
        {},
        {}
      ]
    }
  ]
}
```

