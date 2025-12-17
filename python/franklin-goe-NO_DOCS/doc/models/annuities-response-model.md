
# Annuities Response Model

*This model accepts additional fields of type Any.*

## Structure

`AnnuitiesResponseModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | - |
| `message` | `str` | Required | - |
| `body` | [`GoeWithAnnuitiesOutputModel`](../../doc/models/goe-with-annuities-output-model.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statusCode": 200,
  "message": "Success",
  "body": {
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
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

