
# Purchase Account Credit Response

## Structure

`PurchaseAccountCreditResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_paid` | `float` | Optional | The amount paid for the gift card by the purchaser. |
| `client_id` | `str` | Optional | The client ID of the purchaser. |
| `sale_id` | `int` | Optional | The sale ID of the gift card. |
| `email_receipt` | `bool` | Optional | Whether or not an email receipt was sent to the purchaser. If true, a receipt was sent. |
| `payment_processing_failures` | [`List[PaymentProcessingFailure]`](../../doc/models/payment-processing-failure.md) | Optional | Any cart processing failures, for example when SCA challenged, the cart is in PaymentAuthenticationRequired state and at least one of the failures listed will provide an authentication Url. |

## Example (as JSON)

```json
{
  "AmountPaid": 108.56,
  "ClientId": "ClientId4",
  "SaleId": 162,
  "EmailReceipt": false,
  "PaymentProcessingFailures": [
    {
      "Type": "Type6",
      "Message": "Message2",
      "AuthenticationRedirectUrl": "AuthenticationRedirectUrl2"
    }
  ]
}
```

