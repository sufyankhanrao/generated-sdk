
# Get Sites Response

## Structure

`GetSitesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `sites` | [`List[Site]`](../../doc/models/site.md) | Optional | Contains information about the sites. |

## Example (as JSON)

```json
{
  "Sites": [
    {
      "LeadChannels": [
        {
          "UniversalCustomerId": "00000000-0000-0000-0000-000000000000"
        }
      ],
      "AcceptsAmericanExpress": false,
      "AcceptsDiscover": false,
      "AcceptsMasterCard": false,
      "AcceptsVisa": false,
      "AllowsDashboardAccess": false
    }
  ],
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  }
}
```

