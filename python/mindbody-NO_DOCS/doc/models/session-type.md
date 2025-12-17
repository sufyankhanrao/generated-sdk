
# Session Type

SessionType contains information about the session types in a business.

## Structure

`SessionType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Optional | Contains the class description session type. Possible values are:<br><br>* All<br>* Class<br>* Enrollment<br>* Appointment<br>* Resource<br>* Media<br>* Arrival |
| `default_time_length` | `int` | Optional | The default amount of time that a session of this type typically lasts. |
| `staff_time_length` | `int` | Optional | The amount of time that a session of this type will last for a specific Staff (when applicable.) |
| `id` | `int` | Optional | This session type’s unique ID. |
| `name` | `str` | Optional | The name of this session type. |
| `online_description` | `str` | Optional | The online description associated with the appointment. |
| `num_deducted` | `int` | Optional | The number of sessions that this session type deducts from the pricing option used to pay for this type of session. |
| `program_id` | `int` | Optional | This session type’s service category ID. |
| `category` | `str` | Optional | This session type’s category. |
| `category_id` | `int` | Optional | This session type’s category ID. |
| `subcategory` | `str` | Optional | This session type’s subcategory. |
| `subcategory_id` | `int` | Optional | This session type’s subcategory ID. |
| `available_for_add_on` | `bool` | Optional | This session type’s Add On Flag. |

## Example (as JSON)

```json
{
  "Type": "Class",
  "DefaultTimeLength": 30,
  "StaffTimeLength": 52,
  "Id": 52,
  "Name": "Name8"
}
```

