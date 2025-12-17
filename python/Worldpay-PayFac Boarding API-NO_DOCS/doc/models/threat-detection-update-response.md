
# Threat Detection Update Response

## Structure

`ThreatDetectionUpdateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_threat_detection` | `bool` | Optional | - |
| `opt_out_date` | `str` | Optional | Opt out date |

## Example (as JSON)

```json
{
  "enableThreatDetection": false,
  "optOutDate": "2006-12-22",
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage6"
}
```

