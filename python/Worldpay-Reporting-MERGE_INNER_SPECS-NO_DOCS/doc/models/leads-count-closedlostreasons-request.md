
# Leads Count Closedlostreasons Request

Request message to get count of lost leads.

## Structure

`LeadsCountClosedlostreasonsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level. |
| `month_range` | [`MonthRange1`](../../doc/models/month-range-1.md) | Required | Month range for which data is to be retrieved. Maximum month range supported is 13 months. |
| `sort_results_by` | [`SortsLeadsCountClosedLostReasons`](../../doc/models/sorts-leads-count-closed-lost-reasons.md) | Optional | Sorting order for search results of closed lost reasons. |

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
    "fieldName": "CLOSED_LOST_REASON",
    "orderBy": "ASC"
  }
}
```

