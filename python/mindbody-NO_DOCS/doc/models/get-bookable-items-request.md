
# Get Bookable Items Request

## Structure

`GetBookableItemsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_type_ids` | `List[int]` | Required | A list of the requested session type IDs. |
| `location_ids` | `List[int]` | Optional | A list of the requested location IDs. |
| `staff_ids` | `List[int]` | Optional | A list of the requested staff IDs. Omit parameter to return all staff availabilities. |
| `start_date` | `datetime` | Optional | The start date of the requested date range.<br><br />Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date of the requested date range.<br><br />Default: **StartDate** |
| `appointment_id` | `int` | Optional | If provided, filters out the appointment with this ID. |
| `ignore_default_session_length` | `bool` | Optional | When `true`, availabilities that are non-default return, for example, a 30-minute availability with a 60-minute default session length.<br /><br>When `false`, only availabilities that have the default session length return. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SessionTypeIds": [
    168
  ],
  "LocationIds": [
    20,
    21,
    22
  ],
  "StaffIds": [
    219
  ],
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "AppointmentId": 18
}
```

