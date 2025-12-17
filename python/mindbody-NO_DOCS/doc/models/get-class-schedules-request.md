
# Get Class Schedules Request

## Structure

`GetClassSchedulesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_schedule_ids` | `List[int]` | Optional | The class schedule IDs.<br><br />Default: **all** |
| `end_date` | `datetime` | Optional | The end date of the range. Return any active enrollments that occur on or before this day.<br><br />Default: **StartDate** |
| `location_ids` | `List[int]` | Optional | The location IDs.<br><br />Default: **all** |
| `program_ids` | `List[int]` | Optional | The program IDs.<br><br />Default: **all** |
| `session_type_ids` | `List[int]` | Optional | The session type IDs.<br><br />Default: **all** |
| `staff_ids` | `List[int]` | Optional | The staff IDs.<br><br />Default: **all** |
| `start_date` | `datetime` | Optional | The start date of the range. Return any active enrollments that occur on or after this day.<br><br />Default: **today’s date** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClassScheduleIds": [
    140
  ],
  "EndDate": "2016-03-13T12:52:32.123Z",
  "LocationIds": [
    104
  ],
  "ProgramIds": [
    126,
    127,
    128
  ],
  "SessionTypeIds": [
    4,
    3
  ]
}
```

