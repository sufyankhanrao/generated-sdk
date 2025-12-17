
# Signed Deals Summary Month Response

Search results for signed deals summary.

## Structure

`SignedDealsSummaryMonthResponse`

## Inherits From

[`SignedDealsCommonSummaryResponse`](../../doc/models/signed-deals-common-summary-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[SignedDealsSummaryMonthDetails]`](../../doc/models/signed-deals-summary-month-details.md) | Optional | Signed deals summary grouped by month. |

## Example (as JSON)

```json
{
  "totalSignedDealCount": 150,
  "totalEstimatedAnnualRevenueAmount": 9999999998999.99,
  "totalEstimatedAnnualVolumeAmount": 9999999998999.99,
  "signedDealRatio": 168.38,
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

