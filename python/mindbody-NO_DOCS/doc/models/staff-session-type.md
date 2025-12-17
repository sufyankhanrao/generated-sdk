
# Staff Session Type

## Structure

`StaffSessionType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | The staff member Id |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Optional | Contains the class description session type. |
| `id` | `int` | Optional | This session type’s unique Id. |
| `name` | `str` | Optional | The name of this session type. |
| `num_deducted` | `int` | Optional | The number of sessions that this session type deducts from the pricing option used to pay for this type of session. |
| `program_id` | `int` | Optional | This session type’s service category Id. |
| `category` | `str` | Optional | This session type’s category. |
| `category_id` | `int` | Optional | This session type’s category Id. |
| `subcategory` | `str` | Optional | This session type’s subcategory. |
| `subcategory_id` | `int` | Optional | This session type’s subcategory Id. |
| `time_length` | `int` | Optional | - |
| `prep_time` | `int` | Optional | Prep time in minutes |
| `finish_time` | `int` | Optional | Finish time in minutes |
| `pay_rate_type` | `str` | Optional | The pay rate type |
| `pay_rate_amount` | `float` | Optional | The pay rate amount |

## Example (as JSON)

```json
{
  "StaffId": 216,
  "Type": "All",
  "Id": 206,
  "Name": "Name4",
  "NumDeducted": 166
}
```

