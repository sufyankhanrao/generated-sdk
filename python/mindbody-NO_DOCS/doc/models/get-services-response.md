
# Get Services Response

## Structure

`GetServicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `services` | [`List[Service]`](../../doc/models/service.md) | Optional | Contains information about the services. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Services": [
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    },
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    },
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    }
  ]
}
```

