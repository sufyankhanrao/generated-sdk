
# Hse Incidents Response

An HSE incident.

## Structure

`HseIncidentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hse_incident_id` | `int` | Optional | The id of an HSE incident.<br><br>**Constraints**: `>= 1` |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `device_id` | `int` | Optional | The id of a device.<br><br>**Constraints**: `>= 1` |
| `timestamp` | `datetime` | Optional | The timestamp when the incident occurred.<br>The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `hse_category` | [`HSECategoryEnum`](../../doc/models/hse-category-enum.md) | Optional | The category of an HSE incident. |
| `lost_time_injury` | `bool` | Optional | Whether or not the incident resulted in an injury sustained on the job, causing loss of productive work time.<br><br>**Default**: `False` |
| `incident_description` | `str` | Optional | The description related to the incident. |
| `resolved` | `bool` | Optional | Whether or not the incident has been resolved.<br><br>**Default**: `False` |
| `resolved_timestamp` | `datetime` | Optional | The timestamp when the incident has been resolved. |

## Example (as JSON)

```json
{
  "timestamp": "12/18/2022 09:45:00",
  "hseCategory": "NearMiss",
  "lostTimeInjury": false,
  "incidentDescription": "Met mast wires are rusty and mast is unstable.",
  "resolved": false,
  "resolvedTimestamp": "12/18/2022 11:15:00",
  "hseIncidentId": 80,
  "siteId": 142,
  "deviceId": 30
}
```

