
# Get Session Types Response

## Structure

`GetSessionTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `session_types` | [`List[SessionType]`](../../doc/models/session-type.md) | Optional | Contains information about sessions. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "SessionTypes": [
    {
      "Type": "Media",
      "DefaultTimeLength": 254,
      "StaffTimeLength": 232,
      "Id": 24,
      "Name": "Name6"
    },
    {
      "Type": "Media",
      "DefaultTimeLength": 254,
      "StaffTimeLength": 232,
      "Id": 24,
      "Name": "Name6"
    },
    {
      "Type": "Media",
      "DefaultTimeLength": 254,
      "StaffTimeLength": 232,
      "Id": 24,
      "Name": "Name6"
    }
  ]
}
```

