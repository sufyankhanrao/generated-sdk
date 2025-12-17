
# Signed Deals Common Summary Response

Signed deals summary for selected month range.

## Structure

`SignedDealsCommonSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_signed_deal_count` | `int` | Optional | Total number of singed deals for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_estimated_annual_revenue_amount` | `float` | Optional | Total estimated annual revenue amount.<br><br>**Constraints**: `<= 9999999999999.99` |
| `total_estimated_annual_volume_amount` | `float` | Optional | Total estimated annual volume amount.<br><br>**Constraints**: `<= 9999999999999.99` |
| `signed_deal_ratio` | `float` | Optional | Signed deal or closed deal ratio for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "totalSignedDealCount": 368,
  "totalEstimatedAnnualRevenueAmount": 90546.0,
  "totalEstimatedAnnualVolumeAmount": 10001560.0,
  "signedDealRatio": 9.8,
  "summaries": [
    {
      "processMonth": "processMonth8",
      "signedDealCount": 68,
      "signedDealRatio": 46.24,
      "estimatedAnnualRevenueAmount": 9999999998999.99,
      "estimatedAnnualVolumeAmount": 9999999998999.99
    }
  ]
}
```

