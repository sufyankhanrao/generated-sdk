
# Device Access

A device access

## Structure

`DeviceAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_access_id` | `int` | Optional | The id of a device access.<br><br>**Constraints**: `>= 1` |
| `site_access_id` | `int` | Optional | The id of a site access.<br><br>**Constraints**: `>= 1` |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `device_ids` | `List[int]` | Optional | The associated device ids.<br><br>**Constraints**: `>= 1` |
| `personnel_ids` | `List[int]` | Optional | The associated personnel ids.<br><br>**Constraints**: `>= 1` |
| `task_ids` | `List[int]` | Optional | The associated task ids.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Optional | The timestamp when the device access is/was planned to start. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end_expected` | `datetime` | Optional | The timestamp when the device access is/was planned to end. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Optional | The timestamp when the device access actually ended. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `log_on_comment` | `str` | Optional | A comment for when logging on to the device. |
| `log_off_comment` | `str` | Optional | A comment for when logging off from the device. |

## Example (as JSON)

```json
{
  "deviceAccessId": 60,
  "siteAccessId": 88,
  "siteId": 124,
  "deviceIds": [
    244,
    245
  ],
  "personnelIds": [
    48,
    49,
    50
  ]
}
```

