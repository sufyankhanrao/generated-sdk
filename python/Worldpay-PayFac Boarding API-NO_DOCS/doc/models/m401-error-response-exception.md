
# M401 Error Response Exception

## Structure

`M401ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M401Error]`](../../doc/models/m401-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "401",
  "httpStatusMessage": "UNAUTHORIZED",
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

