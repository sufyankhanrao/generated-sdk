
# Terminal Batch Detail

## Structure

`TerminalBatchDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_number` | `int` | Optional | Batch number is a unique identifier assigned to a group of transaction that were handled together as a single unit. |
| `batch_status` | [`BatchStatus2Enum`](../../doc/models/batch-status-2-enum.md) | Optional | The status of the batch -open, closed, error |
| `batch_type` | [`BatchTypeEnum`](../../doc/models/batch-type-enum.md) | Optional | Type of batch - AUTH, UPLOAD. <br>AUTH - Authorization batches captured by processing system (host). <br>UPLOAD - Batch uploaded by merchant from the terminal. |
| `open_date` | `str` | Optional | Batch opened date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `released_date` | `str` | Optional | The date batch was released<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `next_release_time` | `str` | Optional | Next release time of batch<br><br>**Constraints**: *Maximum Length*: `19` |
| `adjustment_indicator` | `bool` | Optional | identifies if batch contains adjustment |
| `fcs_number` | `str` | Optional | FCS number( also referred as FNS number) is the unique number assigned by Food and Nutrition Service to merchants.<br> It is required to process EBT transactions.<br><br>**Constraints**: *Maximum Length*: `10` |
| `e_2_ee_indicator` | `bool` | Optional | Refers to indicator of end to end encrypted. <br> Possible Value True and False. |
| `terminal_number` | `int` | Optional | The Unique identification number for every terminal of a merchant |
| `terminal_application` | `str` | Optional | The payment software application installed on the Terminal<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `terminal_settlement_type` | [`TerminalSettlementTypeEnum`](../../doc/models/terminal-settlement-type-enum.md) | Optional | The type of settlement for a terminal. <br> Possible values are - "UPLOAD","AUTO_CLOSE","MANUAL" |
| `terminal_active_indicator` | `bool` | Optional | identifies if terminal is active or not |
| `total_sales_transaction_amount` | `float` | Optional | Total value of sales during a specific financial transaction or period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_sales_transaction_count` | `int` | Optional | Total Sales Count<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `total_returns_transaction_amount` | `float` | Optional | Total Returned Amount<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_returns_transaction_count` | `int` | Optional | Total return Count<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `total_transactions_amount` | `float` | Optional | Refers to the amount left over after all deductions are made. <br> Total Transactions Amount = Sales Amount - Returns Amount<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_transactions_count` | `int` | Optional | Total Count of the transactions <br> Total Transactions Count = Sales Count + Returns Count<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `processor_error_message` | `str` | Optional | Error Message from processing Platform – RAFT<br><br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "batchNumber": 111002,
  "batchStatus": "CLOSED",
  "batchType": "AUTH",
  "openDate": "2021-12-06",
  "releasedDate": "2021-12-21",
  "nextReleaseTime": "08/21/2017 13:49:36",
  "adjustmentIndicator": false,
  "fcsNumber": "***6682",
  "e2EEIndicator": false,
  "terminalNumber": 5,
  "terminalApplication": "ABC Software Inc",
  "terminalSettlementType": "UPLOAD",
  "terminalActiveIndicator": true,
  "totalSalesTransactionAmount": 2654,
  "totalSalesTransactionCount": 18,
  "totalReturnsTransactionAmount": 2654,
  "totalReturnsTransactionCount": 12,
  "totalTransactionsAmount": 39115.21,
  "totalTransactionsCount": 7845126,
  "processorErrorMessage": "DENIED HEADER RECORD"
}
```

