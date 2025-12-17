
# Update Service Request

This class represents the request parameters for the update service API

## Structure

`UpdateServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_id` | `str` | Optional | The barcode ID of the pricing option. |
| `price` | `float` | Optional | The cost of the pricing option when sold at a physical location.<br><br>**Constraints**: `>= 0` |
| `online_price` | `float` | Optional | The cost of the pricing option when sold online.<br><br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "BarcodeId": "BarcodeId4",
  "Price": 37.54,
  "OnlinePrice": 72.06
}
```

