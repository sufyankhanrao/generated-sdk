
# Package

## Structure

`Package`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The ID of the package. |
| `name` | `str` | Optional | The name of the package. |
| `discount_percentage` | `float` | Optional | The discount percentage applied to the package. |
| `sell_online` | `bool` | Optional | When `true`, only products that can be sold online are returned.<br /><br>When `false`, all products are returned. |
| `services` | [`List[Service]`](../../doc/models/service.md) | Optional | Information about the services in the packages. |
| `products` | [`List[Product]`](../../doc/models/product.md) | Optional | Information about the products in the packages. |

## Example (as JSON)

```json
{
  "Id": 82,
  "Name": "Name4",
  "DiscountPercentage": 6.46,
  "SellOnline": false,
  "Services": [
    {
      "Price": 224.3,
      "OnlinePrice": 2.82,
      "TaxIncluded": 75.84,
      "ProgramId": 204,
      "TaxRate": 192.34
    }
  ]
}
```

