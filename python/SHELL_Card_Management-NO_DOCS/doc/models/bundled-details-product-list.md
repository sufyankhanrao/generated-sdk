
# Bundled Details Product List

## Structure

`BundledDetailsProductList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `purchase_category_id` | `int` | Optional | Purchase category Id<br>Example: 123, 124, etc., |
| `purchase_category_code` | `str` | Optional | Purchase category name.<br>Example:<br>0 - All Fuels (without VP) and Lubricants<br>1 - FuelSave only<br>2 - FuelSave and Lubricants<br>3 - No Restrictions |
| `products` | `List[str]` | Optional | An array of 3-digit global product codes.<br>Example: [ "033", "021", "023" ] |
| `product_groups` | `List[str]` | Optional | An array of product group ids.<br>Example: [ "670246404", "40557126" ] |
| `fuel_set_id` | `str` | Optional | Fuel set id that is allowed to be purchased with the card |
| `fuel_set_name` | `str` | Optional | Fuel set name that is allowed to be purchased with the card |
| `non_fuel_sets` | `str` | Optional | Non-Fuel set name that is allowed to be purchased with the card |

## Example (as JSON)

```json
{
  "PurchaseCategoryId": 162,
  "PurchaseCategoryCode": "PurchaseCategoryCode6",
  "Products": [
    "Products2",
    "Products3",
    "Products4"
  ],
  "ProductGroups": [
    "ProductGroups5",
    "ProductGroups6",
    "ProductGroups7"
  ],
  "FuelSetId": "FuelSetId8"
}
```

