
# Leads Count Category Request

Request message to get leads count by category.

## Structure

`LeadsCountCategoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `independent_sales_channel_codes` | `List[str]` | Required | Independent sales channel value provides a secondary entity under the independent sales organization hierarchy level. |
| `category` | [`List[CategoryEnum]`](../../doc/models/category-enum.md) | Optional | Refers to the status of the lead.<br><br>**Constraints**: *Maximum Length*: `26` |
| `month_range` | [`MonthRange1`](../../doc/models/month-range-1.md) | Required | Month range for which data is to be retrieved. Maximum month range supported is 13 months. |
| `sort_results_by` | [`SortLeadsCountCategory`](../../doc/models/sort-leads-count-category.md) | Optional | Sorting order for the search results of leads category. |

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
  "category": [
    "IN_PROGRESS_LEADS",
    "APPROVED_BUT_NOT_ACTIVATED"
  ],
  "sortResultsBy": {
    "fieldName": "CATEGORY",
    "orderBy": "ASC"
  }
}
```

