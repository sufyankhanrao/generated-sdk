
# Analysis Report 1

This section gives details of the GOE run for the original plan.

*This model accepts additional fields of type Any.*

## Structure

`AnalysisReport1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `advisor_discretion_report` | `Any` | Required | Recommended Portfolio and corresponding probability. |
| `bankruptcy_msg` | `str` | Required | Message flagging an expected bankruptcy (goal running out of money) in any year.<br>                    Note: <br>                    If ‘NA’, bankruptcy is unlikely to happen during the goal tenure.<br>                    In bankruptcy cases, response would be of the format: <br>                    There is more than 75% probability of going bankrupt after year 10 |
| `current_goal_probability` | `float` | Required | GOE’s estimated probability to achieve the goal target wealth.<br>                    Note: <br>                    To be displayed as 63% (rounded with no decimals) |
| `expected_taxes_for_current_year` | [`ExpectedTaxesForCurrentYear2`](../../doc/models/expected-taxes-for-current-year-2.md) | Required | Details of the taxes as received from LifeYield.<br>                    Note:<br>                    The taxes pertain to accounts that are under GOE’s discretion & are computed, in this dictionary, only for current financial year. |
| `is_goal_realistic` | `bool` | Required | To understand if the goal probability is more                     than 35% (This is a configurable field).<br>                    Note: <br>                    If ‘false’, goal is unrealistic. |
| `loss_threshold` | `float` | Required | - |
| `meet_goal_priority` | `bool` | Required | Checks if goal probability is more than the                     target probability corresponding to the goal                     priority – Target probabilities for all goal                     priorities (Need, Want, Wish and Dream) are                     set in the GOE config.  <br>                    Note: <br>                    If ‘true’, goal                     probability achieves the                     target probability. <br>                    If ‘false’, goal probability                     falls short of the target                     probability. |
| `meet_loss_priority` | `bool` | Required | Checks if loss probability is at least 95%                     (target can be set in the GOE config).<br>                    Note: <br>                    If true, estimated                     loss probability meets                     the target loss                     probability. |
| `one_time_top_up` | `Any` | Required | Recommendations based on available accounts. <br>                     Note: <br>                     The retirement accounts for MVP are of the variety “401k”. <br>                     The max contribution amount recommendation is based solely on accounts available to GOE. |
| `p_delta_current_goal_probability` | `float` | Required | Estimated goal probability considering the                     swing constraint. Since this is a simulation,                     the output might differ slightly on each                     simulation run. |
| `p_delta_current_loss_threshold_probability` | `float` | Required | - |
| `proposed_trades_current_year` | [`ProposedTradesCurrentYear2`](../../doc/models/proposed-trades-current-year-2.md) | Required | Details of trade as of today i.e., current date & end of the year |
| `recommended_portfolio_id` | `int` | Required | GOE’s current recommended portfolio index. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "advisorDiscretionReport": {
    "10": 0.68
  },
  "bankruptcyMsg": "NA",
  "currentGoalProbability": 0.6504,
  "expectedTaxesForCurrentYear": {
    "federalOrdinaryIncomeTaxLiability": 0.0,
    "federalQualifiedDividendsTaxLiability": 0.0,
    "federalCapitalGainsRebalancingLiability": 0.0,
    "federalCapitalGainsWithdrawalLiability": 0.0,
    "federalEarlyDistributionPenalty": 0.15,
    "federalTaxDueToRMD": 0.15,
    "federalTaxDueToSocialSecurity": 0.15,
    "federalTotalTaxLiability": 0.15,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "isGoalRealistic": false,
  "lossThreshold": 247.08,
  "meetGoalPriority": false,
  "meetLossPriority": false,
  "oneTimeTopUp": {
    "D": 0,
    "F": 30000,
    "T": 121043
  },
  "pDeltaCurrentGoalProbability": 0.6372,
  "pDeltaCurrentLossThresholdProbability": 67.22,
  "proposedTradesCurrentYear": {
    "endOfCurrentYear": {
      "accounts": [
        {
          "accountID": "T",
          "trades": [
            {
              "direction": "S",
              "symbol": "CASH",
              "cusip": "cusip4",
              "quantity": 29178.0,
              "amount": 10748.399065,
              "tradeType": null,
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
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "today": {
      "accounts": [
        {
          "accountID": "T",
          "trades": [
            {
              "direction": "S",
              "symbol": "CASH",
              "cusip": "cusip4",
              "quantity": 29178.0,
              "amount": 10748.399065,
              "tradeType": null,
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
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "recommendedPortfolioId": 10,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

