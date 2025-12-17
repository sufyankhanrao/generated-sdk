
# Apple Pay Response

## Structure

`ApplePayResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_apple_pay` | `bool` | Optional | Determines whether Apple Pay has been enabled or disabled |

## Example (as JSON)

```json
{
  "enableApplePay": false,
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage6"
}
```

