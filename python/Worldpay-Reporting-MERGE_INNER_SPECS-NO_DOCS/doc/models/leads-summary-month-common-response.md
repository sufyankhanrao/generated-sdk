
# Leads Summary Month Common Response

Leads summary for the selected month range.

## Structure

`LeadsSummaryMonthCommonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_lead_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_actionable_lead_count` | `int` | Optional | Total number of leads that need to be acted upon for progressing it to next stage.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_signed_deal_count` | `int` | Optional | Total number of signed deals for the independent sales channel(s) for the selected range of month. This is also known as 'closed deals'.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_signed_deal_average_amount` | `float` | Optional | Total signed deals average amount for the selected month range.<br><br>**Constraints**: `<= 9999999999999.99` |
| `total_signed_deal_percentage` | `float` | Optional | Total SignedDeals percentage for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_activated_accounts` | `int` | Optional | Total number of accounts activated for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalLeadCount": 94145,
  "totalActionableLeadCount": 47329,
  "totalSignedDealCount": 5503,
  "totalSignedDealAverageAmount": 62.37,
  "totalSignedDealPercentage": 35.52,
  "totalActivatedAccounts": 3866,
  "summaries": [
    {
      "processMonth": "processMonth8",
      "leadCount": 68,
      "actionableLeadCount": 246,
      "signedDealCount": 68,
      "signedDealAverageAmount": 9999999998999.99
    }
  ]
}
```

