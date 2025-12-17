
# Goal Profile List Wealth Splitter Model

*This model accepts additional fields of type Any.*

## Structure

`GoalProfileListWealthSplitterModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Unique identifier for each goal |
| `goal_value` | `float` | Required | Target goal amount |
| `purpose` | `str` | Required | Type of goal (for example, ‘Children’s education, Vacation, etc.’) |
| `curr_wealth` | `float` | Required | Current wealth allocated for the goal when the Initial Wealth Splitter is being called or executed. |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which infusions/withdrawals                                                                 would be realized for the goal. Format is "dd-mm-yyyy" <br>                                                                 If not passed or value is null, the algorithm would consider the first reallocation date as the cashflow date. |
| `loss_threshold` | `float` | Optional | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>                                                 If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. If a number value is passed, GOE would consider that amount as the loss threshold.<br>                                                 If loss threshold is not available, this needs to be passed as ‘null’, and GOE would calculate the loss threshold and return as a part of the response ‘loss threshold’. <br>                                                 This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br><br>**Constraints**: `>= 0` |
| `goal_priority` | [`WeathSplitterGoalPriorityAttribute`](../../doc/models/weath-splitter-goal-priority-attribute.md) | Required | Defines the importance a goal holds for a specific user. Order of priority is Need > Want > Wish > Dream <br>         goalPriority can be from 1 to 4 levels. However, note that Goal priority defines the target probabilities and the loss threshold values.<br>         For example, goals with a higher priority (e.g. Need) would have a higher target goal probability (85%) with a higher (aggressive) loss threshold value (slightly more than IW value) in the current set-up.<br>         This needs to be re-mapped based on the number of goal-priority levels, in case of a change. |
| `cashflow_type` | `str` | Required | Describes the cash flow frequency. <br>                                         Valid input is ‘yearly’ or ‘monthly’. <br>                                         This parameter is provided to account for real-world investors who might put in monthly infusions as opposed to yearly infusions.<br>                                         Monthly infusions would be smaller in value (and hence easier to commit to) vs. yearly infusions. |
| `cashflow` | `List[float]` | Required | Cashflow array – includes any cash infusions and/or withdrawals; length would depend on cashflow_type and the goal tenure |
| `end_date` | `str` | Required | Defines the end date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `scenario_type` | `str` | Required | Determines the type of the scenario, the suggested portfolio and the wealth glide path is created accordingly. <br>                                             ‘regular’ for regular goals accumulation goals where cash flows are positive (contributions) and with a typical target wealth <br>                                             ‘retirement’ for scenarios where a decumulation period is included: <br>                                             1.	Scenarios with an accumulation period (and an initial wealth) & positive cash flows followed by a decumulation period with withdrawals (negative cash flows) with or without an inheritance <br>                                             2.	Scenarios with an initial wealth followed by a decumulation period with or without an inheritance |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goal_id": "Goal_1",
  "goalValue": 1000000.0,
  "purpose": "Saving",
  "curr_wealth": 829415.0,
  "cashflowDate": "15-06-2020",
  "goalPriority": "Need",
  "cashflowType": "monthly",
  "cashflow": [
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "endDate": "01-01-2033",
  "scenarioType": "retirement",
  "lossThreshold": 206.68,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

