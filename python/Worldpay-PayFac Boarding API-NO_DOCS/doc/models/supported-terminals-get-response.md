
# Supported Terminals Get Response

## Structure

`SupportedTerminalsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `terminals` | [`List[Terminal]`](../../doc/models/terminal.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "Success",
  "terminals": [
    {
      "id": "id4",
      "tid": "tid4",
      "model": "model2",
      "frontEnd": "frontEnd4",
      "environment": "environment0"
    },
    {
      "id": "id4",
      "tid": "tid4",
      "model": "model2",
      "frontEnd": "frontEnd4",
      "environment": "environment0"
    }
  ]
}
```

