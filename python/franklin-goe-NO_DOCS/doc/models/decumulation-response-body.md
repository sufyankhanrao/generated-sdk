
# Decumulation Response Body

*This model accepts additional fields of type Any.*

## Structure

`DecumulationResponseBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wealth_path` | `List[float]` | Required | Projected Wealth Path |
| `risk_threshold` | `str` | Required | Solvency Risk/ Risk Threshold |
| `goal_probability` | `float` | Required | Probability of meeting the GOE Payout without adjusting for Longevity. |
| `current_goal_probability` | `float` | Required | - |
| `allocation_annuity` | `float` | Required | Wealth allocated to Annuities |
| `allocation_goe` | `float` | Required | Wealth allocated to GOE |
| `goal_probability_longevity_adjusted` | `float` | Required | Probability of meeting the GOE Payout after adjusting for Longevity |
| `payout_goe` | `List[float]` | Required | Estimated Payout from GOE. The first element of the array represents the suggested payout from GOE on the current date, while the next elements represent the suggested payout from GOE on following cashflow dates. |
| `recommended_portfolio_id` | `int` | Required | recommended portfolio index from GOE |
| `fundedness` | `str` | Required | Current Fundedness status |
| `guaranteed_income_percent` | `float` | Required | % of expenditures from Guaranteed Income based on input parameters. |
| `is_goal_realistic` | `bool` | Required | To understand if the goal can be met with a reasonable probability (set by the ‘unrealistic’ goal probability value in the GOE config).                    If current goal probability < desired target goal probability (defined by the goal priority), the goal is termed unrealistic. |
| `bankruptcy_message` | `str` | Required | Message about bankruptcy probability |
| `additional_payout_annuity` | `float` | Required | Estimated additional Payout from annuities this year. |
| `portfolio_path` | `List[float]` | Required | Projected Portfolio Path |
| `payout_annuity` | `List[float]` | Required | Estimated Payout from Annuities. The first element of the array represents the payout from annuities on the current date, while the next elements represent the payout from annuities on following cashflow dates. |
| `consumption_goal` | `List[float]` | Required | Consumption goal for GOE. The first element of the array represents the consumption goal on the current date, while the next elements represent the consumption goal on following cashflow dates. |
| `recommended_consumption` | `List[float]` | Required | Total recommended consumption/Income from all income sources. The first element of the array represents the recommended consumption on the current date, while the next elements represent the recommended consumptions on following cashflow dates. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
}
```

