
# Deposit Search Request

Deposit search request details

## Structure

`DepositSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | pagination details |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | The sort results by field is used in request to establish the sort order for the data to be returned in ascending or descending order. |
| `hierarchy` | [`Entity2`](../../doc/models/entity-2.md) | Required | - |
| `settlement_category` | [`SettlementCategoryEnum`](../../doc/models/settlement-category-enum.md) | Optional | settlement category<br><br>**Constraints**: *Maximum Length*: `15` |
| `date_range` | [`DateRange`](../../doc/models/date-range.md) | Required | - |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445000860700",
      "4445000860702"
    ],
    "chainCode": "OA1234"
  },
  "settlementCategory": "FEES",
  "dateRange": {
    "fromDate": "2019-10-27",
    "toDate": "2019-11-27"
  },
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  }
}
```

