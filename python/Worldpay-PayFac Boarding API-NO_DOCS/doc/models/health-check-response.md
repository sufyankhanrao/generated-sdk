
# Health Check Response

## Structure

`HealthCheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | Health status of the service |

## Example (as JSON)

```json
{
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage6",
  "status": "UP"
}
```

