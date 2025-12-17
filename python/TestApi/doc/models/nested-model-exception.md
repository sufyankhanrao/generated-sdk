
# Nested Model Exception

## Structure

`NestedModelException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_message` | `str` | Required | - |
| `server_code` | `str` | Required | - |
| `model` | [`Validate`](../../doc/models/validate.md) | Required | - |

## Example (as JSON)

```json
{
  "ServerMessage": "ServerMessage8",
  "ServerCode": "ServerCode2",
  "model": {
    "field": "field4",
    "name": "name2",
    "address": "address8"
  }
}
```

