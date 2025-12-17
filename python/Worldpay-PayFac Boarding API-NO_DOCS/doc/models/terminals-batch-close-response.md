
# Terminals Batch Close Response

## Structure

`TerminalsBatchCloseResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `chain_code` | `str` | Optional | Chain code |
| `chain_name` | `str` | Optional | Name assocaited with the chain code |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | - |
| `terminal_details` | [`List[TerminalBatchCloseTimeDetails]`](../../doc/models/terminal-batch-close-time-details.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "Success",
  "chainCode": "0A1B2C",
  "chainName": "PayFac Chain 001"
}
```

