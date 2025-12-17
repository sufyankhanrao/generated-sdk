
# Sales Summary Month Summary Details

Sales summary grouped by month.

## Structure

`SalesSummaryMonthSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_month` | `str` | Optional | Process month.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `lead_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the processed month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `disqualified_lead_count` | `int` | Optional | Number of disqualified leads for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `actionable_lead_count` | `int` | Optional | Number of leads that need to be acted upon for progressing it to next stage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `actionable_lead_percentage` | `float` | Optional | Actionable leads percentage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `signed_deal_count` | `int` | Optional | Number of signed deals or closed deals for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `signed_deal_ratio` | `float` | Optional | Signed deals ratio lose ratio for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `signed_deal_percentage` | `float` | Optional | Signed deals or closed deals percentage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `signed_deal_average_amount` | `float` | Optional | Signed deals average amount for the month.<br><br>**Constraints**: `<= 9999999999999.99` |
| `signed_deal_estimated_revenue_amount` | `float` | Optional | Estimated revenue amount from the signed deals for the month.<br><br>**Constraints**: `<= 9999999999999.99` |
| `activated_accounts` | `int` | Optional | Number of accounts activated for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `activation_percentage` | `float` | Optional | Activation percentage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `average_days_to_activate` | `float` | Optional | Average number of days from approval date to activation date.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "processMonth": "2021-04",
  "leadCount": 7300,
  "disqualifiedLeadCount": 57,
  "actionableLeadCount": 5000,
  "actionableLeadPercentage": 68.3,
  "signedDealCount": 315,
  "signedDealRatio": 6.3,
  "signedDealPercentage": 4.29,
  "signedDealAverageAmount": 579,
  "signedDealEstimatedRevenueAmount": 863340,
  "activatedAccounts": 171,
  "activationPercentage": 276.2,
  "averageDaysToActivate": 515
}
```

