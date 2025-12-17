
# Default Response

## Structure

`DefaultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[Error]`](../../doc/models/error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "ERROR_CODE",
  "httpStatusMessage": "STATUS-MESSAGE",
  "correlationId": "correlationId4",
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
    },
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

