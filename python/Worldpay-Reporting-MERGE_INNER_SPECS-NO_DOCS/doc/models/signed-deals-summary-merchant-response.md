
# Signed Deals Summary Merchant Response

Signed deals summary for selected month range.

## Structure

`SignedDealsSummaryMerchantResponse`

## Inherits From

[`SignedDealsMerchantCommonSummaryResponse`](../../doc/models/signed-deals-merchant-common-summary-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[SignedDealsSummaryMerchantDetails]`](../../doc/models/signed-deals-summary-merchant-details.md) | Optional | Signed deals summary grouped by merchant. |

## Example (as JSON)

```json
{
  "totalSignedMerchantCount": 148,
  "totalEstimatedAnnualRevenueAmount": 9999999998999.99,
  "totalEstimatedAnnualVolumeAmount": 9999999998999.99,
  "signedDealRatio": 245.24,
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

