
# Leads Count Disqualified Request

Request message to get count of disqualified leads.

## Structure

`LeadsCountDisqualifiedRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level. |
| `month_range` | [`MonthRange1`](../../doc/models/month-range-1.md) | Required | Month range for which data is to be retrieved. Maximum month range supported is 13 months. |
| `sort_results_by` | [`SortLeadsCountDisqualified`](../../doc/models/sort-leads-count-disqualified.md) | Optional | Sorting order for the search results of disqualified leads. |

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
    "fieldName": "DISQUALIFICATION_REASON",
    "orderBy": "ASC"
  }
}
```

