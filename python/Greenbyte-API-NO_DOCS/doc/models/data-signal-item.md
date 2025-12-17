
# Data Signal Item

A data signal, including type.

## Structure

`DataSignalItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_signal_id` | `int` | Required | The unique id of a data signal.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Required | - |
| `mtype` | `str` | Required | - |
| `unit` | `str` | Required | - |
| `device_type` | [`DeviceType`](../../doc/models/device-type.md) | Optional | - |

## Example (as JSON)

```json
{
  "dataSignalId": 1,
  "title": "Wind speed",
  "type": "Wind speed",
  "unit": "m/s",
  "deviceType": {
    "deviceTypeId": 1,
    "title": "Turbine"
  }
}
```

