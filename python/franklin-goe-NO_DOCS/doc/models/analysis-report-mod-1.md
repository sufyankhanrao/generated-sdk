
# Analysis Report Mod 1

In the event the original plan doesn’t meet the desired probability (in line with the priority), <br>                     the plan is modified by dropping less important goal – denoted by lower priority.- <br>                     This section gives details of the GOE run for the modified plan.<br>                     Please note that the modification of goals is driven by business logic.

*This model accepts additional fields of type Any.*

## Structure

`AnalysisReportMod1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goals_response` | [`List[GoalsResponse]`](../../doc/models/goals-response.md) | Required | Details of original and modified goal |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalsResponse": [
    {
      "goalID": "Goal2",
      "goalAmt": [
        179.05
      ],
      "startDate": "01-12-2023",
      "endDate": "30-11-2025",
      "modifiedGoalAmt": [
        72.68,
        72.69
      ],
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

