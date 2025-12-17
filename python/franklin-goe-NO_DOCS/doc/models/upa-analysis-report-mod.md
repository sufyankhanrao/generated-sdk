
# Upa Analysis Report Mod

*This model accepts additional fields of type Any.*

## Structure

`UpaAnalysisReportMod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_goal_probability` | `float` | Required | GOE’s estimated probability to achieve the goal target wealth<br><br>**Constraints**: `>= 0` |
| `current_loss_threshold_probability` | `float` | Required | GOE’s estimated probability to remain above the loss threshold amount by the end of the goal tenure. |
| `p_delta_current_goal_probability` | `float` | Required | Estimated goal probability considering the swing constraint. Since this is a simulation,             the output might differ slightly on each simulation run. |
| `p_delta_current_loss_threshold_probability` | `float` | Required | Similar to above, this is the loss threshold probability considering swing constraint.                     Since this is a simulation, the output might differ slightly on each simulation run. |
| `recommended_portfolio_id` | `int` | Required | GOE’s current recommended portfolio index. |
| `meet_goal_priority` | `bool` | Required | Checks if goal probability is more than the target probability corresponding to the goal             priority – Target probabilities for all goal priorities (Need, Want, Wish and Dream) are set in the GOE config. |
| `is_goal_realistic` | `bool` | Required | To understand if the goal probability is more than 35% (This is a configurable field). |
| `meet_loss_priority` | `bool` | Required | Checks if loss probability is at least 95% (target can be set in the GOE config). |
| `one_time_top_up` | `float` | Required | Suggested one-time top-up amount that aims to improve the goal probability to meet the target goal probability. |
| `cashflow_recommendation` | [`CashflowRecommendation1`](../../doc/models/cashflow-recommendation-1.md) | Required | Cashflow recommendation is at the plan level.Note: -               Empty in case plan meets the target probability. |
| `bankruptcy_msg` | `str` | Required | Message flagging an expected bankruptcy (goal running out of money) in any year. |
| `advisor_discretion_report` | `Dict[str, float]` | Required | Recommended Portfolio and corresponding probability. In case where current portfolio is not null,                    it provides the following:<br> 1. Probability of attaining goal                     (using the current portfolio sent as an input and a constant portfolio path)                          – Monte Carlo simulations.<br>2. Current Goal Probability (dynamic asset allocation by GOE)                              and the recommended portfolio.<br>In case the current portfolio is null,                                 the current goal probability is displayed (using dynamic asset allocation                                      by GOE and not assuming a constant portfolio path) along with                                         the recommended portfolio |
| `loss_threshold` | `int` | Required | Loss threshold value – the wealth amount that the investor does not want to end up below             at the end of the goal tenure. The GOE algo calculates the loss threshold if not provided. |
| `goals_response` | [`List[UpaGoalResponse]`](../../doc/models/upa-goal-response.md) | Required | - |
| `comments` | `str` | Required | Comment would describe the modifications or % change in goal amount made to original goal amounts to meet the target goal probability. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "currentGoalProbability": 10000.0,
  "currentLossThresholdProbability": 9.76,
  "pDeltaCurrentGoalProbability": 0.3288,
  "pDeltaCurrentLossThresholdProbability": 0.4175,
  "recommendedPortfolioId": 6,
  "meetGoalPriority": false,
  "isGoalRealistic": false,
  "meetLossPriority": false,
  "oneTimeTopUp": 38859.0,
  "cashflowRecommendation": {
    "cashFlowMonthly": null,
    "cashFlowYearly": 2503.0,
    "startDate": "01-01-2022",
    "endDate": "01-01-2036",
    "newPlanProb": 0.85,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "bankruptcyMsg": "NA",
  "advisorDiscretionReport": {
    "6": 0.3344
  },
  "lossThreshold": 11500,
  "goalsResponse": [
    {
      "goalID": "Goal1",
      "goalAmt": [
        179.05
      ],
      "startDate": "01-01-2021",
      "endDate": "01-01-2031",
      "priority": "Dream",
      "modifiedGoalAmt": [
        72.68,
        72.69
      ],
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "comments": "To meet all goals optimally as per their assigned priorities Goal1 has been reduced by 100.0%, Goal2 has been reduced by 50.0% of its original value. The allocated portfolio has an 94.316% probability of meeting the modified goals",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

