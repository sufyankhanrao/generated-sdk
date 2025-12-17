
# Get Programs Request

## Structure

`GetProgramsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule_type` | [`ScheduleType3Enum`](../../doc/models/schedule-type-3-enum.md) | Optional | A schedule type used to filter the returned results. Possible values are:<br><br>* All<br>* Class<br>* Enrollment<br>* Appointment<br>* Resource<br>* Media<br>* Arrival |
| `online_only` | `bool` | Optional | If `true`, filters results to show only those programs that are shown online.<br /><br>If `false`, all programs are returned.<br /><br>Default: **false** |
| `program_ids` | `List[int]` | Optional | Program Ids to filter for |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ScheduleType": "Media",
  "OnlineOnly": false,
  "ProgramIds": [
    122,
    123
  ],
  "Limit": 84,
  "Offset": 150
}
```

