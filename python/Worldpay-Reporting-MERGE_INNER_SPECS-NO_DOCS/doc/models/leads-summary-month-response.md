
# Leads Summary Month Response

Leads summary for the selected month range.

## Structure

`LeadsSummaryMonthResponse`

## Inherits From

[`LeadsSummaryMonthCommonResponse`](../../doc/models/leads-summary-month-common-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[LeadsSummaryMonthSummaryDetails]`](../../doc/models/leads-summary-month-summary-details.md) | Optional | Leads summary grouped by month. |

## Example (as JSON)

```json
{
  "totalLeadCount": 6,
  "totalActionableLeadCount": 22,
  "totalSignedDealCount": 10,
  "totalSignedDealAverageAmount": 9999999998999.99,
  "totalSignedDealPercentage": 236.98,
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

