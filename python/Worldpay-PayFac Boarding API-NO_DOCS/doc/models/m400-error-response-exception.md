
# M400 Error Response Exception

## Structure

`M400ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M400Error]`](../../doc/models/m400-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "400",
  "httpStatusMessage": "BAD_REQUEST",
  "correlationId": "correlationId2",
  "errors": [
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

