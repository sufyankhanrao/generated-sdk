
# Pin Debit Post Response

## Structure

`PinDebitPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_pin_debit` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enablePinDebit": true,
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage2"
}
```

