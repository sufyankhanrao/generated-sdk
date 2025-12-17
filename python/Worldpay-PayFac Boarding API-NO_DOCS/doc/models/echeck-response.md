
# Echeck Response

## Structure

`EcheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_echeck` | `bool` | Optional | - |
| `echeck_company_number` | `str` | Optional | The Company Number created by the Echeck Processor |

## Example (as JSON)

```json
{
  "echeckCompanyNumber": "435971",
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "enableEcheck": false
}
```

