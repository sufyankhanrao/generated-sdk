
# Device

## Structure

`Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `int` | Optional | The id of a device.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Optional | - |
| `alt_title` | `str` | Optional | An alternative title. |
| `identity` | `str` | Optional | Device identification number. |
| `site` | [`Site`](../../doc/models/site.md) | Optional | The site where the device is located. |
| `device_type` | `str` | Optional | The string representation of the device type. |
| `device_type_id` | `int` | Optional | The id of a device type.<br><br>**Constraints**: `>= 1` |
| `parent_id` | `int` | Optional | The id of the parent device, if any.<br><br>**Constraints**: `>= 1` |
| `child_ids` | `List[int]` | Optional | Ids of child devices, if any.<br><br>**Constraints**: `>= 1` |
| `device_model` | [`DeviceModel`](../../doc/models/device-model.md) | Optional | Information about the device manufacturer and model. Applies to devices of device type **other than** `Turbine`. |
| `turbine_type` | [`TurbineType`](../../doc/models/turbine-type.md) | Optional | Turbine type information (manufacturer and model). Only applies to devices of device type `Turbine`. |
| `max_power` | `float` | Optional | The maximum power for a device. |
| `bidding_area` | `str` | Optional | Only applies to Nordic countries and the UK. |
| `timestamp_start` | `datetime` | Optional | The earliest timestamp device data is available for. |
| `latitude` | `str` | Optional | The latitude of the device in the WGS84 system. |
| `longitude` | `str` | Optional | The longitude of the device in the WGS84 system. |
| `elevation` | `str` | Optional | The elevation of the device in meters above sea level. |
| `target_availability` | `float` | Optional | The target availability for the device.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `metadata` | [`List[MetadataField]`](../../doc/models/metadata-field.md) | Optional | A list of metadata fields and their values. |

## Example (as JSON)

```json
{
  "deviceType": "Turbine",
  "deviceId": 14,
  "title": "title6",
  "altTitle": "altTitle8",
  "identity": "identity4",
  "site": {
    "siteId": 14,
    "title": "title0"
  }
}
```

