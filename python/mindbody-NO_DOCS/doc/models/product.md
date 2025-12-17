
# Product

## Structure

`Product`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | The unique ID associated with product. |
| `id` | `str` | Optional | The barcode number of the product. This is the `PurchasedItems[].BarcodeId` returned from GET Sales. |
| `category_id` | `int` | Optional | The revenue category ID of the product. Use this ID when calling the GET Categories endpoint. |
| `sub_category_id` | `int` | Optional | The SubCategory ID of the product. Use this ID when calling the GET Categories endpoint. |
| `price` | `float` | Optional | The price of the product. |
| `tax_included` | `float` | Optional | If tax inclusive-pricing is enabled, this field shows how much tax was added to the price. To fetch this value `LocationId` must be passed as a query parameter. |
| `tax_rate` | `float` | Optional | The tax rate that was applied to this purchase. To fetch this value `LocationId` must be passed as a query parameter. |
| `group_id` | `int` | Optional | The unique ID of the product group. |
| `name` | `str` | Optional | The name of the product. |
| `online_price` | `float` | Optional | The online price of the product. |
| `short_description` | `str` | Optional | A short text description of the product. |
| `long_description` | `str` | Optional | A long, more detailed text description of the product. |
| `type_group` | `int` | Optional | The Type group of the product. |
| `supplier_id` | `int` | Optional | The unique ID of the supplier of product. |
| `supplier_name` | `str` | Optional | The Supplier Name of the product. |
| `image_url` | `str` | Optional | The URL of the image associated with this product. |
| `color` | [`Color`](../../doc/models/color.md) | Optional | A color used by products. |
| `size` | [`Size`](../../doc/models/size.md) | Optional | - |
| `manufacturer_id` | `str` | Optional | The ID number attributed to the product by the manufacturer. |

## Example (as JSON)

```json
{
  "ProductId": 172,
  "Id": "Id0",
  "CategoryId": 128,
  "SubCategoryId": 164,
  "Price": 150.24
}
```

