
# Get Resources Request

## Structure

`GetResourcesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_type_ids` | `List[int]` | Optional | List of session type IDs.<br /><br>Default: **all** |
| `location_id` | `int` | Optional | The location of the resource. This parameter is ignored if `EndDateTime` or `LocationID` is not set.<br /><br>Default: **all** |
| `start_date_time` | `datetime` | Optional | The time the resource starts. This parameter is ignored if `EndDateTime` or `LocationID` is not set. |
| `end_date_time` | `datetime` | Optional | The time the resource ends. This parameter is ignored if `EndDateTime` or `LocationID` is not set. |
| `resource_ids` | `List[int]` | Optional | Filter on resourceIds |
| `location_ids` | `List[int]` | Optional | Filter by location ids (optional) |
| `schedule_types` | [`List[ScheduleType4Enum]`](../../doc/models/schedule-type-4-enum.md) | Optional | Filter by schedule types (optional) |
| `program_ids` | `List[int]` | Optional | Filter by program ids (optional) |
| `include_inactive` | `bool` | Optional | Enable to include inactive |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SessionTypeIds": [
    126,
    125,
    124
  ],
  "LocationId": 248,
  "StartDateTime": "2016-03-13T12:52:32.123Z",
  "EndDateTime": "2016-03-13T12:52:32.123Z",
  "ResourceIds": [
    220
  ]
}
```

