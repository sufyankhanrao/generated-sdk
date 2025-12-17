
# Goe With Annuities Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoeWithAnnuitiesInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_annuities` | `bool` | Required | Flag to recommend allocation to annuities. |
| `annuity_type` | [`AnnuityType`](../../doc/models/annuity-type.md) | Optional | Type of annuity. [non-functional] |
| `annuity_price` | [`List[AnnuityPrice]`](../../doc/models/annuity-price.md) | Optional | Annuity price series <br>        Mandatory only if includeAnnuities is true.         For a deferred annuity - complete age year rate         table to be passed covering all ages from        current age to retirement age. |
| `annuity_payout_freq` | [`AnnuityPayoutFreq`](../../doc/models/annuity-payout-freq.md) | Optional | Frequency of the annuity payouts. |
| `date_of_birth` | `str` | Required | Participant’s date of birth. <br>        Accepts date in dd-mm-yyyy format. |
| `retirement_age` | `int` | Required | Participant’s retirement age. <br>            Accepts positive numbers only. |
| `drawdown_age` | `int` | Required | Participant’s drawdown age. <br>            Accepts positive numbers, greater than or equal to the retirementAge. |
| `planning_age` | `int` | Required | Age of last withdrawal. <br>            Accepts positive numbers, greater than the drawdownAge. |
| `marital_status` | [`MaritalStatus`](../../doc/models/marital-status.md) | Optional | Participant’s marital status. |
| `current_salary` | `float` | Required | Participant’s current salary <br>            Accepts positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `spousal_salary` | `float` | Optional | Participant's spouse's current salary.            Valid values are positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `job_tenure` | `int` | Optional | Participant’s current job tenure. [non-functional]<br><br>**Constraints**: `>= 0` |
| `total_account_balance` | `float` | Required | Total balance in the account. <br>            Valid values: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `balance_proportion` | `float` | Required | Proportion of the total account balance invested in the GOE. <br>            Valid values: decimals between 0 and 1, up to 4 decimal places.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `periodic_contributions` | `float` | Required | Periodic contribution amount.<br>            Valid values: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `contribution_freq` | [`ContributionFreq`](../../doc/models/contribution-freq.md) | Required | Frequency of the periodic contributions. |
| `current_annuity_balance` | `float` | Optional | Current balance of annuity assets.<br>            Valid values: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `current_annuity_income` | `float` | Optional | Current accumulated yearly income from annuity as of the             drawdown age. <br>            Valid values: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `retirement_income_goal` | `float` | Optional | Total yearly retirement income goal for the participant.<br>            Valid values: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `drawdown_age_ss` | `int` | Optional | Participant’s social security drawdown age. <br>            Valid values: positive whole numbers, greater than or equal to retirement age. |
| `income_from_ss` | `float` | Optional | Total yearly income from the participant from social security. <br>            Valid inputs: positive numbers with up to 2 decimal places. |
| `outside_assets` | `float` | Required | Total balance in outside assets <br>        Valid inputs: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `other_income` | `float` | Optional | Income from other sources. This is the sum of income from DB and             other annuities. <br>            Valid inputs: positive numbers with up to 2 decimal places.<br><br>**Constraints**: `>= 0` |
| `other_income_freq` | [`OtherIncomeFreq`](../../doc/models/other-income-freq.md) | Optional | Frequency of other income.<br>            Required only if otherIncome is provided. |
| `current_portfolio_id` | `int` | Required | Current portfolio ID to which the wealth is allocated. If GOE             is being called for the first time, this should be null. [non-functional] <br>            Valid inputs: null or positive integers. |
| `calculate_retirement_income_goal` | `bool` | Optional | Flag to ask GOE to calculate the retirement income goal |
| `current_date` | `str` | Required | Participant’s current date. <br>            Valid input: date in dd-mm-yyyy format |
| `risk_profile` | [`RiskProfile5`](../../doc/models/risk-profile-5.md) | Required | Participant’s risk profile. |
| `auto_escalation` | `float` | Optional | Auto escalation amount. [non-functional]<br><br>**Constraints**: `>= 0`, `<= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "annuityType": "deferred",
  "annuityPrice": [
    {
      "age": 43,
      "value": [
        {
          "year": 2024,
          "rate": 10.0,
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
    {
      "age": 44,
      "value": [
        {
          "year": 2025,
          "rate": 10.0,
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
    {
      "age": 45,
      "value": [
        {
          "year": 2026,
          "rate": 10.0,
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
    {
      "age": 46,
      "value": [
        {
          "year": 2027,
          "rate": 10.0,
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
    {
      "age": 47,
      "value": [
        {
          "year": 2028,
          "rate": 10.0,
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
    {
      "age": 48,
      "value": [
        {
          "year": 2029,
          "rate": 10.0,
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
    {
      "age": 49,
      "value": [
        {
          "year": 2030,
          "rate": 10.0,
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
    {
      "age": 50,
      "value": [
        {
          "year": 2031,
          "rate": 10.0,
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
    {
      "age": 51,
      "value": [
        {
          "year": 2032,
          "rate": 10.0,
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
    {
      "age": 52,
      "value": [
        {
          "year": 2033,
          "rate": 10.0,
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
    {
      "age": 53,
      "value": [
        {
          "year": 2034,
          "rate": 10.0,
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
    {
      "age": 54,
      "value": [
        {
          "year": 2035,
          "rate": 10.0,
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
    {
      "age": 55,
      "value": [
        {
          "year": 2036,
          "rate": 10.0,
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
    {
      "age": 56,
      "value": [
        {
          "year": 2037,
          "rate": 10.0,
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
    {
      "age": 57,
      "value": [
        {
          "year": 2038,
          "rate": 10.0,
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
    {
      "age": 58,
      "value": [
        {
          "year": 2039,
          "rate": 10.0,
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
    {
      "age": 59,
      "value": [
        {
          "year": 2040,
          "rate": 10.0,
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
    {
      "age": 60,
      "value": [
        {
          "year": 2041,
          "rate": 10.0,
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
    {
      "age": 61,
      "value": [
        {
          "year": 2042,
          "rate": 10.0,
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
    }
  ],
  "annuityPayoutFreq": "yearly",
  "dateOfBirth": "01-01-1981",
  "retirementAge": 61,
  "drawdownAge": 66,
  "planningAge": 82,
  "maritalStatus": "married",
  "currentSalary": 350000.0,
  "spousalSalary": 250000.0,
  "jobTenure": 31,
  "totalAccountBalance": 1260000.0,
  "balanceProportion": 0.1,
  "periodicContributions": 8750.0,
  "contributionFreq": "monthly",
  "currentAnnuityBalance": 35000,
  "retirementIncomeGoal": 25000,
  "drawdownAgeSS": 64,
  "incomeFromSS": 10000,
  "outsideAssets": 210000.0,
  "otherIncome": 25000,
  "otherIncomeFreq": "yearly",
  "currentPortfolioId": null,
  "calculateRetirementIncomeGoal": true,
  "riskProfile": "aggressive",
  "includeAnnuities": true,
  "currentDate": "01-01-2024",
  "currAge": 43
}
```

