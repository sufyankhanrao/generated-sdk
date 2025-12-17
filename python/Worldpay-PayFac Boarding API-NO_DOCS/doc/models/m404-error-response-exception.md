
# M404 Error Response Exception

## Structure

`M404ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M404Error]`](../../doc/models/m404-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "404",
  "httpStatusMessage": "NOT FOUND",
  "correlationId": "correlationId8",
  "errors": [
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

