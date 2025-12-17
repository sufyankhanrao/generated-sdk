
# Opening Hours Object

## Structure

`OpeningHoursObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `week_day` | [`OpeningHoursObjectWeekDayEnum`](../../doc/models/opening-hours-object-week-day-enum.md) | Optional | 3 letter day of the week |
| `start_time` | `str` | Optional | Hour in 24h local time when the location opens. |
| `end_time` | `str` | Optional | Hour in 24h local time when the location closes. |

## Example (as JSON)

```json
{
  "weekDay": "Mon",
  "startTime": "08:00",
  "endTime": "23:00"
}
```

