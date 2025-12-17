
# Autopay Schedule

## Structure

`AutopaySchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `frequency_type` | `str` | Optional | Defines how often clients are charged. Possible values are:<br><br>* SetNumberOfAutopays<br>* MonthToMonth |
| `frequency_value` | `int` | Optional | The interval of AutoPay frequency, combined with `FrequencyTimeUnit`. This value is null if `FrequencyType` is `MonthToMonth`. |
| `frequency_time_unit` | `str` | Optional | Defines the time unit that sets how often to run the AutoPay, combined with `FrequencyValue`. This value is null if `FrequencyType` is `MonthToMonth`. Possible values are:<br><br>* Weekly<br>* Monthly<br>* Yearly |

## Example (as JSON)

```json
{
  "FrequencyType": "FrequencyType2",
  "FrequencyValue": 132,
  "FrequencyTimeUnit": "FrequencyTimeUnit8"
}
```

