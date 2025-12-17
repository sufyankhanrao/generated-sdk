
# Get Contact Logs Response

## Structure

`GetContactLogsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `contact_logs` | [`List[ContactLog]`](../../doc/models/contact-log.md) | Optional | Contains the information about the contact logs. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ContactLogs": [
    {
      "Id": 140,
      "Text": "Text8",
      "CreatedDateTime": "2016-03-13T12:52:32.123Z",
      "FollowupByDate": "2016-03-13T12:52:32.123Z",
      "ContactMethod": "ContactMethod0"
    },
    {
      "Id": 140,
      "Text": "Text8",
      "CreatedDateTime": "2016-03-13T12:52:32.123Z",
      "FollowupByDate": "2016-03-13T12:52:32.123Z",
      "ContactMethod": "ContactMethod0"
    }
  ]
}
```

