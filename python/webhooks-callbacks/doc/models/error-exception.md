
# Error Exception

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | Error code |
| `message` | `str` | Required | Human-readable error message |
| `details` | `Any` | Optional | Additional error details |

## Example (as JSON)

```json
{
  "error": "invalid_request",
  "message": "The request body is invalid",
  "details": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

