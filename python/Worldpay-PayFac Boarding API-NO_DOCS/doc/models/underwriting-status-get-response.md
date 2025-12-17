
# Underwriting Status Get Response

## Structure

`UnderwritingStatusGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `underwriting_status` | [`UnderwritingStatus`](../../doc/models/underwriting-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage6",
  "underwritingStatus": {
    "id": "id8",
    "status": "Pending",
    "reason": "reason6"
  }
}
```

