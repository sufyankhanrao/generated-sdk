
# Google Pay Response

## Structure

`GooglePayResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_google_pay` | `bool` | Optional | Determines whether Google Pay has been enabled or disabled |

## Example (as JSON)

```json
{
  "enableGooglePay": false,
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage8"
}
```

