
# Goe to Analysis Report

*This model accepts additional fields of type Any.*

## Structure

`GoeToAnalysisReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `advisor_discretion_report` | `Any` | Required | Recommended Portfolio and corresponding probability.  <br>                    In case where current portfolio is not null, it provides the following:  <br>                    1. Probability of attaining goal (using the current portfolio sent as an input and a constant portfolio path) – Monte Carlo simulations  <br>                    2. Current Goal Probability (dynamic asset allocation by GOE) and the recommended portfolio <br>                    In case the current portfolio is null, the current goal probability is displayed (using dynamic asset allocation by GOE and not assuming a constant portfolio path) along with the recommended portfolio. |
| `bankruptcy_msg` | `str` | Required | Message flagging an expected bankruptcy (goal running out of money) in any year. <br>                    Note:  <br>                    If ‘NA’, bankruptcy is unlikely to happen during the goal tenure. <br>                    In bankruptcy cases, response would be of the format:  <br>                    There is more than 75% probability of going bankrupt after year 10 |
| `current_goal_probability` | `float` | Required | GOE’s estimated probability to achieve the goal target wealth. <br>                    Note:  <br>                    To be displayed as 63% (rounded with no decimals) |
| `expected_taxes_for_current_year` | [`GoeToExpectedTaxesForCurrentYear2`](../../doc/models/goe-to-expected-taxes-for-current-year-2.md) | Required | Details of the taxes as received from LifeYield. <br>                    Note: <br>                    The taxes pertain to accounts that are under GOE’s discretion & are computed, in this dictionary, only for current financial year. |
| `is_goal_realistic` | `bool` | Required | To understand if the goal probability is more                     than 35% (This is a configurable field). <br>                    Note: If ‘false’, goal is                     unrealistic. |
| `loss_threshold` | `float` | Required | - |
| `meet_goal_priority` | `bool` | Required | Checks if goal probability is more than the                     target probability corresponding to the goal                     priority – Target probabilities for all goal                     priorities (Need, Want, Wish and Dream) are                     set in the GOE config. <br>                     Note: If ‘true’, goal                     probability achieves the                     target probability.                     If ‘false’, goal probability                     falls short of the target                     probability. |
| `meet_loss_priority` | `bool` | Required | Checks if loss probability is at least 95%                     (target can be set in the GOE config). <br>                    Note:  <br>                    If true, estimated                     loss probability meets                     the target loss                     probability. |
| `one_time_top_up` | `Any` | Required | Recommendations based on available accounts. Two objectives of recommendations: <br>                    1.	Ensure the probability of withdrawal from the taxable account is greater than the priority of the goal (pre-59.5Y). This is applicable if the user has taxable account with TDA / Roth account. <br>                    2.	Add money to the retirement accounts if the current threshold for contributing to retirement accounts is not met. |
| `p_delta_current_goal_probability` | `float` | Required | Estimated goal probability considering the                     swing constraint. Since this is a simulation,                     the output might differ slightly on each                     simulation run. |
| `p_delta_current_loss_threshold_probability` | `float` | Required | - |
| `proposed_trades_current_year` | [`ProposedTradesCurrentYearInfo2`](../../doc/models/proposed-trades-current-year-info-2.md) | Required | Details of trade as of today i.e., current date & end of the year |
| `recommended_portfolio_id` | `int` | Required | GOE’s current recommended portfolio index. <br>                    Note: Can be between 1                     to 16. Also subject to                     investor’s risk profile: for                     example, conservative                     investors have access to                    1-8 portfolios while                     Aggressive investors have                     access to 1-16. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "advisorDiscretionReport": {
    "16": 0.6504
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
  "lossThreshold": 57.66,
  "meetGoalPriority": false,
  "meetLossPriority": false,
  "oneTimeTopUp": {
    "T": 135040
  },
  "pDeltaCurrentGoalProbability": 0.6372,
  "pDeltaCurrentLossThresholdProbability": 133.8,
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
              "phase": "phase2",
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
              "phase": "phase2",
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
  "recommendedPortfolioId": 16,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

