
# Get Programs Response

## Structure

`GetProgramsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `programs` | [`List[Program]`](../../doc/models/program.md) | Optional | Contains information about the programs. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Programs": [
    {
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "CancelOffset": 182,
      "ContentFormats": [
        "ContentFormats9"
      ]
    },
    {
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "CancelOffset": 182,
      "ContentFormats": [
        "ContentFormats9"
      ]
    }
  ]
}
```

