
# Goal Calculator Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoalCalculatorInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_new_goal` | `bool` | Required | If investor/end user changes the goal amount, in between the re-allocation dates, this is set to ‘true’. For retirement scenarios, this would be a change in retirement income goal, while for a capital accumulation goal,                                                 this would be a change in the lumpsum accumulation target. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_risk_profile` | `bool` | Required | If investor/end user changes the goal priority in between the re-allocation dates, this is set to ‘true’.                                                 For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Required | If investor/end user changes the goal investment tenure after onboarding and before the next immediate re-allocation date,                                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_goal_priority` | `bool` | Required | If investor/end user changes the goal priority in between the re-allocation dates, this is set to ‘true’.                                     For new plans, this needs to be ‘true’. |
| `reallocate` | `bool` | Optional | If the client wants GOE to reallocate between the scheduled re-allocation dates, this should be set to ‘true’.<br><br>**Default**: `False` |
| `use_age_based_cap` | `bool` | Optional | By default, the risk profile of the participant is considered while determining the max equity exposure                                 available for GOE to optimize. When opted for this feature, the risk profile of the participant is ignored and the max equity allocation (available for GOE to optimize) is determined using the participant’s current age, retirement age and a mapper table determining the maximum equity allocation<br><br>**Default**: `False` |
| `reallocation_freq` | [`ReallocationFreq`](../../doc/models/reallocation-freq.md) | Required | Describes the frequency of re-allocation. |
| `get_path` | `bool` | Required | Show ideal portfolio path over time. If getPath parameter is set to False, the portfolio path would not be returned in the response payload |
| `current_portfolio_id` | `int` | Required | Displays the current portfolio index that the goal is allocated to;                                                      if GOE is getting executed for the first time, it should be null. |
| `loss_threshold` | `int` | Required | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>         If the input parameter ‘lossThreshold’ is not passed or value is ‘null’, this parameter is calculated by GOE.         If the input parameter ‘lossThreshold’ is a number value, GOE will consider this as the loss threshold.<br><br>**Constraints**: `>= 0` |
| `scenario_type` | [`ScenarioType`](../../doc/models/scenario-type.md) | Required | Determines the type of the scenario, the suggested portfolio and the wealth glide path is created accordingly. |
| `curr_date` | `str` | Optional | This is an optional parameter that can be used to simulate the current date to be the specified value. <br>                                                     GOE will process the request as if you are making the API call on the specified date. If not passed, the current system date will be used as the current date. |
| `risk_profile` | [`RiskProfile`](../../doc/models/risk-profile.md) | Required | Defines the user’s risk profile – does not vary by goal for each investor. <br>         On a default basis, GOE is configured for three Risk Profile levels, but it can be customized for up to five levels. |
| `initial_investment` | `float` | Required | Defines the initial investment amount to the goal.<br><br>**Constraints**: `>= 0` |
| `current_wealth` | `float` | Required | Current wealth when the GOE is being called or executed. At the time of initial onboarding, currentWealth = initialInvestment.                                                             At subsequent re-allocation dates, currentWealth would be the portfolio account value at the time.<br><br>**Constraints**: `>= 0` |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which infusions/withdrawals                                                                 would be realized for the goal. Format is "dd-mm-yyyy" <br>                                                                 If not passed or value is null, the algorithm would consider the first reallocation date as the cashflow date. |
| `calibrate_recommendations` | `bool` | Optional | Setting this parameter to true will ensure that GOE runs a calibration logic for the recommendations so                     that incorporating the recommendations would result in reaching the goal probability target (for example, 85% for a Need priority).<br><br>**Default**: `False` |
| `goal_priority` | [`GoalCalculatorGoalPriorityAttribute`](../../doc/models/goal-calculator-goal-priority-attribute.md) | Required | Defines the importance a goal holds for a specific user. Order of priority is Need > Want > Wish > Dream <br>         goalPriority can be from 1 to 4 levels. However, note that Goal priority defines the target probabilities and the loss threshold values. |
| `goal_amount` | `float` | Required | For regular scenarios, either the goal amount field shouldn't be provided in the input payload, or if provided, it should either be 'null' or '0.<br>         For retirement cases where  the intent is to calculate an appropriate bequest amount, the bequest (“goal_amt”) should be specified as ‘null’ or ‘0’. For other cases, it can any number greater than zero.<br><br>**Constraints**: `>= 0` |
| `start_date` | `str` | Required | Defines the start date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `end_date` | `str` | Required | Defines the end date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `infusion_type` | [`InfusionType`](../../doc/models/infusion-type.md) | Required | Indicates the frequency of cash flows – determines the cash flow array corresponding to the ‘infusions’ parameter. |
| `infusions` | `List[float]` | Required | Cash flows from the user, recurring payments yearly <br>                                                        The length for this parameter is dynamic depending on the goal tenure, start date and end date.                                                        The reference will always be on the created date. So, the first infusion will be on the first day of the goal                                                         followed by infusions every year/month followed by the last infusion/withdrawal on the last day of the goal.<br> <br>                                                         The values are positive in case of infusions; negative in case of withdrawals; zero in case of no cashflows; frequency depends on ‘infusion_type’ parameter |
| `stepup_date` | `str` | Optional | This is a optional and nullable parameter used for determining the stepup date in case of monthly cashflows that are supposed to be inflation adjusted. The trigger would be through passing the 'inflation' parameter in the user payload. |
| `inflation` | `float` | Optional | This is a optional parameter which captures the user-provided inflation number, to be considered (only) in the yearly/monthly recommendations.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `current_age` | `int` | Optional | Captures the current age of the investor.<br>         Optional Parameter.Need to be passed if ‘considerMortality’ is set to True or ‘requiredDataAvailable’ is set to False. |
| `retirement_age` | `int` | Optional | Captures the retirement age of the investor.<br>         Optional Parameter.Need to be passed if ‘considerMortality’ is set to True or ‘requiredDataAvailable’ is set to False. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "isNewGoal": true,
  "isNewRiskProfile": true,
  "isNewInvestmentTenure": true,
  "isNewGoalPriority": true,
  "reallocate": false,
  "useAgeBasedCap": false,
  "reallocationFreq": "yearly",
  "getPath": true,
  "currentPortfolioId": null,
  "lossThreshold": null,
  "scenarioType": "regular",
  "currDate": "19-09-2023",
  "riskProfile": "Aggressive",
  "initialInvestment": 100000.0,
  "currentWealth": 100000.0,
  "calibrateRecommendations": true,
  "goalPriority": "Need",
  "goalAmount": 0.0,
  "startDate": "19-09-2023",
  "endDate": "01-11-2032",
  "infusionType": "yearly",
  "infusions": [
    0.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    5000.0,
    0.0
  ],
  "stepupDate": "01-01-2024",
  "inflation": 0,
  "cashflowDate": "cashflowDate6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

