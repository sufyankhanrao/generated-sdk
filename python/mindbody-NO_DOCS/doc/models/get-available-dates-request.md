
# Get Available Dates Request

## Structure

`GetAvailableDatesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_type_id` | `int` | Required | required requested session type ID. |
| `location_id` | `int` | Optional | optional requested location ID. |
| `staff_id` | `int` | Optional | optional requested staff ID. |
| `start_date` | `datetime` | Optional | The start date of the requested date range. If omitted, the default is used.<br><br />Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date of the requested date range.<br><br />Default: **StartDate** |

## Example (as JSON)

```json
{
  "SessionTypeId": 14,
  "LocationId": 170,
  "StaffId": 120,
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z"
}
```

