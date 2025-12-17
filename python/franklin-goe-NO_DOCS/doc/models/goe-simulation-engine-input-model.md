
# Goe Simulation Engine Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoeSimulationEngineInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reallocate` | `bool` | Optional | Set as “true” when a newportfolio is needed.<br><br>**Default**: `False` |
| `is_new_goal_priority` | `bool` | Optional | If investor/end user changes the goal priority of any of the goals within the plan, in between the re-allocation dates, this is set to ‘true’. <br>                                     For new plans, this needs to be ‘true’. |
| `reallocation_freq` | [`ReallocationFreq`](../../doc/models/reallocation-freq.md) | Required | Describes the frequency of re-allocation. |
| `current_portfolio_id` | `int` | Required | Displays the current portfolio assigned to a user. For the firsttime user, this should be set as “null”. |
| `curr_date` | `str` | Optional | The date on which GOE-SOFT call is made.<br>             Valid input format is date –‘dd-mm-yyyy’. |
| `risk_profile` | [`RiskProfile4`](../../doc/models/risk-profile-4.md) | Required | Defines the user’s risk profile, which is mapped to one or more portfolios.This is customizable. |
| `compute_social_security` | `bool` | Required | When set to true computes the social security. <br>                 Mandatory fields (part of memberList) needed for social security are: “DOB”, “currentSalary”, “socialSecurityStartAge” |
| `use_social_security_for_goals` | `bool` | Required | When set to “true” uses Social Security to meet the withdrawals. <br>             If set to “false”, and when 'computeSocialSecurity' is set as 'true' - only computes the Social Security but does not use it to fulfil the goals. <br>            In cases social security (post-tax) is greater than the withdrawal amount, the social security is collected into the taxable accounts. <br>             If no taxable accounts are present, SocialSecurity left – after meeting the goals – is ignored. |
| `cashflow_date` | `str` | Optional | Cashflow date of the goal - this is the date (year is ignored) on which infusions/withdrawals would be realized for the goal. <br>            This parameter is optional.  If not passed or value is null,             the algorithm would consider the first reallocation date as the cashflow date. |
| `is_new_risk_profile` | `bool` | Required | If the risk profile of the investor has changed, this is set to ‘true’. <br>                                                 For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_investment_tenure` | `bool` | Optional | If investor/end user changes the goal investment tenure after onboarding and before the next immediate re-allocation date, <br>                                     this is set to ‘true’. For first time calls to GOE, this needs to be set to ‘true’. |
| `is_new_goal` | `bool` | Optional | If the end user changes the goal amount / infusions / withdrawals, in between the re-allocation dates, <br>                     this is set to ‘true’. For retirement scenarios, this would be a change in retirement income goal, <br>                     while for a capital accumulation goal, this would be a change in the lumpsum accumulation target. <br>                     For first time calls to GOE, this needs to be set to ‘true’. |
| `loss_threshold` | `float` | Optional | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure. <br>                     This is an optional parameter. If not passed or value is ‘null’, the GOE algo would calculate the loss threshold. <br>                     If a number value is passed, GOE would consider that amount as the loss threshold.  <br>                     If loss threshold is not available, this needs to be passed as ‘null’, <br>                     and GOE would calculate the loss threshold and return as a part of the response (‘loss threshold’). <br>                     This amount needs to be stored, and should be passed as ‘lossThreshold’ on subsequent GOE calls.<br>                     Valid Input: non-negative values.<br><br>**Constraints**: `>= 0` |
| `infusion_type` | [`InfusionType3`](../../doc/models/infusion-type-3.md) | Required | Defines if the infusions are at the yearly level or monthly level. |
| `cola_rate` | `float` | Required | Defines the Cost-of-Living Adjustment to be used for Social Security amount computations.<br>             When passed as “null”, this is assumed to be 0%. |
| `tax_rates` | [`TaxRates2`](../../doc/models/tax-rates-2.md) | Required | Consists of tax rates applicable pre & post-retirement. |
| `household` | [`Household2`](../../doc/models/household-2.md) | Required | contains all information about all the participants within the household.                         For MVP, only a single member is allowed. |
| `accounts` | [`List[Account]`](../../doc/models/account.md) | Required | Details of different accounts associated with unique memberID in the household. |
| `goal_profile_list` | [`List[GoalProfileSimulationEngine]`](../../doc/models/goal-profile-simulation-engine.md) | Required | Details related to the withdrawals associated with the plan where a plan is defined as a collection of goals. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "reallocate": false,
  "isNewGoalPriority": false,
  "reallocationFreq": "yearly",
  "currentPortfolioId": null,
  "currDate": "01-01-2023",
  "riskProfile": "Aggressive",
  "computeSocialSecurity": true,
  "useSocialSecurityForGoals": true,
  "cashflowDate": "01-01-2023;",
  "isNewRiskProfile": true,
  "isNewInvestmentTenure": false,
  "isNewGoal": false,
  "infusionType": "yearly",
  "colaRate": 0.02,
  "taxRates": {
    "LTCGPreRetirement": 0.15,
    "LTCGPostRetirement": 0.15,
    "ETRPreRetirement": 0.15,
    "ETRPostRetirement": 0.15,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "household": {
    "householdID": "house_1",
    "stateOfResidence": "CA",
    "memberList": [
      {
        "DOB": "12-1968",
        "RMDUtilized": 2000.0,
        "TDABalanceForRMD": 10000.0,
        "currentAge": 55,
        "currentSalary": 50000.0,
        "existingMonthlySocialSecurityAmount": 1000.0,
        "memberID": "1234",
        "memberType": "Primary",
        "retirementAge": 65,
        "socialSecurityStartAge": 62,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "accounts": [
    {
      "accountID": "5",
      "accountType": "401k",
      "taxabilityType": "T",
      "memberIDs": [
        "memberIDs0"
      ],
      "currentBalance": 14589.0,
      "currentHoldings": [
        {
          "categoryName": "CASH",
          "categoryID": "10",
          "categoryPrice": 1.0,
          "quantity": 200000.0,
          "costBasis": 14589.0,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "cashflowDetails": {
        "startDate": "01-03-2024",
        "endDate": "01-11-2032",
        "cashflowAmt": [
          2500.0,
          2575.0
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
  ],
  "goalProfileList": [
    {
      "bequest": false,
      "endDate": "01-12-2067",
      "goalAmt": [
        2215916.68281757,
        2282394.1833021,
        2350866.00880116,
        2421391.9890652,
        2494033.74873716,
        2568854.76119927,
        2645920.40403525,
        2725298.01615631,
        2807056.95664099,
        2891268.66534022
      ],
      "goalId": "Goal1",
      "goalPurpose": "Non-education",
      "priority": "Need",
      "scenarioType": "retirement",
      "startDate": "01-12-2059"
    },
    {
      "bequest": false,
      "endDate": "01-01-2025",
      "goalAmt": [
        10600.0
      ],
      "goalId": "Goal2",
      "goalPurpose": "Non-education",
      "priority": "Want",
      "scenarioType": "regular",
      "startDate": "01-01-2023"
    },
    {
      "bequest": false,
      "endDate": "01-01-2028",
      "goalAmt": [
        31907.039
      ],
      "goalId": "Goal3",
      "goalPurpose": "Non-education",
      "priority": "Want",
      "scenarioType": "regular",
      "startDate": "01-01-2023"
    },
    {
      "bequest": false,
      "endDate": "02-04-2025",
      "goalAmt": [
        5061.361
      ],
      "goalId": "Goal4",
      "goalPurpose": "Non-education",
      "priority": "Dream",
      "scenarioType": "regular",
      "startDate": "01-01-2023"
    },
    {
      "bequest": false,
      "endDate": "02-01-2048",
      "goalAmt": [
        407057.448
      ],
      "goalId": "Goal5",
      "goalPurpose": "Non-education",
      "priority": "Dream",
      "scenarioType": "regular",
      "startDate": "01-01-2023"
    },
    {
      "bequest": false,
      "endDate": "06-02-2024",
      "goalAmt": [
        5024.45469099256
      ],
      "goalId": "Goal6",
      "goalPurpose": "Non-education",
      "priority": "Want",
      "scenarioType": "regular",
      "startDate": "01-01-2023"
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

