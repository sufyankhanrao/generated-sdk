
# Bank Card Rejects Search Request

## Structure

`BankCardRejectsSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | This is used to retrieve the numbers or marks used to indicate the sequence of pages. |
| `hierarchy` | [`Entity`](../../doc/models/entity.md) | Required | This object holds the entity and its hierarchy level |
| `sort_results_by` | [`Sortbankcarddetails`](../../doc/models/sortbankcarddetails.md) | Optional | A field in a record that is used in determining the final sorted sequence of the records |
| `date_range` | [`SearchAuthTransactionsRequestRealTimeTransactionDateRange`](../../doc/models/search-auth-transactions-request-real-time-transaction-date-range.md) | Required | Refers to number of dates that includes a particular start and end date and all dates in between specific periods of time. |
| `batch_number` | `int` | Optional | Settlement transactions are processed in batches and each batch file must have a unique sequential identifier within the file called Batch Number of length 6 bytes.<br><br>**Constraints**: `>= 100000`, `<= 999999` |
| `batch_hold_status` | `str` | Optional | Indicates batch hold status of the transaction<br><br>**Constraints**: *Maximum Length*: `256` |
| `batch_amount` | `float` | Optional | Total Batch Amount of all the transactions that are part of the batch file<br><br>**Constraints**: `>= 1000000000`, `<= 9999999999` |
| `sale_amount` | `float` | Optional | Indicates sale amount of the transaction<br><br>**Constraints**: `>= 1000000000`, `<= 9999999999` |
| `return_amount` | `float` | Optional | Indicates return amount of the transaction<br><br>**Constraints**: `>= 1000000000`, `<= 9999999999` |

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
  "batchHoldStatus": "RELEASE BATCH ",
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  },
  "batchNumber": 100000,
  "batchAmount": 1000000000.0
}
```

