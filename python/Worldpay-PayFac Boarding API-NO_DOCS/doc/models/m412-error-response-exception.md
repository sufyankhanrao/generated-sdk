
# M412 Error Response Exception

## Structure

`M412ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `errors` | [`List[M412Error]`](../../doc/models/m412-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "httpStatusCode": "412",
  "httpStatusMessage": "PRECONDITION FAILED",
  "correlationId": "correlationId2",
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

