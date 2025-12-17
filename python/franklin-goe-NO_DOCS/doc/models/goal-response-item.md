
# Goal Response Item

*This model accepts additional fields of type Any.*

## Structure

`GoalResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Goal identifier for individual goal. |
| `goal` | `str` | Required | Name of the goal |
| `orig_curr_wealth` | `float` | Required | Original current wealth of the goal prior to executing Initial Wealth Splitter. |
| `min_initial_needed` | `float` | Required | Minimum initial wealth needed to reach the desired goal probability. |
| `wealth_split` | `float` | Required | Ideal wealth split suggested by the splitter for each goal. It displays 0 when there is no lumpsum left after funding other goals. |
| `shortfall` | `float` | Required | In case of a shortfall in initial wealth, this field denotes the shortfall amount (negative) related to the minimum initial wealth needed. Set to 0 when there is no shortfall. |
| `funded_status` | `str` | Required | Displays the status of the goal if it’s funded or not. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "Goal_ID": "Goal1",
  "Goal": "Saving",
  "Orig_Curr_Wealth": 141412.0,
  "Min_Initial_Needed": 1114000.0,
  "Wealth_Split": 1038906.0,
  "Shortfall": -75094.0,
  "Funded_Status": "Underfunded",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

