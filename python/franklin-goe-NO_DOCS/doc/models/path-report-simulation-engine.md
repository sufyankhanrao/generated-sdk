
# Path Report Simulation Engine

*This model accepts additional fields of type Any.*

## Structure

`PathReportSimulationEngine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `early_withdrawal_penalty` | `float` | Required | 10% penalty if the expected path has an early                     withdrawal incidence from the Roth account. |
| `ending_wealth` | `Any` | Required | Estimate of the ending wealth as of end of the                     year after accounting for all the infusions and                     withdrawals in the year. <br>                     Three estimates:                    “expected”, “optimistic”, and “pessimistic.” |
| `expected_tax_amount` | `float` | Required | Expected Taxes due to following: <br>                     - Withdrawals <br>                     - Social Security <br>                     - RMD |
| `goal_amount` | `float` | Required | Post-tax withdrawal as requested by the                     participant for a given period |
| `period` | `int` | Required | Represents a financial year.<br>                    Note:<br>                    Period 1: represents the current financial year. |
| `portfolio_id` | `int` | Required | Portfolio number for a given period |
| `rmd_amount` | [`List[RmdAmount]`](../../doc/models/rmd-amount.md) | Required | Represents the RMD amount for a given period                    (if applicable). <br>                     This is based on the projected balance of the                     TDA account as of 31st December of the                     preceding year. |
| `social_security_amount` | [`List[RmdAmount]`](../../doc/models/rmd-amount.md) | Required | Social security amounts to be received for each                     participant in a given period. <br>                     This amount is not an optimized amount, but                     an amount derived based on the custom age                     specified by the participant. <br>                     Please note that the social security amount is                     pre-tax |
| `withdrawal_amount` | `Any` | Required | Three elements are part of the dictionary: <br>                     “taxableAccount”: withdrawal from taxable  account. <br>                     “tdaAmount”: withdrawal from TDA account. <br>                     “rothAccount”: withdrawal from Roth account. <br>                    The withdrawal sequencing is following: <br>                     Social Security (if any), RMD (if any), Taxable account, TDA account, and Roth Account                    In case of taxable accounts, due to the unpredictable nature of capital gains, <br>                     the desired withdrawal is taxed, but the taxes are not sourced. However, for TDA accounts, due to the                     predictability of the taxes - the withdrawals are escalated for taxes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "earlyWithdrawalPenalty": 0.0,
  "endingWealth": {
    "expected": 221160,
    "optimistic": 240110,
    "pessimistic": 204004
  },
  "expectedTaxAmount": 0.0,
  "goalAmount": 86.58,
  "period": 2,
  "portfolioId": 16,
  "rmdAmount": [
    {
      "amount": 127.8,
      "memberId": "memberId8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "socialSecurityAmount": [
    {
      "amount": 87.4,
      "memberId": "memberId8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "withdrawalAmount": {
    "D": 0,
    "F": 0,
    "T": 0
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

