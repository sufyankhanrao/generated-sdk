
# Internal Server Message 1 Exception

*This model accepts additional fields of type Any.*

## Structure

`InternalServerMessage1Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | error message |
| `status_code` | `int` | Required | statuscode |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Internal Server Error",
  "statusCode": 500,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

