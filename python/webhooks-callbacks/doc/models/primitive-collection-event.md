
# Primitive Collection Event

## Structure

`PrimitiveCollectionEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType3Enum`](../../doc/models/event-type-3-enum.md) | Optional | - |
| `ids` | `List[int]` | Required | - |

## Example (as JSON)

```json
{
  "eventType": "primitive.variant",
  "ids": [
    77,
    78,
    79
  ]
}
```

