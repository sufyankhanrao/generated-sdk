
# Pass Token Post Response

## Structure

`PassTokenPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_pass_token` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enablePassToken": true,
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode4",
  "httpStatusMessage": "httpStatusMessage8"
}
```

