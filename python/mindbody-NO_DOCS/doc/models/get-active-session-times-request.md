
# Get Active Session Times Request

## Structure

`GetActiveSessionTimesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule_type` | [`ScheduleType1Enum`](../../doc/models/schedule-type-1-enum.md) | Optional | Filters on the provided the schedule type. Either `SessionTypeIds` or `ScheduleType` must be provided. |
| `session_type_ids` | `List[int]` | Optional | Filters on the provided session type IDs. Either `SessionTypeIds` or `ScheduleType` must be provided. |
| `start_time` | `datetime` | Optional | Filters results to times that start on or after this time on the current date. Any date provided is ignored.<br><br />Default: **00:00:00** |
| `end_time` | `datetime` | Optional | Filters results to times that end on or before this time on the current date. Any date provided is ignored..<br><br />Default: **23:59:59** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ScheduleType": "Enrollment",
  "SessionTypeIds": [
    194,
    195,
    196
  ],
  "StartTime": "2016-03-13T12:52:32.123Z",
  "EndTime": "2016-03-13T12:52:32.123Z",
  "Limit": 22
}
```

