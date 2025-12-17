
# Upa Goal Response

*This model accepts additional fields of type Any.*

## Structure

`UpaGoalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Goal identifier for individual goal. |
| `goal_amt` | `List[float]` | Required | Accumulation only Goals: Target wealth value associated with the goal at end of goal tenure.             Accumulation & Decumulation, and decumulation/income goals: Goal value (withdrawal)                 each year during decumulation period. |
| `start_date` | `str` | Required | Accumulation Goals: Beginning date of the goal - this is typically the date of initial             investment for accumulation goals.<br> Accumulation & Decumulation, and decumulation/income goals:                 Date when the first withdrawal/income starts. |
| `end_date` | `str` | Required | Accumulation Goals: End date of the goal - when a lumpsum is due. <br> Accumulation & Decumulation, and decumulation/income goals: Date of last withdrawal. |
| `priority` | `str` | Required | Goal priority. |
| `modified_goal_amt` | `List[float]` | Required | Modified goal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalID": "Goal1",
  "goalAmt": [
    70.51,
    70.52,
    70.53
  ],
  "startDate": "01-01-2021",
  "endDate": "01-01-2031",
  "priority": "Dream",
  "modifiedGoalAmt": [
    220.14
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

