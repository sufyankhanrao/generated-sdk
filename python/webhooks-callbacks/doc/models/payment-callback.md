
# Payment Callback

## Structure

`PaymentCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Required | - |
| `payment_status` | [`PaymentStatusEnum`](../../doc/models/payment-status-enum.md) | Required | - |
| `transaction_id` | `str` | Required | - |
| `amount` | `float` | Optional | - |
| `currency` | `str` | Optional | - |
| `timestamp` | `datetime` | Optional | - |
| `failure_reason` | `str` | Optional | Reason for payment failure (if applicable) |

## Example (as JSON)

```json
{
  "orderId": "order_789",
  "paymentStatus": "success",
  "transactionId": "txn_abc123",
  "amount": 59.98,
  "currency": "USD",
  "timestamp": "09/19/2025 10:35:00",
  "failureReason": "failureReason0"
}
```

