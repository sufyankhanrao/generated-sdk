
# Signed Deals Summary Month Details

Signed deals summary by grouped by month.

## Structure

`SignedDealsSummaryMonthDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_month` | `str` | Optional | Process month.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `signed_deal_count` | `int` | Optional | Number of signed deals for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `signed_deal_ratio` | `float` | Optional | Signed deal or closed deal ratio for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `estimated_annual_revenue_amount` | `float` | Optional | Estimated annual revenue amount for the month.<br><br>**Constraints**: `<= 9999999999999.99` |
| `estimated_annual_volume_amount` | `float` | Optional | Estimated annual volume amount for the month.<br><br>**Constraints**: `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "processMonth": "2021-01",
  "signedDealCount": 368,
  "signedDealRatio": 6.8,
  "estimatedAnnualRevenueAmount": 5492.0,
  "estimatedAnnualVolumeAmount": 60000.0
}
```

