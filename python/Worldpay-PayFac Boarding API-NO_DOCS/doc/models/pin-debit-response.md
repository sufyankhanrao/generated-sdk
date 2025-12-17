
# Pin Debit Response

## Structure

`PinDebitResponse`

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
  "enablePinDebit": false,
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage2"
}
```

