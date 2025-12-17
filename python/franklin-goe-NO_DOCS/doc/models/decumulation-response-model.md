
# Decumulation Response Model

*This model accepts additional fields of type Any.*

## Structure

`DecumulationResponseModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | - |
| `message` | `str` | Required | - |
| `body` | [`DecumulationResponseBody`](../../doc/models/decumulation-response-body.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statusCode": 174,
  "message": "message8",
  "body": {
    "wealthPath": [
      5000.0,
      5200.0,
      5400.0,
      5600.0
    ],
    "riskThreshold": "High",
    "goalProbability": 0.62,
    "currentGoalProbability": 0.2947,
    "allocationAnnuity": 100001.0,
    "allocationGOE": 200000.5,
    "goalProbabilityLongevityAdjusted": 0.8,
    "payoutGOE": [
      5000.0,
      5200.0,
      5400.0,
      5600.0
    ],
    "recommendedPortfolioId": 10,
    "fundedness": "UnderFunded",
    "guaranteedIncomePercent": 0.91,
    "isGoalRealistic": true,
    "bankruptcyMessage": "NA",
    "additionalPayoutAnnuity": 1007.5,
    "portfolioPath": [
      15.0,
      15.0,
      14.0,
      13.0,
      12.0,
      11.0,
      10.0,
      8.0,
      5.0,
      4.0,
      2.0,
      1.0
    ],
    "payoutAnnuity": [
      5000.0,
      5200.0,
      5400.0,
      5600.0
    ],
    "consumptionGoal": [
      10000.0,
      10200.0,
      10400.0,
      10600.0
    ],
    "recommendedConsumption": [
      10000.0,
      10200.0,
      10400.0,
      10600.0
    ],
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

