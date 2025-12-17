
# Signed Deals Merchant Common Summary Response

Signed deals summary for selected month range.

## Structure

`SignedDealsMerchantCommonSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_signed_merchant_count` | `int` | Optional | Total number of signed merchants for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_estimated_annual_revenue_amount` | `float` | Optional | Total estimated annual revenue amount for selected month range.<br><br>**Constraints**: `<= 9999999999999.99` |
| `total_estimated_annual_volume_amount` | `float` | Optional | Total estimated annual volume amount for selected month range.<br><br>**Constraints**: `<= 9999999999999.99` |
| `signed_deal_ratio` | `float` | Optional | Signed deal or closed deal ratio for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "totalSignedMerchantCount": 3,
  "totalEstimatedAnnualRevenueAmount": 90265.0,
  "totalEstimatedAnnualVolumeAmount": 1100000.0,
  "signedDealRatio": 12.5,
  "summaries": [
    {
      "merchantName": "merchantName4",
      "branchName": "branchName8",
      "estimatedAnnualRevenueAmount": 9999999998999.99,
      "estimatedAnnualVolumeAmount": 9999999998999.99
    }
  ]
}
```

