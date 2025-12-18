
# Data Real Time Item

An object containing a single data point for a specific aggregate, data signal and interval.

## Structure

`DataRealTimeItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregate` | [`AggregateModeEnum`](../../doc/models/aggregate-mode-enum.md) | Required | How data is aggregated in the asset structure.<br><br>**Default**: `'device'` |
| `aggregate_id` | `int` | Required | The id of this aggregate group: device id, site id, or the constant -1 for portfolio. For `siteLevel` aggregation a generated unique id is used. |
| `aggregate_path_names` | `List[str]` | Optional | For `siteLevel` aggregation this contains the title for each level in the hierarchy. For other types of aggregation it will be empty. |
| `device_ids` | `List[int]` | Required | The ids of the devices in this aggregate group.<br><br>**Constraints**: `>= 1` |
| `calculation` | [`CalculationModeRealTimeEnum`](../../doc/models/calculation-mode-real-time-enum.md) | Required | Which operation to use when aggregating data. |
| `data_signal` | [`DataSignal`](../../doc/models/data-signal.md) | Required | A data signal. |
| `data` | `Dict[str, float]` | Required | A single key value pair with timestamp as key and the data measurement as value. The timestamps are in UTC. |

## Example (as JSON)

```json
{
  "aggregate": "device",
  "aggregateId": 42,
  "deviceIds": [
    72,
    73,
    74
  ],
  "calculation": "sum",
  "dataSignal": {
    "dataSignalId": 1,
    "title": "Wind Speed",
    "unit": "m/s"
  },
  "data": {
    "2020-01-01T00:00:00Z": 584.33
  },
  "aggregatePathNames": [
    "aggregatePathNames8",
    "aggregatePathNames7"
  ]
}
```

