
# Payment Completed Event

## Structure

`PaymentCompletedEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType2Enum`](../../doc/models/event-type-2-enum.md) | Optional | - |
| `payment_id` | `int` | Required | - |

## Example (as JSON)

```json
{
  "paymentId": 91,
  "eventType": "payment.completed"
}
```

