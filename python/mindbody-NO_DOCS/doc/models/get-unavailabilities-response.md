
# Get Unavailabilities Response

## Structure

`GetUnavailabilitiesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `unavailabilities` | [`List[UnavailabilityPlain]`](../../doc/models/unavailability-plain.md) | Optional | Contains information about unavailabilities |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Unavailabilities": [
    {
      "Id": 246,
      "StaffId": 0,
      "StartDateTime": "2016-03-13T12:52:32.123Z",
      "EndDateTime": "2016-03-13T12:52:32.123Z",
      "Description": "Description8"
    },
    {
      "Id": 246,
      "StaffId": 0,
      "StartDateTime": "2016-03-13T12:52:32.123Z",
      "EndDateTime": "2016-03-13T12:52:32.123Z",
      "Description": "Description8"
    },
    {
      "Id": 246,
      "StaffId": 0,
      "StartDateTime": "2016-03-13T12:52:32.123Z",
      "EndDateTime": "2016-03-13T12:52:32.123Z",
      "Description": "Description8"
    }
  ]
}
```

