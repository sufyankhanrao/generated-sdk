
# Get Time Cards Response

## Structure

`GetTimeCardsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `time_cards` | [`List[TimeCardEvent]`](../../doc/models/time-card-event.md) | Optional | Information about time card entries, ordered by staff ID. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "TimeCards": [
    {
      "StaffId": 162,
      "Task": "Task2",
      "TimeIn": "2016-03-13T12:52:32.123Z",
      "TimeOut": "2016-03-13T12:52:32.123Z",
      "Hours": 250.5
    },
    {
      "StaffId": 162,
      "Task": "Task2",
      "TimeIn": "2016-03-13T12:52:32.123Z",
      "TimeOut": "2016-03-13T12:52:32.123Z",
      "Hours": 250.5
    }
  ]
}
```

