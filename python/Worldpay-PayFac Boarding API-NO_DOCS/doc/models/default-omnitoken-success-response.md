
# Default Omnitoken Success Response

## Structure

`DefaultOmnitokenSuccessResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `disable_omni_token_raft` | `bool` | Optional | - |
| `disable_omni_token_express` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "disableOmniTokenRAFT": true,
  "disableOmniTokenExpress": true,
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage2"
}
```

