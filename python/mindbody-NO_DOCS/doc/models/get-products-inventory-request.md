
# Get Products Inventory Request

## Structure

`GetProductsInventoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_ids` | `List[str]` | Optional | When included, the response only contains details about the specified product Ids. |
| `location_ids` | `List[int]` | Optional | When included, the response only contains details about the specified location Ids. |
| `barcode_ids` | `List[str]` | Optional | When included, the response only contains details about the specified Barcode Ids. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ProductIds": [
    "ProductIds2"
  ],
  "LocationIds": [
    100
  ],
  "BarcodeIds": [
    "BarcodeIds4"
  ],
  "Limit": 172,
  "Offset": 106
}
```

