
# Get Semesters Request

Get Semesters Request Model

## Structure

`GetSemestersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `semester_i_ds` | `List[int]` | Optional | The requested semester IDs. |
| `start_date` | `datetime` | Optional | The start date for the range. All semesters that are on or after this day.<br>Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date for the range. All semesters that are on or before this day.<br>Default: **StartDate** |
| `active` | `bool` | Optional | When true, the response only contains semesters which are activated. When false, only deactivated semesters are returned.<br>Default: **All semesters** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SemesterIDs": [
    157
  ],
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "Active": false,
  "Limit": 220
}
```

