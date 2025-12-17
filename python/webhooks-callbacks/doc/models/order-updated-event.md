
# Order Updated Event

## Structure

`OrderUpdatedEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType1Enum`](../../doc/models/event-type-1-enum.md) | Optional | - |
| `order_updated_id` | `int` | Required | - |

## Example (as JSON)

```json
{
  "orderUpdatedId": 91,
  "eventType": "order.updated"
}
```

