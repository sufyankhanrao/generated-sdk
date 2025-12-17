
# Run Pipe Input Model

*This model accepts additional fields of type Any.*

## Structure

`RunPipeInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_new_goal_priority` | `bool` | Required | If investor/end user changes the goal priority in between the re-allocation dates, <br>                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Required | If investor/end user changes the goal investment tenure after onboarding and before the next immediate re-allocation date,<br>                                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_risk_profile` | `bool` | Required | If the risk profile of the investor has changed, this should be set to ‘true’.<br>                    For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_goal` | `bool` | Required | If investor/end user changes the goal amount, in between the re-allocation dates, this is set to ‘true’. <br>                    For retirement scenarios, this would be a change in retirement income goal, while for a capital accumulation goal,                     this would be a change in the lumpsum accumulation target. For first time calls to GOE, this needs to be set to ‘true’. |
| `reallocate` | `bool` | Optional | If the client wants GOE to reallocate between the scheduled re-allocation dates, this should be set to ‘true’.<br><br>**Default**: `False` |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which infusions/withdrawals <br>                                                                would be realized for the goal. Format is "dd-mm-yyyy" <br>                                                                 If not passed or value is null, the algorithm would consider the first reallocation date as the cashflow date. |
| `loss_threshold` | `float` | Optional | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>                                                 If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. If a number value is passed, GOE would consider that amount as the loss threshold.<br>                                                 If loss threshold is not available, this needs to be passed as ‘null’, and GOE would calculate the loss threshold and return as a part of the response ‘loss threshold’. <br>                                                 This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br><br>**Constraints**: `>= 0` |
| `get_path` | `bool` | Required | Show ideal portfolio path over time. If getPath parameter is set to False, the portfolio path would not be returned in the response payload |
| `reallocation_freq` | [`ReallocationFreq`](../../doc/models/reallocation-freq.md) | Required | Describes the frequency of re-allocation. |
| `goal_amount` | `float` | Required | Defines the target wealth value associated with the goal at end of goal tenure.<br><br>**Constraints**: `>= 0` |
| `initial_investment` | `float` | Required | Defines the initial investment amount to the goal.<br><br>**Constraints**: `>= 0` |
| `current_wealth` | `float` | Required | Current wealth when the GOE is being called or executed. At the time of initial onboarding, currentWealth = initialInvestment. <br>                                                            At subsequent re-allocation dates, currentWealth would be the portfolio account value at the time.<br><br>**Constraints**: `>= 0` |
| `start_date` | `str` | Required | Defines the start date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `end_date` | `str` | Required | Defines the end date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `curr_date` | `str` | Optional | This is an optional parameter that can be used to simulate the current date to be the specified value. <br>                     GOE will process the request as if you are making the API call on the specified date. <br>                     If not passed, the current system date will be used as the current date.<br>                     Valid input format is date – ‘dd-mm-yyyy’. |
| `goal_priority` | [`GoalPriority`](../../doc/models/goal-priority.md) | Required | Defines the importance a goal holds for a specific user. Order of priority is Need > Want > Wish > Dream <br>         goalPriority can be from 1 to 4 levels. However, note that Goal priority defines the target probabilities and the loss threshold values. |
| `current_portfolio_id` | `int` | Required | Displays the current portfolio index that the goal is allocated to; <br>                    if GOE is getting executed for the first time, it should be null. |
| `infusions` | `List[float]` | Required | Cash flows from the user, recurring payments yearly <br>                                                        The length for this parameter is dynamic depending on the goal tenure, start date and end date.<br>                                                        The reference will always be on the created date. So, the first infusion will be on the first day of the goal <br>                                                        followed by infusions every year/month followed by the last infusion/withdrawal on the last day of the goal.<br>                                                         The values are positive in case of infusions; negative in case of withdrawals; zero in case of no cashflows; frequency depends on ‘infusion_type’ parameter |
| `risk_profile` | [`RiskProfile6`](../../doc/models/risk-profile-6.md) | Required | Defines the user’s risk profile – does not vary by goal for each investor. <br>             On a default basis, GOE is configured for three Risk Profile levels, but it can be customized for up to five levels. <br>             Note that Risk Profiles are mapped to portfolio access.This is nullable and non mandatory if useAgeBasedCap is true |
| `scenario_type` | [`ScenarioType1`](../../doc/models/scenario-type-1.md) | Required | Determines the type of the scenario, the suggested portfolio and the wealth glide path is created accordingly. <br>                     ‘regular’ for regular goals accumulation goals where cash flows are positive (contributions) and with a typical target wealth <br>                     ‘retirement’ for scenarios where a decumulation period is included: <br>                     1. Scenarios with an accumulation period (and an initial wealth) & positive cash flows followed <br>                     by a decumulation period with withdrawals (negative cash flows) with or without an inheritance <br>                     2. Scenarios with an initial wealth followed by a decumulation period with or without an inheritance. |
| `infusion_type` | [`InfusionType`](../../doc/models/infusion-type.md) | Required | Indicates the frequency of cash flows – determines the cash flow array corresponding to the ‘infusions’ parameter. |
| `current_age` | `int` | Optional | Captures the current age of the investor. <br>             Optional Parameter.Need to be passed if ‘useAgeBasedCap’ is set to True or ‘requiredDataAvailable’ is set to False. |
| `retirement_age` | `int` | Optional | Captures the retirement age of the investor. <br>                 Optional Parameter.Considered as 65 if not passed |
| `risk_override` | `bool` | Optional | This is an optional parameter to disable GOE’s default de-risking logic. <br>                     When set to False, GOE considers the default de-risking logic.the goal and the allocation advice <br>                     When set to True, GOE will not consider the default de-risking logic and will consider the risk profile of the participant for portfolio access. |
| `engaged_participant` | `bool` | Optional | This applies only to retirement use cases which specifies whether a participant is engaged or unengaged. If the “currentAge” and the <br>        “retirementAge” are passed, they will be used to determine the de-risking criteria; If set to true GOE <br>        will de-risk 5 years before retirement and if set to false GOE will de-risk 1 year before retirement as per the default admin configuration settings |
| `required_data_available` | `bool` | Optional | This indicates to GOE if all the mandatory data parameters that are required to run the GOE algorithm are available or not.<br>          If all the mandatory fields are available, this parameter is set to true, and they need be passed to run GOE. <br>         If all the mandatory fields are not available, this parameter is set to false, and they need not be passed to run GOE except the 'currentAge' and <br>        the “retirementAge”; The API response body would contain only the recommended portfolio and the portfolio path, which is derived from a pre-determined glide path <br>        based on the current age and the retirement age (this would be defaulted to 65 if not passed). All other response parameters would be null.<br><br>**Default**: `True` |
| `wealth_path_probabilities` | `List[float]` | Optional | This is an optional input parameter. If this input is passed, instead of one wealth path, the GOE output will <br>         have 3 wealth paths –one path at the goal priority probability level and one path for each of the 2 probability values passed in this input array.<br><br>**Constraints**: *Minimum Items*: `2`, *Maximum Items*: `2`, `>= 0`, `<= 1` |
| `last_reallocation_probability` | `float` | Optional | The goal probability as of last reallocation needs to be passed.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `last_reallocation_date` | `str` | Optional | The date on which last reallocation call was made to GOE.Format - dd-mm-yyyy |
| `plan_id` | `str` | Optional | Plan ID of the partipant. |
| `participant_id` | `str` | Optional | ID of the partipant. |
| `source_id` | `str` | Optional | Source ID of the plan |
| `use_age_based_cap` | `bool` | Optional | This is an optional parameter set as false by default. If this is passed as <br>                     ‘true’ – the maximum number of portfolios at any age would be restricted based <br>                     on a pre-defined glide path based on the number years to retirement; <br>                     The ‘currentAge’ and ‘retirementAge’ become mandatory fields. This applies only to retirement goals.<br><br>**Default**: `False` |
| `inflation` | `float` | Optional | This is an optional field that when provided adjusts the yearly/monthly topup recommendations for inflation<br><br>**Constraints**: `>= 0`, `<= 1` |
| `retirement_date` | `str` | Optional | Optional parameter that can be used to identify periods where cashflow recommendations are applied.             saveMore will be appied before and spendLess will be applied affter the retirement date.            Its format is 'dd-mm-yyyy' |
| `target_portfolio` | `int` | Optional | Defines the portfolio ID that has to be held across the entire goal horizon <br>             during single portfolio mode i.e. buy and hold strategy. <br>             Mandatory if mode is 'single-portfolio'​ |
| `mode` | `str` | Optional | Determines the custom modes that can be invoked by GOE API |
| `min_equity_allocation` | `float` | Optional | Defines the minimum equity allocation for the GOE recommended portfolio.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `max_equity_allocation` | `float` | Optional | Defines the maximum equity allocation for the GOE recommended portfolio.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `allocation_to_annuities` | `float` | Optional | Specifies percenatage of wealth that the user has allocated to annuities externally.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "useAgeBasedCap": false,
  "startDate": "13-01-2021",
  "endDate": "10-10-2055",
  "lastReallocatedDate": "01-01-2020",
  "goalPriority": "Need",
  "initialInvestment": 95027.0,
  "currentWealth": 95027.0,
  "goalAmount": 1000000.0,
  "riskProfile": "Moderate",
  "infusions": [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "reallocationFreq": "yearly",
  "scenarioType": "regular",
  "infusionType": "yearly",
  "cashflowDate": "11-10-2020",
  "isNearTermVolatility": true,
  "isNewGoalPriority": true,
  "isNewInvestmentTenure": true,
  "isNewGoal": true,
  "isNewRiskProfile": true,
  "getPath": true,
  "currentPortfolioId": null,
  "currDate": "13-01-2021",
  "calibrateRecommendations": true,
  "reallocate": false,
  "lossThreshold": 27.52,
  "currentAge": 2
}
```

