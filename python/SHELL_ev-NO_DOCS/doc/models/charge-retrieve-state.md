
# Charge Retrieve State

## Structure

`ChargeRetrieveState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | Describes the session state<br><br>started, stopped, start-requested, stop-requested, failed-to-start, failed-to-stop |
| `error` | [`ChargeError`](../../doc/models/charge-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "status": "status6",
  "error": {
    "code": "code2",
    "message": "message4"
  }
}
```

