
# Get Resource Availabilities Request

## Structure

`GetResourceAvailabilitiesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `datetime` | Optional | Start time |
| `end_date` | `datetime` | Optional | End date. If default, StartDate is used. |
| `resource_ids` | `List[int]` | Optional | Filter on resourceIds |
| `location_ids` | `List[int]` | Optional | Filter by location ids (optional) |
| `schedule_types` | [`List[ScheduleType4Enum]`](../../doc/models/schedule-type-4-enum.md) | Optional | Filter by schedule types (optional) |
| `program_ids` | `List[int]` | Optional | Filter by program ids (optional) |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "ResourceIds": [
    52,
    53
  ],
  "LocationIds": [
    210,
    211
  ],
  "ScheduleTypes": [
    "All",
    "Class"
  ]
}
```

