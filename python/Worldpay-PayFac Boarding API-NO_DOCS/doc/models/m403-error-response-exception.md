
# M403 Error Response Exception

## Structure

`M403ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M403Error]`](../../doc/models/m403-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "403",
  "httpStatusMessage": "FORBIDDEN",
  "correlationId": "correlationId0",
  "errors": [
    {
      "errorCode": "errorCode6",
      "errorMessage": "errorMessage8",
      "target": "target2"
    }
  ]
}
```

