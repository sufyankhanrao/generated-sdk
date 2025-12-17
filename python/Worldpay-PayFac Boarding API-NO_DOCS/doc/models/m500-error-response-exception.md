
# M500 Error Response Exception

## Structure

`M500ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M500Error]`](../../doc/models/m500-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "500",
  "httpStatusMessage": "INTERNAL_SERVER_ERROR",
  "correlationId": "correlationId8",
  "errors": [
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    },
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

