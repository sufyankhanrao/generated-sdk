
# Get Sales Response

## Structure

`GetSalesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `sales` | [`List[Sale]`](../../doc/models/sale.md) | Optional | Contains the Sale objects, each of which describes the sale and payment for a purchase event. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Sales": [
    {
      "Id": 112,
      "SaleDate": "2016-03-13T12:52:32.123Z",
      "SaleTime": "SaleTime0",
      "SaleDateTime": "2016-03-13T12:52:32.123Z",
      "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 112,
      "SaleDate": "2016-03-13T12:52:32.123Z",
      "SaleTime": "SaleTime0",
      "SaleDateTime": "2016-03-13T12:52:32.123Z",
      "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

