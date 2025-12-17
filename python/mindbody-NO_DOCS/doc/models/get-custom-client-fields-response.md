
# Get Custom Client Fields Response

## Structure

`GetCustomClientFieldsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `custom_client_fields` | [`List[CustomClientField]`](../../doc/models/custom-client-field.md) | Optional | Contains information about the available custom client fields. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "CustomClientFields": [
    {
      "Id": 112,
      "DataType": "DataType2",
      "Name": "Name8"
    },
    {
      "Id": 112,
      "DataType": "DataType2",
      "Name": "Name8"
    },
    {
      "Id": 112,
      "DataType": "DataType2",
      "Name": "Name8"
    }
  ]
}
```

