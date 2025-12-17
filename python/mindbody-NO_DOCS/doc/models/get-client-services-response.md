
# Get Client Services Response

## Structure

`GetClientServicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `client_services` | [`List[ClientService]`](../../doc/models/client-service.md) | Optional | Contains information about client pricing options. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ClientServices": [
    {
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 38,
      "Current": false,
      "ExpirationDate": "2016-03-13T12:52:32.123Z",
      "Id": 230
    }
  ]
}
```

