
# Batch Details Search Request

Request body for searching the batch

## Structure

`BatchDetailsSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_type` | [`DateTypeEnum`](../../doc/models/date-type-enum.md) | Required | Type of date |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | Specifying start and end dates for transactions. |
| `merchant_id` | `str` | Required | Merchant Number (also referred as MID) , sometimes this is combination of bank ID & alternate merchant number<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `batch_number` | `int` | Optional | Batch number is a unique identifier assigned to a group of transaction that were handled together as a single unit. |
| `batch_status` | [`BatchStatusEnum`](../../doc/models/batch-status-enum.md) | Optional | The status of the batch - open, closed, error |
| `terminal_number` | `int` | Optional | The Unique identification number for every terminal of a merchant |
| `pagination` | [`PaginationType`](../../doc/models/pagination-type.md) | Optional | Used for pagination. |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | Sort results by option for authorization batches. |

## Example (as JSON)

```json
{
  "dateType": "RELEASED_DATE",
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "merchantId": "1000910955961234",
  "batchNumber": 111002,
  "batchStatus": "CLOSED",
  "terminalNumber": 5,
  "pagination": {
    "pageNumber": 221.22,
    "pageSize": 216.38
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  }
}
```

