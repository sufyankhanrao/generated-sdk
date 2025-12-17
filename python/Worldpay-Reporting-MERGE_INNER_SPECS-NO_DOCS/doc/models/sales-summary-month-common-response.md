
# Sales Summary Month Common Response

Sales summary for the selected month range.

## Structure

`SalesSummaryMonthCommonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_lead_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_disqualified_lead_count` | `int` | Optional | Total number of disqualified leads for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_actionable_lead_count` | `int` | Optional | Total number of leads that need to be acted upon for progressing it to next stage.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_actionable_lead_percentage` | `float` | Optional | Total actionable leads percentage for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_signed_deal_count` | `int` | Optional | Total number of signed deals for the independent sales channel(s) for the selected range of month. This is also known as 'closed deals'.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `signed_deal_ratio` | `float` | Optional | Signed deal ratio or closed ratio for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_signed_deal_percentage` | `float` | Optional | Total signed deals percentage for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_signed_deal_average_amount` | `float` | Optional | Total signed deals average amount for the selected month range.<br><br>**Constraints**: `<= 9999999999999.99` |
| `total_signed_deal_estimated_revenue_amount` | `float` | Optional | Total estimated revenue amount of signed deals.<br><br>**Constraints**: `<= 9999999999999.99` |
| `total_activated_accounts` | `int` | Optional | Total number of accounts activated for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_activation_percentage` | `float` | Optional | Total activation percentage for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `lead_per_business_day_count` | `float` | Optional | Number of referrals per business day.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `average_days_to_activate` | `float` | Optional | Average days to activate the accounts.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `pipeline_revenue_next_90_days_amount` | `float` | Optional | Pipeline revenue in next 90 days for the selected month range.<br><br>**Constraints**: `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "totalLeadCount": 94145,
  "totalDisqualifiedLeadCount": 57,
  "totalActionableLeadCount": 47329,
  "totalActionableLeadPercentage": 79.2,
  "totalSignedDealCount": 5492,
  "signedDealRatio": 9.2,
  "totalSignedDealPercentage": 35.52,
  "totalSignedDealAverageAmount": 62.37,
  "totalSignedDealEstimatedRevenueAmount": 530,
  "totalActivatedAccounts": 3866,
  "totalActivationPercentage": 89.3,
  "leadPerBusinessDayCount": 0.7,
  "averageDaysToActivate": 515,
  "pipelineRevenueNext90DaysAmount": 55000000,
  "summaries": [
    {
      "processMonth": "processMonth8",
      "leadCount": 68,
      "disqualifiedLeadCount": 136,
      "actionableLeadCount": 246,
      "actionableLeadPercentage": 240.36
    }
  ]
}
```

