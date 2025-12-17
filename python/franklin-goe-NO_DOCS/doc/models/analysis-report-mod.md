
# Analysis Report Mod

*This model accepts additional fields of type Any.*

## Structure

`AnalysisReportMod`

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

