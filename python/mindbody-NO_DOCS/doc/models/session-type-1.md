
# Session Type 1

## Structure

`SessionType1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Optional | - |
| `default_time_length` | `int` | Optional | - |
| `staff_time_length` | `int` | Optional | - |
| `program_id` | `int` | Optional | - |
| `num_deducted` | `int` | Optional | - |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `active` | `bool` | Optional | - |
| `capacity` | `int` | Optional | - |
| `resource_required` | `bool` | Optional | - |
| `category` | [`ServiceTag`](../../doc/models/service-tag.md) | Optional | ServiceTag refers to Category and Subcategory fields for classes and appointments |
| `subcategory` | [`ServiceTag`](../../doc/models/service-tag.md) | Optional | ServiceTag refers to Category and Subcategory fields for classes and appointments |
| `online_description` | `str` | Optional | - |
| `available_for_add_on` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "Type": "Arrival",
  "DefaultTimeLength": 152,
  "StaffTimeLength": 130,
  "ProgramId": 134,
  "NumDeducted": 246
}
```

