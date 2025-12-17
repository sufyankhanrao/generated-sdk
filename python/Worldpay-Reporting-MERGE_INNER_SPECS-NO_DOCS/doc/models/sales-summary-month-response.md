
# Sales Summary Month Response

Sales summary for the selected month range.

## Structure

`SalesSummaryMonthResponse`

## Inherits From

[`SalesSummaryMonthCommonResponse`](../../doc/models/sales-summary-month-common-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[SalesSummaryMonthSummaryDetails]`](../../doc/models/sales-summary-month-summary-details.md) | Optional | Sales summary grouped by month. |

## Example (as JSON)

```json
{
  "totalLeadCount": 110,
  "totalDisqualifiedLeadCount": 178,
  "totalActionableLeadCount": 174,
  "totalActionableLeadPercentage": 157.56,
  "totalSignedDealCount": 114,
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

