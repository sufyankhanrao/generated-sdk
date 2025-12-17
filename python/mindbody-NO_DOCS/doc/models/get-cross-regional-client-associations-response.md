
# Get Cross Regional Client Associations Response

## Structure

`GetCrossRegionalClientAssociationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `cross_regional_client_associations` | [`List[CrossRegionalClientAssociation]`](../../doc/models/cross-regional-client-association.md) | Optional | Contains information about the client’s cross regional associations. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "CrossRegionalClientAssociations": [
    {
      "SiteId": 80,
      "ClientId": "ClientId0",
      "UniqueId": 202
    },
    {
      "SiteId": 80,
      "ClientId": "ClientId0",
      "UniqueId": 202
    }
  ]
}
```

