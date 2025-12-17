
# Settlement Rejects Search Request

## Structure

`SettlementRejectsSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | This is used to retrieve the numbers or marks used to indicate the sequence of pages |
| `hierarchy` | [`Entity`](../../doc/models/entity.md) | Required | This object holds the entity and its hierarchy level |
| `sort_results_by` | [`Sortsettlementfiledetails`](../../doc/models/sortsettlementfiledetails.md) | Optional | A field in a record that is used in determining the final sorted sequence of the records |
| `date_range` | [`SearchAuthTransactionsRequestRealTimeTransactionDateRange`](../../doc/models/search-auth-transactions-request-real-time-transaction-date-range.md) | Required | Refers to number of dates that includes a particular start and end date and all dates in between specific periods of time. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "INDEPENDENT_SALES_ORGANIZATION",
    "values": [
      "4445000860700",
      "4445000860702"
    ],
    "chainCode": "OA1234"
  },
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "RESUBMIT_DATE",
    "orderBy": "ASC"
  }
}
```

