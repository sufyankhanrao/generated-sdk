
# Expected Taxes for Current Year 2

Details of the taxes as received from LifeYield.<br>                    Note:<br>                    The taxes pertain to accounts that are under GOE’s discretion & are computed, in this dictionary, only for current financial year.

*This model accepts additional fields of type Any.*

## Structure

`ExpectedTaxesForCurrentYear2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `federal_ordinary_income_tax_liability` | `float` | Required | Income tax for current financial year due to following: <br>                     •	Withdrawals from TDA (if any) <br>                     •	Social Security (if any)<br>                     •	RMD |
| `federal_qualified_dividends_tax_liability` | `float` | Required | Long Term Capital Gains Taxes on dividends received during the current financial year. |
| `federal_capital_gains_rebalancing_liability` | `float` | Required | Capital gains due to rebalancing of the taxable accounts during the financial year. |
| `federal_capital_gains_withdrawal_liability` | `float` | Required | Capital gains due to withdrawal from the taxable accounts during the financial year. |
| `federal_early_distribution_penalty` | `float` | Required | A 10% penalty is levied when tax deferred account is used to meet withdrawals during the current financial year. |
| `federal_tax_due_to_rmd` | `float` | Required | Taxes due to RMD due in the current financial year. |
| `federal_tax_due_to_social_security` | `float` | Required | Ordinary income tax due to social security received in the current financial year. <br>             For MVP, only 85% of social security is taxed at the effective rate |
| `federal_total_tax_liability` | `float` | Required | Total expected taxes due in the current year |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
}
```

