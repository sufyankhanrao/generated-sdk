
# Goe for Decumulation Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoeForDecumulationInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `future_annuity_proj` | `bool` | Required | If set to True, provides an array of future annuity projections. |
| `risk_profile` | [`RiskProfile`](../../doc/models/risk-profile.md) | Required | Defines the user’s risk profile – does not vary by goal for each investor. <br>         On a default basis, GOE is configured for three Risk Profile levels, but it can be customized for up to five levels. |
| `current_portfolio_id` | `int` | Required | Displays the current portfolio index that the goal is allocated to;                     if GOE is getting executed for the first time, it should be null.                    For cases where updated probability is needed in between the scheduled re-allocation dates,                    this parameter should be set to the portfolio index the investor is assigned to. |
| `date_of_birth` | `str` | Required | Investor’s DOB |
| `gender` | `str` | Optional | Gender is mandatory if the type of mortality table to be used is 'Unisex', 'GenderBased', 'GenderAndHealthStatusBased'. Gender should not be passed if the type of mortality table to be used is 'HealthStatusBased'. |
| `health_status` | `int` | Optional | Health status is mandatory if the type of mortality table to be used is 'HealthStatusBased', 'GenderAndHealthStatusBased' |
| `db_income` | `List[float]` | Required | Income from DB plans, if any. All the values in the array must be rounded off to one decimal. |
| `other_guaranteed_income` | `List[float]` | Required | Other guaranteed income, if any. All the values in the array must be rounded off to one decimal. |
| `existing_annuities_income` | `List[float]` | Required | Income from existing annuities, if any. All the values in the array must be rounded off to one decimal. |
| `state_income` | `List[float]` | Required | Income from State Pension or Social Security. All the values in the array must be rounded off to one decimal. |
| `target_expenditures` | `List[float]` | Required | Total expenditure goals of the investor. All the values in the array must be rounded off to one decimal. |
| `fixed_expense_fact` | `List[float]` | Required | Fixed Expenses as a percentage of total expenditures. Value range from 0 to 1. |
| `current_wealth` | `float` | Required | Current wealth when the GOE is being called or executed. At the time of initial onboarding, currentWealth = initialInvestment.                                                             At subsequent re-allocation dates, currentWealth would be the portfolio account value at the time.<br><br>**Constraints**: `>= 0` |
| `initial_investment` | `float` | Required | Defines the initial investment amount to the goal. Its value must be rounded to one decimal place.<br><br>**Constraints**: `>= 0` |
| `include_annuities` | `bool` | Required | Flag to include annuitisation and annuity income in recommendation. If client needs annuitisation , this needs to be set to true when calling GOE on each re-allocation date. |
| `infusion_type` | [`InfusionType`](../../doc/models/infusion-type.md) | Required | Indicates the frequency of cash flows – determines the cash flow array corresponding to the ‘infusions’ parameter. |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which infusions/withdrawals                     would be realized for the goal. Format is "dd-mm-yyyy" <br>                     If not passed or value is null, the algorithm would consider the first reallocation date as the cashflow date. |
| `start_date` | `str` | Required | Defines the start date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `end_date` | `str` | Required | Defines the end date of goal.Valid input format is date – ‘dd-mm-yyyy’ |
| `curr_date` | `str` | Optional | This is an optional parameter that can be used to simulate the current date to be the specified value. <br>                     GOE will process the request as if you are making the API call on the specified date. If not passed, the current system date will be used as the current date. |
| `annuity_rate` | `float` | Required | Annuity payout rate for the investor. Its value must be rounded to four decimal places. |
| `reallocation_freq` | [`ReallocationFreq1`](../../doc/models/reallocation-freq-1.md) | Required | Describes the frequency of re-allocation. If set to 'yearly', GOE would assume the re-allocation to happen once a year. Response parameters such as portfolio path and wealth path would have one value each year. |
| `retirement_age` | `int` | Optional | Captures the retirement age of the investor.<br><br>**Default**: `65` |
| `is_new_goal_priority` | `bool` | Required | If investor/end user changes the goal priority in between the re-allocation dates, this is set to ‘true’.                                     For new plans, this needs to be ‘true’. |
| `is_new_risk_profile` | `bool` | Required | If investor/end user changes the risk profile in between the re-allocation dates, this is set to ‘true’.                                                 For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Required | If investor/end user changes the goal investment tenure after onboarding and before the next immediate re-allocation date,                                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_goal` | `bool` | Required | If investor/end user changes the target expenditures, state income, income from existing annuities, income from defined benefits or other guaranteed income in between the re-allocation dates, this is set to ‘true’. |
| `reallocate` | `bool` | Optional | If the client wants GOE to reallocate between the scheduled re-allocation dates, this should be set to ‘true’.<br><br>**Default**: `False` |
| `loss_threshold` | `float` | Required | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>                                                 If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. If a number value is passed, GOE would consider that amount as the loss threshold.<br>                                                 If loss threshold is not available, this needs to be passed as ‘null’, and GOE would calculate the loss threshold and return as a part of the response ‘loss threshold’. <br>                                                 This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br><br>**Constraints**: `>= 0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "futureAnnuityProj": true,
  "riskProfile": "Aggressive",
  "currentPortfolioId": null,
  "dateOfBirth": "15-06-2020",
  "gender": "unisex",
  "healthStatus": 0,
  "dbIncome": [
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0
  ],
  "otherGuaranteedIncome": [
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0
  ],
  "existingAnnuitiesIncome": [
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0
  ],
  "stateIncome": [
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0,
    1000.0
  ],
  "targetExpenditures": [
    20400.0,
    20808.0,
    21224.2,
    21648.7,
    22081.7
  ],
  "fixedExpenseFact": [
    30.3
  ],
  "currentWealth": 10000.0,
  "initialInvestment": 100000.0,
  "includeAnnuities": true,
  "infusionType": "yearly",
  "cashflowDate": "01-01-2024",
  "startDate": "01-01-2023",
  "endDate": "01-01-2052",
  "annuityRate": 0.0865,
  "reallocationFreq": "yearly",
  "retirementAge": 65,
  "isNewGoalPriority": true,
  "isNewRiskProfile": true,
  "isNewInvestmentTenure": true,
  "isNewGoal": true,
  "reallocate": false,
  "lossThreshold": 100000.0,
  "currDate": "currDate0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

