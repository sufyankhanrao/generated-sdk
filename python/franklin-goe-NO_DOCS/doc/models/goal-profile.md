
# Goal Profile

*This model accepts additional fields of type Any.*

## Structure

`GoalProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Goal identifier for individual goal. |
| `goal_amt` | `List[float]` | Required | Accumulation only Goals:              Target wealth value associated with the goal at end of goal tenure.<br><br>              Accumulation & Decumulation, and decumulation/income goals: goal value (withdrawal) each year                  during the decumulation period. For subsequent calls, the goalAmt list needs to be updated based on the time that has elapsed. |
| `start_date` | `str` | Required | Accumulation Goals: beginning date of the goal - this is typically the date of initial investment for accumulation goals. For subsequent calls, the original start date for the goal needs to be passed.                           <br>Accumulation & Decumulation, and decumulation/income goals: date when the first withdrawal/income starts. For subsequent calls, the original start date (date of first withdrawal) for the goal needs to be passed. |
| `end_date` | `str` | Required | Accumulation Goals: end date of the goal - when a lumpsum is due.                         <br>Accumulation & Decumulation, and decumulation/income goals: date of last withdrawal. |
| `priority` | `str` | Required | Defines the importance a goal holds for a specific user.          Order of priority is Need > Want > Wish > Dream. Goal priority defines the target probabilities and             the loss threshold values. For example, goals with a higher priority (e.g. Need) would have a                  higher target goal probability (85%) with a higher (aggressive) loss threshold value. |
| `scenario_type` | `str` | Required | ‘regular’ for regular goals accumulation goals where cash flows are positive (contributions)             and with a typical target wealth.<br><br>            ‘retirement’ for scenarios where a decumulation period is included: <br>            1. Scenarios with an accumulation period (and an initial wealth) & positive cash flows followed by                 a decumulation period with withdrawals (negative cash flows) with or without an inheritance.<br>                    2. Scenarios with an initial wealth followed by a decumulation period with or without an inheritance. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalID": "Goal1",
  "goalAmt": [
    41400.0,
    41400.0,
    41400.0,
    41400.0,
    41400.0
  ],
  "startDate": "01-01-2022",
  "endDate": "01-01-2026",
  "priority": "Need",
  "scenarioType": "retirement",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

