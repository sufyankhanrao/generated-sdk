
# Tenure Recommendation

*This model accepts additional fields of type Any.*

## Structure

`TenureRecommendation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Goal identifier for individual goal. |
| `goal_start_date` | `str` | Required | Suggested start date considering tenure recommendation. |
| `goal_end_date` | `str` | Required | Suggested end date considering tenure recommendation. |
| `new_plan_probability` | `float` | Required | New plan probability as per the suggested tenure recommendation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalID": "Goal1",
  "goalStartDate": "13-01-2021",
  "goalEndDate": "01-01-2031",
  "newPlanProbability": 0.3648,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

