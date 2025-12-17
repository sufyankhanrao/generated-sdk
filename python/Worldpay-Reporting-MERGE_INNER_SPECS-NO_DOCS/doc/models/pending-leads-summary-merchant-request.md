
# Pending Leads Summary Merchant Request

Request message to get pending leads summary by merchant.

## Structure

`PendingLeadsSummaryMerchantRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level. |
| `month_range` | [`MonthRange1`](../../doc/models/month-range-1.md) | Required | Month range for which data is to be retrieved. Maximum month range supported is 13 months. |
| `sort_results_by` | [`SortPartnerCardNetwork`](../../doc/models/sort-partner-card-network.md) | Optional | Sorting order for the search results of pending leads summary. |

## Example (as JSON)

```json
{
  "independentSalesChannelCodes": [
    "MTBCON",
    "MTBNEW"
  ],
  "monthRange": {
    "startMonth": "2022-01",
    "endMonth": "2022-06"
  },
  "sortResultsBy": {
    "fieldName": "PROCESS_REVENUE",
    "orderBy": "ASC"
  }
}
```

