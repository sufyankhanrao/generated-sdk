
# Signed Deals Summary Merchant Details

Signed deals summary grouped by merchant.

## Structure

`SignedDealsSummaryMerchantDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Name of the signed deal merchant.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `branch_name` | `str` | Optional | Branch name associated with the merchant.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `estimated_annual_revenue_amount` | `float` | Optional | Estimated annual revenue amount of a specific merchant.<br><br>**Constraints**: `<= 9999999999999.99` |
| `estimated_annual_volume_amount` | `float` | Optional | Estimated annual volume of a specific merchant.<br><br>**Constraints**: `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "merchantName": "MANNA FARM AND GARDEN INC",
  "branchName": "NH445 | Hampton Falls",
  "estimatedAnnualRevenueAmount": 24923.0,
  "estimatedAnnualVolumeAmount": 6000.0
}
```

