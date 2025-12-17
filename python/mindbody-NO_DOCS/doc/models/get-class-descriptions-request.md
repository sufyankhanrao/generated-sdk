
# Get Class Descriptions Request

## Structure

`GetClassDescriptionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_description_id` | `int` | Optional | The ID of the requested client. |
| `program_ids` | `List[int]` | Optional | A list of requested program IDs. |
| `start_class_date_time` | `datetime` | Optional | Filters the results to class descriptions for scheduled classes that happen on or after the given date and time. |
| `end_class_date_time` | `datetime` | Optional | Filters the results to class descriptions for scheduled classes that happen before the given date and time. |
| `staff_id` | `int` | Optional | Filters results to class descriptions for scheduled classes taught by the given staff member. |
| `location_id` | `int` | Optional | Filters results to classes descriptions for schedule classes as the given location. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClassDescriptionId": 242,
  "ProgramIds": [
    186,
    187,
    188
  ],
  "StartClassDateTime": "2016-03-13T12:52:32.123Z",
  "EndClassDateTime": "2016-03-13T12:52:32.123Z",
  "StaffId": 136
}
```

