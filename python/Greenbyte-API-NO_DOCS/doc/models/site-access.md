
# Site Access

A site access.

## Structure

`SiteAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_access_id` | `int` | Optional | The id of a site access.<br><br>**Constraints**: `>= 1` |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `device_ids` | `List[int]` | Optional | Device ids associated with the site access.<br><br>**Constraints**: `>= 1` |
| `task_ids` | `List[int]` | Optional | Task ids associated with the site access.<br><br>**Constraints**: `>= 1` |
| `site_access_personnel` | [`List[SiteAccessPersonnel]`](../../doc/models/site-access-personnel.md) | Optional | Personnel associated with the site access. |
| `timestamp_start` | `datetime` | Optional | The timestamp when the site access is/was planned to start. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end_expected` | `datetime` | Optional | The timestamp when the site access is/was planned to end. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Optional | The timestamp when the site access actually ended. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `log_on_comment` | `str` | Optional | A comment for when logging on to the site. |
| `log_off_comment` | `str` | Optional | A comment for when logging off from the site. |

## Example (as JSON)

```json
{
  "siteAccessId": 214,
  "siteId": 2,
  "deviceIds": [
    114,
    115
  ],
  "taskIds": [
    126,
    127,
    128
  ],
  "siteAccessPersonnel": [
    {
      "personnelId": 170,
      "firstName": "firstName4",
      "lastName": "lastName2",
      "company": "company8",
      "phoneNumber": "phoneNumber8"
    }
  ]
}
```

