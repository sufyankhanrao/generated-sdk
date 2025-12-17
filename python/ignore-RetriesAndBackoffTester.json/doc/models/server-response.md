
# Server Response

## Structure

`ServerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `passed` | `bool` | Required | - |
| `retry_count` | `int` | Required | - |
| `idle_time_between_api_calls` | `List[int]` | Optional | - |

## Example (as JSON)

```json
{
  "passed": false,
  "retryCount": 250,
  "idleTimeBetweenApiCalls": [
    126,
    127,
    128
  ]
}
```

