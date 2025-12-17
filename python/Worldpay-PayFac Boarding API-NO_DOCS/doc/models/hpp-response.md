
# HPP Response

## Structure

`HPPResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_google_pay` | `bool` | Optional | Determines whether HPP has been enabled or disabled |

## Example (as JSON)

```json
{
  "enableGooglePay": false,
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage6"
}
```

