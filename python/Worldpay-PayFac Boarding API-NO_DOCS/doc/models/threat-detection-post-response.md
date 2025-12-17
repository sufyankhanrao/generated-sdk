
# Threat Detection Post Response

## Structure

`ThreatDetectionPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_threat_detection` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enableThreatDetection": true,
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4"
}
```

