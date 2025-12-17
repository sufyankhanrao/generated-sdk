
# Add Availabilities Request

## Structure

`AddAvailabilitiesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test` | `bool` | Optional | When `true`, the request ensures that its parameters are valid without affecting real data.<br>When `false`, the request performs as intended and may affect live client data.<br>(optional) Defaults to false. |
| `location_id` | `int` | Optional | Location of availability.<br><br />Not used when IsUnavailable is `true`. |
| `staff_i_ds` | `List[int]` | Optional | A list of requested staff IDs.<br /><br>(optional) Defaults to staff ID of user credentials. Use 0 for all. |
| `program_i_ds` | `List[int]` | Optional | A list of program IDs.<br /><br>(optional) Defaults to all.<br><br />Not used when IsUnavailable is true. |
| `start_date_time` | `datetime` | Optional | The start date and time of the new availabilities or unavailabilities. |
| `end_date_time` | `datetime` | Optional | The end date and time of the new availabilities or unavailabilities. |
| `days_of_week` | [`List[DaysOfWeekEnum]`](../../doc/models/days-of-week-enum.md) | Optional | The days of the week to set.<br /><br>(optional) Defaults to all. |
| `unavailable_description` | `str` | Optional | Description of unavalability.<br><br />Only used when IsUnavailable is true. |
| `is_unavailable` | `bool` | Optional | When `true`, indicates that unavailability is getting added. When `false`, indicates that availability is getting added.<br>Default: **false** |
| `public_display` | [`PublicDisplay1Enum`](../../doc/models/public-display-1-enum.md) | Optional | Sets the public display of the availability.<br /><ul><li>Show</li><li>Mask</li><li>Hide</li></ul><br>(optional) Defaults to Show. |

## Example (as JSON)

```json
{
  "Test": false,
  "LocationID": 106,
  "StaffIDs": [
    237,
    238,
    239
  ],
  "ProgramIDs": [
    0
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

