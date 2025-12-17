
# Product Group

## Structure

`ProductGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_id` | `int` | Optional | Referenced Purchase Category Id<br>Example: 123, 124 |
| `product_group_id` | `str` | Optional | Product group ID |
| `name` | `str` | Optional | Product group name |
| `is_default` | `bool` | Optional | Indicates whether this is a default Product Group at ColCo level or not.<br>Note: The Customer level default settings are not considered here. |
| `is_fuel_type` | `bool` | Optional | Identifies the type of Product group.<br>true - if it is a Fuel type Product group<br>false - if it is Non-Fuel type |
| `products` | [`List[ProductAllOf0]`](../../doc/models/product-all-of-0.md) | Optional | - |

## Example (as JSON)

```json
{
  "ReferenceId": 123,
  "ProductGroupId": "7",
  "Name": "Automotive Gas Oil",
  "IsDefault": false,
  "IsFuelType": false
}
```

