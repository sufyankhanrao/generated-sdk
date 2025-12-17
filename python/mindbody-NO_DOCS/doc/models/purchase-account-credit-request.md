
# Purchase Account Credit Request

## Structure

`PurchaseAccountCreditRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test` | `bool` | Optional | When `true`, allows you to test the request without affecting the database.<br>When `false`, the request is carried out and the database is affected. |
| `location_id` | `int` | Optional | The ID of the location where the account credit is being sold. |
| `client_id` | `str` | Required | The ID of the location where the account credit is being sold. |
| `send_email_receipt` | `bool` | Optional | When `true`, indicates that a purchase receipt email should be sent to the purchasing client, if all settings are correctly configured.<br /><br>When `false`, no email is sent to the purchaser. |
| `sales_rep_id` | `int` | Optional | The ID of the staff member to be marked as the sales rep for this account credit sale. |
| `consumer_present` | `bool` | Optional | When `true`, indicates that the consumer is present or otherwise able to successfully negotiate an SCA challenge.<br>It is not a good idea to have this always be false as that could very likely lead to a bank declining all transactions for the merchant. Defaults to false.<br>Default: **false** |
| `payment_authentication_callback_url` | `str` | Optional | The URL consumer is redirected to if the bank requests SCA. This field is only needed if ConsumerPresent is true. |
| `payment_info` | [`CheckoutPaymentInfo`](../../doc/models/checkout-payment-info.md) | Optional | - |

## Example (as JSON)

```json
{
  "Test": false,
  "LocationId": 158,
  "ClientId": "ClientId4",
  "SendEmailReceipt": false,
  "SalesRepId": 164,
  "ConsumerPresent": false
}
```

