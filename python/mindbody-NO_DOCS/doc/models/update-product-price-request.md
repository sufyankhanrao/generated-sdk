
# Update Product Price Request

Update Product Price Request Model

## Structure

`UpdateProductPriceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_id` | `str` | Optional | The barcode number of the product. This is the `Products[].Id` returned from GET Products. |
| `price` | `float` | Optional | The price you sell the product for. |
| `online_price` | `float` | Optional | The online price of the product. |

## Example (as JSON)

```json
{
  "BarcodeId": "BarcodeId8",
  "Price": 150.78,
  "OnlinePrice": 185.3
}
```

