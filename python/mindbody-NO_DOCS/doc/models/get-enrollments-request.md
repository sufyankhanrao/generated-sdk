
# Get Enrollments Request

## Structure

`GetEnrollmentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_schedule_ids` | `List[int]` | Optional | A list of the requested class schedule IDs. If omitted, all class schedule IDs return. |
| `end_date` | `datetime` | Optional | The end of the date range. The response returns any active enrollments that occur on or before this day.<br /><br>Default: **StartDate** |
| `location_ids` | `List[int]` | Optional | List of the IDs for the requested locations. If omitted, all location IDs return. |
| `program_ids` | `List[int]` | Optional | List of the IDs for the requested programs. If omitted, all program IDs return. |
| `session_type_ids` | `List[int]` | Optional | List of the IDs for the requested session types. If omitted, all session types IDs return. |
| `staff_ids` | `List[int]` | Optional | List of the IDs for the requested staff IDs. If omitted, all staff IDs return. |
| `start_date` | `datetime` | Optional | The start of the date range. The response returns any active enrollments that occur on or after this day.<br /><br>Default: **today’s date** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClassScheduleIds": [
    234
  ],
  "EndDate": "2016-03-13T12:52:32.123Z",
  "LocationIds": [
    198
  ],
  "ProgramIds": [
    220,
    221,
    222
  ],
  "SessionTypeIds": [
    246,
    245,
    244
  ]
}
```

