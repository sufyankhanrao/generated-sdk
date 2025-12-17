
# Goe With Annuities Output Model

*This model accepts additional fields of type Any.*

## Structure

`GoeWithAnnuitiesOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `retirement_goal` | `float` | Required | Recommended yearly retirement income goal |
| `retirement_goal_min` | `float` | Required | Minimum recommended yearly retirement income goal |
| `retirement_goal_max` | `float` | Required | Maximum recommended yearly retirement income goal |
| `income_from_outside_assets` | `float` | Required | Projected income from outside assets. |
| `income_from_ss` | `float` | Required | Projected Social Security income |
| `income_from_others` | `float` | Required | Projected income from other sources. |
| `allocation_to_annuities` | `float` | Required | Balance to be allocated to annuities. |
| `allocation_to_goe` | `float` | Required | Balance to be allocated to GOE. |
| `recommended_portfolio_id` | `int` | Required | Recommended portfolio index for the participant. |
| `retirement_goal_probability` | `float` | Required | Probability of achieving the retirement goal |
| `recommended_consumption` | `float` | Required | Recommended yearly consumption |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "retirementGoal": 60000.0,
  "retirementGoalMin": 50000.0,
  "retirementGoalMax": 75000.0,
  "incomeFromOutsideAssets": 2000.0,
  "incomeFromSS": 2000.0,
  "incomeFromOthers": 10000.0,
  "allocationToAnnuities": 1000.0,
  "allocationToGOE": 20000.0,
  "recommendedPortfolioID": 8,
  "retirementGoalProbability": 0.8513,
  "recommendedConsumption": 60000.0,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

