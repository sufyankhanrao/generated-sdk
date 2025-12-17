
# Purchase Gift Card Response

## Structure

`PurchaseGiftCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_id` | `str` | Optional | The barcode ID assigned to the purchased gift card. |
| `value` | `float` | Optional | The monetary value of the gift card. |
| `amount_paid` | `float` | Optional | The amount paid for the gift card by the purchaser. |
| `from_name` | `str` | Optional | The name of the purchaser. |
| `layout_id` | `int` | Optional | The ID of the layout used for this gift card. |
| `email_receipt` | `bool` | Optional | Whether or not an email receipt was sent to the purchaser. If true, a receipt was sent. |
| `purchaser_client_id` | `str` | Optional | The client ID of the purchaser. |
| `purchaser_email` | `str` | Optional | The purchaser’s email address. |
| `recipient_email` | `str` | Optional | The recipient’s email address. |
| `sale_id` | `int` | Optional | The sale ID of the gift card. |
| `payment_processing_failures` | [`List[PaymentProcessingFailure]`](../../doc/models/payment-processing-failure.md) | Optional | Any cart processing failures, for example when SCA challenged, the cart is in PaymentAuthenticationRequired state and at least one of the failures listed will provide an authentication Url. |

## Example (as JSON)

```json
{
  "BarcodeId": "BarcodeId0",
  "Value": 107.42,
  "AmountPaid": 228.46,
  "FromName": "FromName0",
  "LayoutId": 246
}
```

