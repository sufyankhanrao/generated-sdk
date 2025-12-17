
# Response 401 Token Exception

## Structure

`Response401tokenException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Optional | Response code |
| `error` | `str` | Optional | Unauthorized |
| `message` | `str` | Optional | Invalid token |

## Example (as JSON)

```json
{
  "statusCode": 401,
  "error": "Unauthorized",
  "message": "Invalid token"
}
```

