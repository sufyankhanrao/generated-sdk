
# Get Products Inventory Response

## Structure

`GetProductsInventoryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `products_inventory` | [`List[ProductsInventory]`](../../doc/models/products-inventory.md) | Optional | Contains information about the products inventory. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ProductsInventory": [
    {
      "ProductId": 114,
      "BarcodeId": "BarcodeId0",
      "LocationId": 216,
      "UnitsLogged": 10,
      "UnitsSold": 24
    }
  ]
}
```

