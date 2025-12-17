
# Products Inventory

## Structure

`ProductsInventory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | A ProductId of the product. |
| `barcode_id` | `str` | Optional | The Id is barcode Id of the product. |
| `location_id` | `int` | Optional | The LocationId of the product. |
| `units_logged` | `int` | Optional | UnitsLogged of the product. |
| `units_sold` | `int` | Optional | UnitsSold of the product. |
| `units_in_stock` | `int` | Optional | The units in stock of the product |
| `reorder_level` | `int` | Optional | ReorderLevel of the product. |
| `max_level` | `int` | Optional | MaxLevel of the product. |
| `created_date_time_utc` | `datetime` | Optional | CreatedDateTimeUTC of the product. |
| `modified_date_time_utc` | `datetime` | Optional | ModifiedDateTimeUTC of the product. |

## Example (as JSON)

```json
{
  "ProductId": 114,
  "BarcodeId": "BarcodeId0",
  "LocationId": 216,
  "UnitsLogged": 10,
  "UnitsSold": 24
}
```

