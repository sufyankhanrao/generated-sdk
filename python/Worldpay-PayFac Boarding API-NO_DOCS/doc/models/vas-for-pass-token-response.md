
# Vas for Pass Token Response

## Structure

`VasForPassTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_for_pass_token` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enableForPassToken": false,
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage2"
}
```

