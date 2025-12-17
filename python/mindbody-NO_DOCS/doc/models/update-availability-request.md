
# Update Availability Request

This is the update avaialability request coming DTO

## Structure

`UpdateAvailabilityRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `availability_ids` | `List[int]` | Optional | Unique IDs for the availabilities or unavailabilities. |
| `public_display` | [`PublicDisplayEnum`](../../doc/models/public-display-enum.md) | Optional | Choice that decides whether the availablity should be publicly visible, masked or hidden. |
| `days_of_week` | [`List[DaysOfWeekEnum]`](../../doc/models/days-of-week-enum.md) | Optional | The days of week to update the availabilities or unavailabilities.<br /><br>Default: **All** |
| `program_ids` | `List[int]` | Optional | The program Id to be set for the availabilities.<br>Default: **All** |
| `start_date_time` | `datetime` | Optional | The start date and time for the availabilities or unavailabilities. |
| `end_date_time` | `datetime` | Optional | The end date and time for the availabilities or unavailabilities. |
| `location_id` | `int` | Optional | The location Id to be updated for the provided availability Ids. |
| `unavailable_description` | `str` | Optional | The description for unavailability. |
| `test` | `bool` | Optional | When `true`, the request ensures that its parameters are valid without affecting real data.<br>When ``false`, the request performs as intended and may affect live client data.<br>Default: **false** |

## Example (as JSON)

```json
{
  "AvailabilityIds": [
    134
  ],
  "PublicDisplay": "Show",
  "DaysOfWeek": [
    "Tuesday"
  ],
  "ProgramIds": [
    98
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

