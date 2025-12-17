
# Get Contracts Response

## Structure

`GetContractsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `contracts` | [`List[Contract]`](../../doc/models/contract.md) | Optional | Contains information about each contract. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Contracts": [
    {
      "Id": 44,
      "Name": "Name6",
      "Description": "Description0",
      "AssignsMembershipId": 176,
      "AssignsMembershipName": "AssignsMembershipName4"
    }
  ]
}
```

