
# Get Client Duplicates Response

## Structure

`GetClientDuplicatesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `client_duplicates` | [`List[ClientDuplicate]`](../../doc/models/client-duplicate.md) | Optional | The requested clients. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ClientDuplicates": [
    {
      "Id": "Id4",
      "UniqueId": 212,
      "FirstName": "FirstName6",
      "LastName": "LastName4",
      "Email": "Email6"
    },
    {
      "Id": "Id4",
      "UniqueId": 212,
      "FirstName": "FirstName6",
      "LastName": "LastName4",
      "Email": "Email6"
    },
    {
      "Id": "Id4",
      "UniqueId": 212,
      "FirstName": "FirstName6",
      "LastName": "LastName4",
      "Email": "Email6"
    }
  ]
}
```

