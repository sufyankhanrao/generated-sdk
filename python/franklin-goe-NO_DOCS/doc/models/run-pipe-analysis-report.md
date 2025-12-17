
# Run Pipe Analysis Report

*This model accepts additional fields of type Any.*

## Structure

`RunPipeAnalysisReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_goal_probability` | `float` | Required | GOE’s estimated probability to achieve the goal target wealth. This is rounded to 4 decimal places.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `current_loss_threshold_probability` | `float` | Required | GOE’s estimated probability to remain above the loss threshold amount by the end of the goal tenure. <br>             This is rounded to 4 decimal places.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `p_delta_current_goal_probability` | `float` | Required | This probability refers to the goal probability simulation results. This parameter uses a random variable, <br>         and each run returns a slightly different result. This is rounded to 4 decimal places.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `p_delta_current_loss_threshold_probability` | `float` | Required | Like the p-delta goal probability, this is only used for simulation purposes. It simulates the goal's loss threshold probability.         This is rounded to 4 decimal places.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `recommended_portfolio_id` | `int` | Required | GOE’s current recommended portfolio index. <br>                     Note: Portfolio chosen from the list of all available portfolios to the goal.<br><br>**Constraints**: `>= 1` |
| `meet_goal_priority` | `bool` | Required | Checks if goal probability is more than the target probability corresponding to <br>         the goal priority – Target probabilities for all goal priorities (Need, Want, Wish and Dream) are set in the GOE config. <br>         Note: If ‘true’, goal probability achieves the target probability – goal probability to be shown on the front end. <br>         If ‘false’, goal probability falls short of the target probability –goal probability to be shown along with infusion and tenure recommendations |
| `is_goal_realistic` | `bool` | Required | To understand if the goal can be met with a reasonable probability (set by the ‘unrealistic’ goal probability value in the GOE config).<br>         If current goal probability < desired target goal probability (defined by the goal priority), the goal is termed unrealistic <br>         Note: Flag will be set to False if the current goal probability is less than the probability threshold for realistic goal for all cases irrespective. <br>         If ‘false’, goal is unrealistic - need to alert the user on the front end with a message such as ‘Goal is not realistic, please try reducing your target <br>         goal amount or increasing your initial investment’ |
| `meet_loss_priority` | `bool` | Required | Checks if loss probability is more than the target loss probability (target set in the GOE config) <br>         Note: If true, estimated loss probability meets the target loss probability |
| `one_time_top_up` | `float` | Required | Suggested one-time top-up amount that aims to improve the goal probability to meet the target goal probability.<br>                     This is rounded to the nearest integer.<br><br>**Constraints**: `>= 0` |
| `yearly_top_up_accumulation` | `float` | Required | Suggested recurring yearly top-up amount that aims to improve the goal probability to meet the target goal probability. <br> This would be returned with a value if the infusionType is annual. This is rounded to the nearest integer. This would be 0 if infusionType is monthly. <br> Note: Zero in cases where meet goal priority = ‘true’; Non-zero otherwise.<br><br>**Constraints**: `>= 0` |
| `monthly_top_up_accumulation` | `float` | Required | Suggested recurring monthly top-up amount during the accumulation period that aims to improve <br>              the goal probability to meet the target goal probability. This would be returned only if the infusionType is monthly. <br>             This is rounded to the nearest integer. <br>             Note: Zero in cases where meet goal priority = ‘true’; Non-zero otherwise.<br><br>**Constraints**: `>= 0` |
| `yearly_top_up_decumulation` | `float` | Required | Suggested recurring yearly decumulation amount that aims to improve the goal probability to meet the target goal probability. <br>            This would be returned only if the infusionType is annual. This is rounded to the nearest integer. |
| `monthly_top_up_decumulation` | `float` | Required | Suggested recurring monthly top-up decumulation amount that aims to improve the goal probability to meet the target <br>        goal probability, this value would be populated only in cases of decumulation of withdrawal scenario. This would be returned only <br>        if the infusionType is monthly. This is rounded to the nearest integer. |
| `recommended_tenure` | `str` | Required | For scenarios with goal probability less than 50%: <br>                     • If original tenure between 1 - 8 years –extended/reduced tenure 2 years to 4 years <br>                     • If original tenure between 9 – 14 years – extended/reduced tenure 4 years to 8 years <br>                     • If original tenure greater than equal to 15 years –extended/reduced tenure 5 years to 10 years <br>         For scenarios with goal probability greater than or equal to 50%, extended/reduced tenure = 2 years to 4 years for all cases.<br>         The algorithm recommends standard tenure increments/decrements based on the tenure input and the goal probability (calculated using current and end date).<br>         Cases where tenure recommendation isn’t valid/required will show the recommendation as NA. <br>        For retirement cases, where there is accumulation followed by decumulation, the extension is based on years to retirement and not on original tenure |
| `bankruptcy_msg` | `str` | Required | Message flagging an expected bankruptcy (goal running out of money) in any year.<br>         The algorithm recommends standard tenure increments/decrements based on the tenure input and the goal probability (calculated using current and end date). <br>        Note: If ‘NA’, bankruptcy is unlikely to happen during the goal tenure.In bankruptcy cases, response would be similar to <br>        ‘Bankruptcy is likely to happen in year 1’. |
| `recommended_final_wealth_at_75` | `float` | Optional | This is an optional parameter .If the target wealth were to be reduced by 25% of the difference between the target and the current wealth.<br>         Applicable for non-retirement scenarios with tenures less than or equal to 30 years. This is rounded to the nearest integer <br>        Note: To be denoted as a rounded number with a currency suffix ($980,384) on the front end. |
| `recommended_prob_at_75` | `float` | Optional | Goal probability corresponding to ‘recommended final wealth at 75%’ above.<br>         Applicable for non-retirement scenarios with tenures less than or equal to 30 years. This is rounded to the nearest integer.<br>        Note: To be denoted as a rounded number with no decimals, on the front end.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `recommended_final_wealth_at_50` | `float` | Optional | This is an optional parameter .If the target wealth were to be reduced by 50% of the difference between the target and the current wealth.<br>         Applicable for non-retirement scenarios with tenures less than or equal to 30 years. This is rounded to the nearest integer <br>        Note: To be denoted as a rounded number with a currency suffix ($960,769) on the front end. |
| `recommended_prob_at_50` | `float` | Optional | Goal probability corresponding to ‘recommended final wealth at 50%’ above.<br>         Applicable for non-retirement scenarios with tenures less than or equal to 30 years. This is rounded to the nearest integer.<br>        Note: To be denoted as a rounded number with no decimals, on the front end.<br><br>**Constraints**: `>= 0`, `<= 0.99` |
| `advisor_discretion_report` | `Dict[str, float]` | Required | Recommended Portfolio and corresponding probability.<br>         In case where current portfolio is not null, it provides the following:<br>        1. Probability of attaining goal (using the current portfolio sent as an input and a constant portfolio path) – Monte Carlo simulations<br>         2. 2. Current Goal Probability (dynamic asset allocation by GOE) and the recommended portfolio <br>         In case the current portfolio is null, the current goal probability is displayed (using dynamic asset allocation by GOE <br>        and not assuming a constant portfolio path) along with the recommended portfolio. |
| `message` | `str` | Required | Captures any message from the API after it is done processing the request. |
| `loss_threshold` | `int` | Required | Loss threshold value – the wealth amount that the investor does not want to end up below at the end of the goal tenure.<br>         If the input parameter ‘lossThreshold’ is not passed or value is ‘null’, this parameter is calculated by GOE.<br>         If the input parameter ‘lossThreshold’ is a number value, GOE will consider this as the loss threshold.<br><br>**Constraints**: `>= 0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "currentGoalProbability": 0.99,
  "currentLossThresholdProbability": 0.99,
  "pDeltaCurrentGoalProbability": 0.99,
  "pDeltaCurrentLossThresholdProbability": 0.99,
  "recommendedPortfolioId": 182,
  "meetGoalPriority": false,
  "isGoalRealistic": false,
  "meetLossPriority": false,
  "oneTimeTopUp": 96.82,
  "yearlyTopUpAccumulation": 70.54,
  "monthlyTopUpAccumulation": 169.34,
  "yearlyTopUpDecumulation": 87.46,
  "monthlyTopUpDecumulation": 2.64,
  "recommendedTenure": "recommendedTenure4",
  "bankruptcyMsg": "bankruptcyMsg2",
  "recommendedFinalWealthAt75": 189.54,
  "recommendedProbAt75": 0.99,
  "recommendedFinalWealthAt50": 56.46,
  "recommendedProbAt50": 0.99,
  "advisorDiscretionReport": {
    "key0": 155.0,
    "key1": 155.01,
    "key2": 155.02
  },
  "message": "message0",
  "lossThreshold": 78,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

