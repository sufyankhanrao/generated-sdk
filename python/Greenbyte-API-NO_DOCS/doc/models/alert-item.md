
# Alert Item

An alert generated for a device based on a rule.

## Structure

`AlertItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `int` | Optional | The id of the device the alert was generated for.<br><br>**Constraints**: `>= 1` |
| `rule_id` | `int` | Optional | The id of the rule the alert is based on.<br><br>**Constraints**: `>= 1` |
| `timestamp_start` | `datetime` | Optional | The timestamp when the alert began. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Optional | The timestamp when the alert ended. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `message` | `str` | Optional | The title of the rule the alert is based on. |
| `comment` | `str` | Optional | A user comment associated with the alert. |
| `description` | `str` | Optional | A description explaning the rule the alert is based on. |
| `details` | `str` | Optional | Additional details for the alert. Note that the structure of this data is subject to change. |

## Example (as JSON)

```json
{
  "timestampStart": "01/01/2020 00:00:00",
  "timestampEnd": "01/08/2020 00:00:00",
  "deviceId": 232,
  "ruleId": 196,
  "message": "message4"
}
```

