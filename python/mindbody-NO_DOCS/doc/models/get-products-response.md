
# Get Products Response

## Structure

`GetProductsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `products` | [`List[Product]`](../../doc/models/product.md) | Optional | Contains information about the products. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Products": [
    {
      "ProductId": 92,
      "Id": "Id0",
      "CategoryId": 48,
      "SubCategoryId": 84,
      "Price": 72.64
    },
    {
      "ProductId": 92,
      "Id": "Id0",
      "CategoryId": 48,
      "SubCategoryId": 84,
      "Price": 72.64
    },
    {
      "ProductId": 92,
      "Id": "Id0",
      "CategoryId": 48,
      "SubCategoryId": 84,
      "Price": 72.64
    }
  ]
}
```

