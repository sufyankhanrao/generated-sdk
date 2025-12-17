
# Get Courses Request

This is the request class for the get courses API

## Structure

`GetCoursesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_i_ds` | `List[int]` | Optional | Return only courses that are available for the specified LocationIds. |
| `course_i_ds` | `List[int]` | Optional | Return only courses that are available for the specified CourseIds. |
| `staff_i_ds` | `List[int]` | Optional | Return only courses that are available for the specified StaffIds. |
| `program_i_ds` | `List[int]` | Optional | Return only courses that are available for the specified ProgramIds. |
| `start_date` | `datetime` | Optional | The start date range. Any active courses that are on or after this day.<br><br />(optional) Defaults to today. |
| `end_date` | `datetime` | Optional | The end date range. Any active courses that are on or before this day.<br><br />(optional) Defaults to StartDate. |
| `semester_i_ds` | `List[int]` | Optional | Return only courses that are available for the specified SemesterIds. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "LocationIDs": [
    129,
    130
  ],
  "CourseIDs": [
    81,
    82
  ],
  "StaffIDs": [
    209,
    210,
    211
  ],
  "ProgramIDs": [
    228
  ],
  "StartDate": "2016-03-13T12:52:32.123Z"
}
```

