
# Status Item

A status that may contain statuses of the same type as sub-statuses. Note that for sub-statuses the fields `categoryIec`, `categoryContract`, and `subStatus` will always be null.

## Structure

`StatusItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `turbine_status_id` | `int` | Optional | The id of a turbine status.<br><br>**Constraints**: `>= 1` |
| `device_id` | `int` | Optional | The id of a device.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Optional | The timestamp when the status began. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Optional | The timestamp when the status ended. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `has_timestamp_end` | `bool` | Optional | Indicates whether the status has a duration. |
| `category` | [`StatusCategoryEnum`](../../doc/models/status-category-enum.md) | Optional | The category a status belongs to. |
| `code` | `int` | Optional | The status code. |
| `message` | `str` | Optional | A description of the status code. |
| `comment` | `str` | Optional | A user comment associated with the status. |
| `lost_production_signal` | [`DataSignal`](../../doc/models/data-signal.md) | Optional | A data signal. |
| `lost_production` | `float` | Optional | The lost production in kWh associated with the status. This field<br>will be null if the caller is not authorized for the system-configured<br>lost production signal. The configured lost production signal is available<br>via the `/configuration.json` endpoint (`DataSignalConfiguration` schema). |
| `category_iec` | `str` | Optional | The status category as defined by the IEC. |
| `category_contract` | `str` | Optional | The status category as defined in the service availability contract assigned to the site. |
| `category_global_contract` | `str` | Optional | The status category as defined in the global availability contract assigned to the site. |
| `category_custom_contract` | `str` | Optional | The status category as defined in the custom availability contract assigned to the site. |
| `sub_status` | [`List[StatusItem]`](../../doc/models/status-item.md) | Optional | Statuses of the same type that have been grouped under this status. |
| `acknowledged` | `bool` | Optional | Indicates whether the status has been acknowledged. |
| `component` | `Any` | Optional | The status component categorization. |

## Example (as JSON)

```json
{
  "timestampStart": "01/01/2020 00:00:00",
  "timestampEnd": "01/08/2020 00:00:00",
  "lostProductionSignal": {
    "dataSignalId": 1,
    "title": "Wind Speed",
    "unit": "m/s"
  },
  "turbineStatusId": 116,
  "deviceId": 230,
  "hasTimestampEnd": false
}
```

