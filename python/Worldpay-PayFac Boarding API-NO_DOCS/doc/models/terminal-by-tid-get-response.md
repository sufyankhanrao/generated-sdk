
# Terminal by TID Get Response

## Structure

`TerminalByTIDGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `terminal` | [`Terminal`](../../doc/models/terminal.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId0",
  "httpStatusCode": "httpStatusCode4",
  "httpStatusMessage": "httpStatusMessage0",
  "terminal": {
    "id": "id2",
    "tid": "tid8",
    "model": "model0",
    "frontEnd": "frontEnd2",
    "environment": "environment8"
  }
}
```

