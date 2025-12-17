
# Leads Summary Month Summary Details

Leads summary grouped by month.

## Structure

`LeadsSummaryMonthSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_month` | `str` | Optional | Process month.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `lead_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the processed month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `actionable_lead_count` | `int` | Optional | Number of leads that need to be acted upon for progressing it to next stage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `signed_deal_count` | `int` | Optional | Number of signed deals or closed deals for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `signed_deal_average_amount` | `float` | Optional | Signed deals average amount for the month.<br><br>**Constraints**: `<= 9999999999999.99` |
| `signed_deal_percentage` | `float` | Optional | Signed deals or closed deals percentage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `activated_accounts` | `int` | Optional | Number of accounts activated for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "processMonth": "2021-04",
  "leadCount": 7300,
  "actionableLeadCount": 5000,
  "signedDealCount": 315,
  "signedDealAverageAmount": 579.0,
  "signedDealPercentage": 4.29,
  "activatedAccounts": 171
}
```

