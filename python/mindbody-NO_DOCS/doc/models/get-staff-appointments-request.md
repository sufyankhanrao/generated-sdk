
# Get Staff Appointments Request

## Structure

`GetStaffAppointmentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `appointment_ids` | `List[int]` | Optional | A list of the requested appointment IDs. |
| `location_ids` | `List[int]` | Optional | A list of the requested location IDs. |
| `start_date` | `datetime` | Optional | The start date of the requested date range. If omitted, the default is used.<br><br />Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date of the requested date range.<br><br />Default: **StartDate** |
| `staff_ids` | `List[int]` | Optional | List of staff IDs to be returned. Omit parameter to return staff appointments for all staff. |
| `client_id` | `str` | Optional | The client ID to be returned. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "AppointmentIds": [
    222,
    223,
    224
  ],
  "LocationIds": [
    86
  ],
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "StaffIds": [
    113,
    114
  ]
}
```

