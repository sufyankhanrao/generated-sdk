
# Data Item

An object containing time-series data for a specific aggregate, data signal and interval.

## Structure

`DataItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregate` | [`AggregateModeEnum`](../../doc/models/aggregate-mode-enum.md) | Required | How data is aggregated in the asset structure.<br><br>**Default**: `"device"` |
| `aggregate_id` | `int` | Required | The id of this aggregate group: device id, site id, or the constant -1 for portfolio. For `siteLevel` aggregation a generated unique id is used. |
| `aggregate_path_names` | `List[str]` | Optional | For `siteLevel` aggregation this contains the title for each level in the hierarchy. For other types of aggregation it will be empty. |
| `device_ids` | `List[int]` | Required | The ids of the devices in this aggregate group.<br><br>**Constraints**: `>= 1` |
| `resolution` | [`ResolutionEnum`](../../doc/models/resolution-enum.md) | Required | The resolution of the data. Note: For requests with *device* as the specified resolution, the actual resolution will be returned e.g. *10minute*. |
| `calculation` | [`CalculationModeEnum`](../../doc/models/calculation-mode-enum.md) | Required | Which operation to use when aggregating data. |
| `data_signal` | [`DataSignal`](../../doc/models/data-signal.md) | Required | A data signal. |
| `data` | `Dict[str, float]` | Required | A dictionary with the **timestamp** as key and the **data measurement** as value.<br><br>The format of the timestamp(s) depends on the **useUtc** attribute you specified in the request.<br><br>In case you specified `useUtc = true` you will get the timestamps in UTC format. Example:<br><br>```<br>{<br>"2022-05-01T00:00:00Z": 8.1,<br>"2022-05-01T00:10:00Z": 6.9,<br>"2022-05-01T00:20:00Z": 6.6,<br>...<br>```<br><br>If you omitted the **useUtc** attribute (*default is* `false`) or you explicitly specified it to `false` you will get the timestamps in the time zone configured in the Greenbyte Platform, in the format stated in the example. Example:<br><br>```<br>{<br>"2022-05-01T02:00:00": 8.1,<br>"2022-05-01T02:10:00": 6.9,<br>"2022-05-01T02:20:00": 6.6,<br>...<br>```<br><br>**Attention**: please notice the lack of the letter `Z` at the end of the timestamp. Also, the configured time zone for the given example is *UTC+2*. |

## Example (as JSON)

```json
{
  "aggregate": "device",
  "aggregateId": 178,
  "deviceIds": [
    208,
    209,
    210
  ],
  "resolution": "15minute",
  "calculation": "sum",
  "dataSignal": {
    "dataSignalId": 1,
    "title": "Wind Speed",
    "unit": "m/s"
  },
  "data": {
    "key0": 89.33,
    "key1": 89.34
  },
  "aggregatePathNames": [
    "aggregatePathNames6",
    "aggregatePathNames5"
  ]
}
```

