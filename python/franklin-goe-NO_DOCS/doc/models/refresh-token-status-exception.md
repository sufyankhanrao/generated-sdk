
# Refresh Token Status Exception

*This model accepts additional fields of type Any.*

## Structure

`RefreshTokenStatusException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `str` | Required | - |
| `message` | `str` | Required | message |
| `status_code` | `int` | Required | status code |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "body": "body4",
  "message": "Invalid Refresh Token",
  "statusCode": 400,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

