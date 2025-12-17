
# Tenure Recommendation 1

Tenure recommendation is at the goal level and is applicable to the highest-ranking goal             within the plan (the recommendation would be to increase the tenure by 25% rounded off to next             highest integral value). In case of an accumulation goal, end date of the goal is to be deferred.             In case of a decumulation/ retirement goal, start date (date of first withdrawal) is to be deferred

*This model accepts additional fields of type Any.*

## Structure

`TenureRecommendation1`

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

