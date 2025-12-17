
# Data Signal

A data signal.

## Structure

`DataSignal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_signal_id` | `int` | Required | The unique id of a data signal.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Required | - |
| `unit` | `str` | Required | - |

## Example (as JSON)

```json
{
  "dataSignalId": 1,
  "title": "Wind Speed",
  "unit": "m/s"
}
```

