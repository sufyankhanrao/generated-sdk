
# Downtime Event

A downtime event.

## Structure

`DowntimeEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `downtime_event_id` | `int` | Optional | The id of a downtime event.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Optional | The timestamp when the downtime is/was planned to start. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Optional | The timestamp when the downtime is/was planned to end. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `comment` | `str` | Optional | A comment describing the downtime event. |
| `device_ids` | `List[int]` | Optional | **Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Optional | **Constraints**: `>= 1` |
| `task_ids` | `List[int]` | Optional | **Constraints**: `>= 1` |
| `remaining_capacity_percentage` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "timestampStart": "01/01/2020 00:00:00",
  "timestampEnd": "01/08/2020 00:00:00",
  "remainingCapacityPercentage": 50.5,
  "downtimeEventId": 138,
  "comment": "comment0",
  "deviceIds": [
    196
  ]
}
```

