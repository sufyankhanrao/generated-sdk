
# Worklog Response

A worklog item.

## Structure

`WorklogResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `worklog_item_id` | `int` | Optional | The id of a worklog item.<br><br>**Constraints**: `>= 1` |
| `timestamp` | `datetime` | Optional | The timestamp when the worklog item was entered. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `hours_worked` | `float` | Optional | The number of hours worked on the worklog item. |
| `comment` | `str` | Optional | The comment related to the worklog item. |

## Example (as JSON)

```json
{
  "timestamp": "01/01/2023 00:00:00",
  "hoursWorked": 2.5,
  "comment": "Inverter B Offline With Repeated Fault\n- Work Performed: INV B was cleaned\n",
  "worklogItemId": 60,
  "siteId": 132
}
```

