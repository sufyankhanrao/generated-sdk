
# Internal Server Message General Exception

*This model accepts additional fields of type Any.*

## Structure

`InternalServerMessageGeneralException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | message |
| `status_code` | `int` | Required | statuscode |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Error message",
  "statusCode": 500,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

