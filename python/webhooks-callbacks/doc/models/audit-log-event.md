
# Audit Log Event

## Structure

`AuditLogEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType4Enum`](../../doc/models/event-type-4-enum.md) | Optional | - |
| `actor` | `str` | Optional | - |
| `action` | `str` | Optional | - |
| `context` | `Any` | Optional | - |

## Example (as JSON)

```json
{
  "eventType": "audit.log",
  "actor": "actor0",
  "action": "action2",
  "context": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

