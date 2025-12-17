
# Error Model 1 Exception

## Structure

`ErrorModel1Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_message` | `str` | Required | - |
| `server_code` | `str` | Optional | - |
| `model` | [`Validate`](../../doc/models/validate.md) | Required | - |

## Example (as JSON)

```json
{
  "ServerMessage": "ServerMessage2",
  "ServerCode": "ServerCode8",
  "model": {
    "field": "field4",
    "name": "name2",
    "address": "address8"
  }
}
```

