
# Safer Payments Get Response

## Structure

`SaferPaymentsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `division_code` | `str` | Optional | The Division under which the submerchant is grouped. If the Division code needs to be updated for a submerchant, it can be done using PATCH /submerchants/{id} endpoint with the Division code sent in the request body |
| `program` | `str` | Optional | - |
| `non_validation_fee_enabled` | `bool` | Optional | Indicates if merchant will be charged for non-validation fee |
| `pci_scan_data` | [`ScanData`](../../doc/models/scan-data.md) | Optional | - |
| `saq_data` | [`SaqData`](../../doc/models/saq-data.md) | Optional | - |

## Example (as JSON)

```json
{
  "divisionCode": "001",
  "program": "Basic",
  "nonValidationFeeEnabled": true,
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage6"
}
```

