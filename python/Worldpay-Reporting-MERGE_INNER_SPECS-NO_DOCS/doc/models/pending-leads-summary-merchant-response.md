
# Pending Leads Summary Merchant Response

Pending leads summary for selected month range.

## Structure

`PendingLeadsSummaryMerchantResponse`

## Inherits From

[`PendingLeadsMerchantCommonSummaryResponse`](../../doc/models/pending-leads-merchant-common-summary-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[PendingLeadsSummaryMerchantDetails]`](../../doc/models/pending-leads-summary-merchant-details.md) | Optional | Pending leads summary grouped by merchant. |

## Example (as JSON)

```json
{
  "totalEstimatedRevenueAmount": 153.48,
  "totalMerchantCount": 144,
  "totalLeadCount": 54,
  "summaries": [
    {
      "merchantName": "merchantName4",
      "referringBanker": "referringBanker6",
      "branchName": "branchName8",
      "closedDate": "closedDate8",
      "estimatedRevenueAmount": 9999999998999.99
    }
  ]
}
```

