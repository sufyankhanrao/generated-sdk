
# Pinless Debit Post Response

## Structure

`PinlessDebitPostResponse`

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
  "enablePinlessDebit": true,
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage6"
}
```

