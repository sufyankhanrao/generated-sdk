
# Response Webhook

## Structure

`ResponseWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type119Enum`](../../doc/models/type-119-enum.md) | Optional | Resource Type<br><br>**Default**: `'Webhook'` |
| `data` | [`Data34`](../../doc/models/data-34.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "basic_auth_username8",
    "basic_auth_password": "basic_auth_password0",
    "expands": "expands2",
    "format": "api-default"
  }
}
```

