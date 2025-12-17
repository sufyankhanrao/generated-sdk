
# Pinless Debit Response

## Structure

`PinlessDebitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_pinless_debit` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enablePinlessDebit": false,
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage8"
}
```

