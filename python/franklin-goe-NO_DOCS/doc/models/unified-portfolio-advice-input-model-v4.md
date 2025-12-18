
# Unified Portfolio Advice Input Model V4

*This model accepts additional fields of type Any.*

## Structure

`UnifiedPortfolioAdviceInputModelV4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_new_goal_priority` | `bool` | Required | If the investor/end user changes the priority of any of the goals within the plan,             in between the re-allocation dates, this should be set to ‘true’.             For new plans, this needs to be ‘true’. |
| `is_new_risk_profile` | `bool` | Required | If the risk profile of the investor/end user  has changed, this should be set to ‘true’.                      For new plans, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Required | If the investor/end user changes the goal investment tenure of any of the goals within the plan,                      in between re-allocation dates, this should be set to ‘true’.For new plans, this needs to be ‘true’. |
| `is_near_term_volatility` | `bool` | Optional | When the near-term volatility indicator flashes, this is set to ‘true’. For first time calls to GOE,                                                 this needs to be set to ‘true’.<br><br>**Default**: `False` |
| `is_new_goal` | `bool` | Required | If the investor/end user changes the goal amount in between the re-allocation dates,              this is set to ‘true’. For retirement scenarios, this would be a change in the retirement income goal,                  while for a capital accumulation goal, this would be a change in the lump sum accumulation target.                      For new plans, this needs to be set to ‘true’. |
| `cashflow_date` | `str` | Optional | Cashflow date of the plan - this is typically the date (year is ignored) on which infusions/withdrawals would happen for the goals.                                                                 Format is "dd-mm-yyyy". <br>                                                                 If the cashflowDate parameter is set to null, the algorithm would consider the first reallocation date as the cashflow date. |
| `get_path` | `bool` | Required | If this parameter is set to False, GOE would not compute the portfolio path ,wealth path and cashflow recommendations. |
| `reallocation_freq` | [`ReallocationFreq5`](../../doc/models/reallocation-freq-5.md) | Required | Describes the frequency of re-allocation. If set to 'yearly',             GOE would assume the re-allocation to happen once a year. |
| `initial_investment` | `float` | Required | Defines the lump sum initial welath of the plan.<br><br>**Constraints**: `>= 0` |
| `current_wealth` | `float` | Required | Current wealth of the plan/combined goal when the GOE is being called or executed At the time of initial onboarding, currentWealth is null. On subsequent dates, currentWealth would be the portfolio account value at the time.<br><br>**Constraints**: `>= 0` |
| `current_portfolio_id` | `int` | Required | Current portfolio index that the combined plan is allocated to; if algo is getting executed for the first time (onboarding call), it should be null.        For cases where updated probability is needed in between the scheduled re-allocation dates, this parameter should be set to the portfolio index the investor is assigned to. |
| `infusions` | `List[float]` | Required | Net cash flow array for the plan/combined goal. Positive in the case of infusions; negative in             case of withdrawals; zero in case of no cashflows; frequency depends on ‘infusionType’.            For subsequent calls, the infusions array needs to be adjusted based on the time that has elapsed. |
| `risk_profile` | [`RiskProfile7`](../../doc/models/risk-profile-7.md) | Required | Defines the user’s risk profile. Note that Risk Profiles are mapped to portfolio access. For example, a Conservative investor has access to portfolios 1-8 (or 50% Equity) while an Aggressive investor has access to all 16 portfolios (up to 90% Equity). <br> On a default basis, GOE is configured for three Risk Profile levels, but it can be customized for up to five levels. |
| `infusion_type` | `str` | Required | Indicates the frequency of cash flows – Determines the cash flow array. |
| `curr_date` | `str` | Optional | This is an optional parameter that can be used to simulate the current date being the specified value. <br>                                                     GOE will process the request as if you are making the API call on the specified date. If not passed, the current system date will be used as the current date.<br><br>**Default**: `'System Date'` |
| `loss_threshold` | `float` | Optional | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>                                                 If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. If a number value is passed, GOE would consider that amount as the loss threshold.<br>                                                 If loss threshold is not available, this needs to be passed as ‘null’, and GOE would calculate the loss threshold and return as a part of the response ‘loss threshold’. <br>                                                 This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br><br>**Constraints**: `>= 0` |
| `goal_profile_list` | [`List[GoalProfile]`](../../doc/models/goal-profile.md) | Required | List of goal profiles |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "isNewGoalPriority": true,
  "isNewRiskProfile": true,
  "isNewInvestmentTenure": true,
  "isNewGoal": true,
  "calibrateGoalRec": true,
  "isNearTermVolatility": false,
  "getPath": true,
  "currentPortfolioId": null,
  "riskProfile": "Aggressive",
  "currentWealth": null,
  "reallocationFreq": "yearly",
  "initialInvestment": 86000.0,
  "infusionType": "yearly",
  "cashflowDate": "01-01-2021",
  "currDate": "04-01-2021",
  "infusions": [
    0.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    4000.0,
    -21000.0,
    -19000.0,
    -75000.0,
    -23000.0,
    -23000.0,
    -23000.0
  ],
  "goalProfileList": [
    {
      "goalID": "Goal1",
      "goalAmt": [
        25000.0
      ],
      "startDate": "01-01-2021",
      "endDate": "01-01-2031",
      "priority": "Need",
      "scenarioType": "regular",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "goalID": "Goal2",
      "goalAmt": [
        52000.0
      ],
      "startDate": "01-01-2021",
      "endDate": "01-01-2033",
      "priority": "Need",
      "scenarioType": "regular",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "goalID": "Goal3",
      "goalAmt": [
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0,
        2000.0
      ],
      "startDate": "01-01-2022",
      "endDate": "01-01-2036",
      "priority": "Need",
      "scenarioType": "retirement",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "goalID": "Goal4",
      "goalAmt": [
        21000.0,
        21000.0,
        21000.0,
        21000.0,
        21000.0
      ],
      "startDate": "01-01-2032",
      "endDate": "01-01-2036",
      "priority": "Need",
      "scenarioType": "retirement",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "lossThreshold": 69.98
}
```

