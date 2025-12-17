
# Internal Server Message Exception

*This model accepts additional fields of type Any.*

## Structure

`InternalServerMessageException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | message |
| `status_code` | `int` | Required | statuscode |
| `body` | `str` | Required | body |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Internal Server Error",
  "statusCode": 500,
  "body": "Unexpected error: Please contact FT GOE Business team.",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

