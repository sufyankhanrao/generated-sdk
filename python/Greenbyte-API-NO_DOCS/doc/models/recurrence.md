
# Recurrence

Recurrence settings for the task. To calculate when the
task is recurring, use the `timestampStart` field and
then add to it multiples of the specified interval; the
`intervalType` field determines if the task is recurring
on daily, weekly, monthly, or yearly basis.

If the task is not recurring, this field is null.

**Note:** Only the main (first) task in a recurring
series have recurrence settings. For the other tasks in
the series, the field `mainTaskId` can be used to find
it.

## Structure

`Recurrence`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duration` | `int` | Optional | The interval with which the task repeats. |
| `duration_type` | [`DurationTypeEnum`](../../doc/models/duration-type-enum.md) | Optional | The type of with which the task repeats. |
| `date_end` | `date` | Optional | When the recurring task series ends (exclusive).<br><br>The end date is **not** included in the<br>recurring task series: for example, to have a<br>task series occur until and including the last<br>day of March 2020, set `dateEnd` to<br>"2020-04-01". |

## Example (as JSON)

```json
{
  "duration": 42,
  "durationType": "day",
  "dateEnd": "2016-03-13"
}
```

