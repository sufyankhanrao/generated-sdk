
# Order Created Event

## Structure

`OrderCreatedEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Optional | - |
| `order_created_id` | `int` | Required | - |

## Example (as JSON)

```json
{
  "orderCreatedId": 9,
  "eventType": "order.created"
}
```

