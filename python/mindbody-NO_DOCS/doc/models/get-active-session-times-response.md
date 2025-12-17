
# Get Active Session Times Response

## Structure

`GetActiveSessionTimesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `active_session_times` | `List[str]` | Optional | List of available start times for active sessions. Note the following:<br><br>* The times returned represent possibilities for scheduling a session, not necessarily currently scheduled sessions.<br>* The response includes either all schedule types or those filtered by supplying `ScheduleType` or `SessionTypeIds`.<br>* Each session has an associated schedule type, but when you supply `SessionTypeIds`, they may map to one or more of the schedule types. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ActiveSessionTimes": [
    "ActiveSessionTimes4"
  ]
}
```

