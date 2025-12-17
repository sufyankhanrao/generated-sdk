
# Validation Message Two Exception

*This model accepts additional fields of type Any.*

## Structure

`ValidationMessageTwoException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | statuscode |
| `message` | `str` | Required | Validation Error |
| `body` | `str` | Required | Validation error message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statusCode": 400,
  "message": "Validation Error",
  "body": "error description",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

