
# Goe for Taxes Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoeForTaxesInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reallocate` | `bool` | Optional | If the client wants GOE to reallocate between the scheduled re-allocation dates, this should be set to ‘true’.<br><br>**Default**: `False` |
| `is_new_risk_profile` | `bool` | Required | If the risk profile of the investor has changed, this is set to ‘true’. <br>                                                 For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Required | If investor/end user changes the goal investment tenure after onboarding and before the next immediate re-allocation date, <br>                                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_goal_priority` | `bool` | Required | If investor/end user changes the goal priority of any of the goals within the plan, in between the re-allocation dates, this is set to ‘true’. <br>                                     For new plans, this needs to be ‘true’. |
| `is_near_term_volatility` | `bool` | Optional | When the near-term volatility indicator flashes, this is set to ‘true’. Currently under development, <br>                                                 shold be set to ‘false’.<br><br>**Default**: `False` |
| `is_new_goal` | `bool` | Required | If the end user changes the goal amount / infusions / withdrawals, in between the re-allocation dates, <br>                     this is set to ‘true’. For retirement scenarios, this would be a change in retirement income goal, <br>                     while for a capital accumulation goal, this would be a change in the lumpsum accumulation target. <br>                     For first time calls to GOE, this needs to be set to ‘true’. |
| `get_path` | `bool` | Required | Shows the forward-looking portfolio path over time. |
| `reallocation_freq` | [`ReallocationFreq`](../../doc/models/reallocation-freq.md) | Required | Describes the frequency of re-allocation. |
| `current_portfolio_id` | `int` | Required | Displays the current portfolio index that the goal is allocated to;  <br>                         if GOE is getting executed for the first time, it should be null. |
| `curr_date` | `str` | Optional | This is an optional parameter that can be used to simulate the current date to be the specified value.  <br>                         GOE will process the request as if you are making the API call on the specified date. If not passed,  <br>                             the current system date will be used as the current date. Valid input format is date – ‘dd-mm-yyyy’ |
| `risk_profile` | [`RiskProfile3`](../../doc/models/risk-profile-3.md) | Required | Defines the user’s risk profile. Note that Risk Profiles are mapped to portfolio access.  <br>             For example, a Conservative investor has access to portfolios 1-8 (or 50% Equity) while an Aggressive  <br>             investor has access to all 16 portfolios (up to 90% Equity). This is configurable. |
| `compute_social_security` | `bool` | Required | When set to true computes the social security.  <br>                 Mandatory fields (part of memberList) needed for social security are: “DOB”, “currentSalary”, “socialSecurityStartAge” |
| `use_social_security_for_goals` | `bool` | Required | When set to “true” uses Social Security to meet the withdrawals.  <br>             If set to “false”, and when 'computeSocialSecurity' is set as 'true' - only computes the Social Security but does not use it to fulfil the goals.  <br>            In cases social security (post-tax) is greater than the withdrawal amount, the social security is collected into the taxable accounts.  <br>            If set to “true”, a taxable account must be present. This is because there can be instances where there are no goals in a given year but an incoming social security infusion.  <br>             This infusion can only go into a taxable account. |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which <br>             infusions/withdrawals would be realized for the goal. This parameter is optional. <br>                 If not passed or value is null, the algorithm would consider the first reallocation date as the cashflow date. <br>                     Scheduled cashflows should be planned for a date prior to the 29th of any month. |
| `loss_threshold` | `float` | Optional | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure. <br>                     This is an optional parameter. If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. <br>                     If a number value is passed, GOE would consider that amount as the loss threshold.  <br>                     If loss threshold is not available, this needs to be passed as ‘null’, <br>                     and GOE would calculate the loss threshold and return as a part of the response (‘loss threshold’). <br>                     This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br><br>**Constraints**: `>= 0` |
| `infusion_type` | [`InfusionType3`](../../doc/models/infusion-type-3.md) | Required | Defines if the infusions are at the yearly level or monthly level. |
| `cola_rate` | `float` | Required | Defines the Cost-of-Living Adjustment to be used for Social Security amount computations. |
| `tax_rates` | [`TaxRatesDic2`](../../doc/models/tax-rates-dic-2.md) | Required | Consists of tax rates applicable pre & post-retirement for the entire household |
| `household` | [`HouseholdGoeForTaxesObj2`](../../doc/models/household-goe-for-taxes-obj-2.md) | Required | contains all information about all the participants. |
| `accounts` | [`List[GoeToAccountAttr]`](../../doc/models/goe-to-account-attr.md) | Required | Details of different accounts associated with unique memberID in the household.  <br>                    Note:  <br>                    A single account can be associated with multiple members within the household.  <br>                    This would generally be the case with joint taxable accounts. |
| `goal_profile_list` | [`List[GoalProfileGoeForTaxesAttr]`](../../doc/models/goal-profile-goe-for-taxes-attr.md) | Required | Details related to the withdrawals associated with the plan where a plan is defined as a collection of goals. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "cashflowDate": "02-05-2025",
  "currDate": "02-05-2025",
  "reallocate": false,
  "isNewRiskProfile": false,
  "isNewInvestmentTenure": false,
  "isNewGoalPriority": false,
  "isNearTermVolatility": false,
  "isNewGoal": false,
  "getPath": true,
  "reallocationFreq": "yearly",
  "currentPortfolioId": null,
  "riskProfile": "Aggressive",
  "infusionType": "yearly",
  "lossThreshold": 0.0,
  "goalProfileList": [
    {
      "goalId": "39623865346539642d366234362d343639362d393332332d356134356563653030336130",
      "goalAmt": [
        666.0
      ],
      "startDate": "02-05-2052",
      "endDate": "02-05-2052",
      "priority": "Need",
      "scenarioType": "retirement",
      "goalPurpose": "non-education",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "computeSocialSecurity": false,
  "useSocialSecurityForGoals": true,
  "household": {
    "householdID": "1",
    "stateOfResidence": "KS",
    "memberList": [
      {
        "memberType": "Primary",
        "memberID": "eff63fdb-1ed8-41be-a0f8-7788fdac728c",
        "DOB": "02-1959",
        "currentAge": 66,
        "retirementAge": 93,
        "currentSalary": 400.0,
        "socialSecurityStartAge": 65,
        "existingMonthlySocialSecurityAmount": 10.0,
        "lifeExpectancy": 93,
        "TDABalanceForRMD": 74.16,
        "RMDUtilized": 37.72
      }
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "colaRate": 0.03,
  "taxRates": {
    "ETRPreRetirement": 0.15,
    "LTCGPreRetirement": 0.15,
    "ETRPostRetirement": 0.2,
    "LTCGPostRetirement": 0.1,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "targetPortfolio": {
    "meanReturn": 0.03,
    "standardDeviation": 0.04
  },
  "accounts": [
    {
      "accountID": "dbcd5e3d-55fb-45f6-a654-d720f056a071",
      "currentBalance": 2,
      "taxabilityType": "D",
      "memberIDs": [
        "eff63fdb-1ed8-41be-a0f8-7788fdac728c"
      ],
      "cashflowDetails": {
        "cashflowAmt": [
          2500.0,
          2575.0,
          2652.0,
          2732.0,
          2814.0,
          2898.0,
          2985.0,
          3075.0,
          3167.0,
          3262.0,
          3360.0,
          3461.0,
          3564.0,
          3671.0,
          3781.0,
          3895.0,
          4012.0,
          4132.0,
          4256.0,
          4384.0,
          4515.0,
          4651.0,
          4790.0,
          4934.0,
          5082.0,
          5234.0,
          5391.0
        ],
        "startDate": "02-05-2025",
        "endDate": "02-05-2051",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "currentHoldings": [
        {
          "categoryName": "CASH",
          "categoryID": "10",
          "categoryPrice": 1.0,
          "quantity": 2.0,
          "costBasis": 2.0,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "accountType": "IRA",
      "lockExpiry": 0,
      "meanReturn": 0.03,
      "standardDeviation": 0.04
    }
  ]
}
```

