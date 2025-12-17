
# Webhook

## Structure

`Webhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_id` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `last_delivery` | `datetime` | Optional | Timestamp of the last successful delivery |
| `delivery_count` | `int` | Optional | Total number of events delivered |

## Example (as JSON)

```json
{
  "webhookId": "webhook_456",
  "createdAt": "09/19/2025 09:00:00",
  "updatedAt": "09/19/2025 09:00:00",
  "deliveryCount": 42,
  "lastDelivery": "2016-03-13T12:52:32.123Z"
}
```

