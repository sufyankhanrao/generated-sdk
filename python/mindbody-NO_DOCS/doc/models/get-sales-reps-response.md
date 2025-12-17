
# Get Sales Reps Response

This is the response class for the get sales reps API

## Structure

`GetSalesRepsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `sales_reps` | [`List[SalesRepResponse]`](../../doc/models/sales-rep-response.md) | Optional | This the list of sales reps and their details |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "SalesReps": [
    {
      "Id": 188,
      "FirstName": "FirstName8",
      "LastName": "LastName2",
      "SalesRepNumbers": [
        112,
        113,
        114
      ]
    },
    {
      "Id": 188,
      "FirstName": "FirstName8",
      "LastName": "LastName2",
      "SalesRepNumbers": [
        112,
        113,
        114
      ]
    },
    {
      "Id": 188,
      "FirstName": "FirstName8",
      "LastName": "LastName2",
      "SalesRepNumbers": [
        112,
        113,
        114
      ]
    }
  ]
}
```

