
# Highresdata Response

An object containing a single data point for a specific device and data signal.

## Structure

`HighresdataResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `int` | Required | The id of a device.<br><br>**Constraints**: `>= 1` |
| `data_signal` | [`DataSignal`](../../doc/models/data-signal.md) | Required | A data signal. |
| `data` | `Dict[str, float]` | Required | One or more key value pairs with timestamp as key and the data measurement as value. The timestamps are in UTC. |

## Example (as JSON)

```json
{
  "deviceId": 88,
  "dataSignal": {
    "dataSignalId": 1,
    "title": "Wind Speed",
    "unit": "m/s"
  },
  "data": {
    "2021-04-09T04:14:18Z": 5.81789970397949,
    "2021-04-09T04:14:48Z": 5.43127489089966,
    "2021-04-09T04:15:18Z": 7.41247510910034,
    "2021-04-09T04:15:48Z": 5.58427476882935
  }
}
```

