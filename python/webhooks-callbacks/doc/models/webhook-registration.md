
# Webhook Registration

## Structure

`WebhookRegistration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | The endpoint URL that will receive webhook events |
| `events` | [`List[EventEnum]`](../../doc/models/event-enum.md) | Required | List of events to subscribe to |
| `secret` | `str` | Optional | Secret key for webhook signature verification |
| `active` | `bool` | Optional | Whether the webhook is active<br><br>**Default**: `True` |

## Example (as JSON)

```json
{
  "url": "https://merchant.example.com/webhooks/events",
  "events": [
    "order.created",
    "payment.completed"
  ],
  "secret": "webhook_secret_key_123",
  "active": true
}
```

