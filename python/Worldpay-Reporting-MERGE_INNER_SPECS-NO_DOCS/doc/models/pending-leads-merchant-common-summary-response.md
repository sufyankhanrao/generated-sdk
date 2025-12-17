
# Pending Leads Merchant Common Summary Response

Pending leads summary for selected month range.

## Structure

`PendingLeadsMerchantCommonSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_estimated_revenue_amount` | `float` | Optional | Total estiamted revenue amount of the pending leads.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_merchant_count` | `int` | Optional | Total number of merchants in pipeline for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_lead_count` | `int` | Optional | Total number of leads generated for the independent sales channel(s) for the selected range of month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalEstimatedRevenueAmount": 1564263.0,
  "totalMerchantCount": 125,
  "totalLeadCount": 125,
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

