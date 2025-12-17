
# Scenario

*This model accepts additional fields of type Any.*

## Structure

`Scenario`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_investment` | `float` | Required | The initial amount of funds placed by the investor at the beginning of the goal tenure. |
| `target_wealth` | `float` | Required | The amount of funds at the end of the goal tenure. |
| `goal_tenure` | `int` | Required | The duration, in years, between the initial investment being placed in the portfolio and the investor's last withdrawal from the portfolio (at which point the funds in the portfolio are zero). |
| `irr` | `float` | Required | The internal rate of return of the portfolio that is required to attain the target wealth at the end of the goal tenure, given the cash flows resulting from the investor's infusions. |
| `infusions` | `float` | Required | The cash flows into/out of the portfolio from the investor at the chosen (monthly or yearly) interval. The investor will place these funds starting one interval period (i.e. one month/year) after the initial investment is placed into the fund until one interval period before the final withdrawal takes place (i.e. before the end of the goal tenure). For example, an investor with a five-year goal tenure and yearly infusions of $1000 will contribute $1000 at years 2, 3, and 4 of the goal tenure. |
| `goal_probability` | `int` | Required | The probability that the target wealth will be achieved at the end of the goal tenure. |
| `portfolio_id` | `int` | Required | The ID of the portfolio that corresponds to this scenario. |
| `goal_priority` | `int` | Required | Defines the importance of achieving the goal for the investor. The importance increases in the following order: Desire > Dream > Wish > Want > Need. The investor can select multiple importances. Selecting more importances will result in more scenarios being returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "initialInvestment": 100000.0,
  "targetWealth": 200000.2,
  "goalTenure": 8,
  "irr": 2.9,
  "infusions": 24000.3,
  "goalProbability": 220,
  "portfolioId": 2,
  "goalPriority": 158,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

