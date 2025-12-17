
# Goal Discovery Input Model

*This model accepts additional fields of type Any.*

## Structure

`GoalDiscoveryInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_type` | [`GoalType`](../../doc/models/goal-type.md) | Required | Defines the investor's goal for a portfolio. Only portfolios that correspond to the investor's goal are returned. The investor can only select one of 'retirement' or 'wealth'. |
| `risk_profile` | [`RiskProfile1`](../../doc/models/risk-profile-1.md) | Required | Defines the risk the investor is willing to take; the returned scenarios are chosen/tailored based on this risk. Risk profiles represent increasing risk in the following order: conservative > conservatively moderate > moderate > moderately aggressive > aggressive. The investor may only choose one risk profile. |
| `initial_investment` | [`InitialInvestment2`](../../doc/models/initial-investment-2.md) | Required | Defines a range of possible initial investments the investor will make. The `min`/`max` amounts represent the minimum and maximum amounts of funds respectively that the investor will place into the portfolio at the beginning of the goal tenure. |
| `goal_priority` | [`List[GoalDiscoveryGoalPriorityAttribute]`](../../doc/models/goal-discovery-goal-priority-attribute.md) | Required | Defines the importance of achieving the goal for the investor. The importance increases in the following order: Desire > Dream > Wish > Want > Need. The investor can select multiple importances. Selecting more importances will result in more scenarios being returned. |
| `infusion_type` | [`InfusionType1`](../../doc/models/infusion-type-1.md) | Required | Defines the duration between each infusion the investor makes. If set to 'yearly', the investor makes an infusion every year on the same day of the year. Setting this to 'monthly' means the infusion is made every month, on the same day of the month. Idiosyncrasies in the calendar, such as 28/29/30/31 day months and leap years are already considered. |
| `infusions` | [`Infusions2`](../../doc/models/infusions-2.md) | Required | Defines the amount of funds that the investor is willing to place at a chosen (monthly/yearly) interval. The investor will place these funds starting one interval period (i.e. one month/year) after the initial investment is placed into the fund until one interval period before the final withdrawal takes place (i.e. before the end of the goal tenure). For example, an investor with a five-year goal tenure and yearly infusions of $1000 will contribute $1000 at years 2, 3, and 4 of the goal tenure. The `min`/`max` values represent the minimum and maximum infusion amounts respectively that the investor is willing to make into the portfolio. |
| `goal_tenure` | [`GoalTenure2`](../../doc/models/goal-tenure-2.md) | Required | Defines the duration, in years, between the initial investment being placed in the portfolio and the investor's last withdrawal (at which point the funds in the portfolio are zero). The investor may make infusions during this time into/out of the portfolio. The `min`/`max` values represent the minimum and maximum goal tenures that the investor is considering. The `max` value must be more or equal to the `min` value, and the `min` value must be positive. |
| `target_wealth` | [`TargetWealth2`](../../doc/models/target-wealth-2.md) | Required | Defines the amount that the investor is willing to set as their target wealth in their portfolio at the end of the (maximum length) goal tenure. The `min`/`max` values represent the minimum and maximum target wealth values respectively. The `max` value must be more than or equal to the `min` value. |
| `page_size` | `int` | Required | Defines the number of scenarios to be returned on one page. Each scenario is returned as a JSON object. Typically, a larger page size lowers the time taken to receive all the results, but increases the time to receive each page of data. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalType": "retirement",
  "riskProfile": "moderate",
  "initialInvestment": {
    "min": 100000.0,
    "max": 77.92,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "goalPriority": [
    "need"
  ],
  "infusionType": "yearly",
  "infusions": {
    "min": 102,
    "max": 20,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "goalTenure": {
    "min": 120,
    "max": 38,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "targetWealth": {
    "min": 100000.0,
    "max": 35.54,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "pageSize": 12000,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

