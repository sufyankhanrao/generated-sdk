
# Terminal Batch Details

## Structure

`TerminalBatchDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_number` | `int` | Optional | Batch number is a unique identifier assigned to a group of transaction that were handled together as a single unit. |
| `batch_status` | [`BatchStatusEnum`](../../doc/models/batch-status-enum.md) | Optional | The status of the batch - open, closed, error |
| `batch_type` | [`BatchTypeEnum`](../../doc/models/batch-type-enum.md) | Optional | Type of batch - AUTH, UPLOAD. <br>AUTH - Authorization batches captured by processing system (host). <br>UPLOAD - Batch uploaded by merchant from the terminal. |
| `open_date` | `str` | Optional | Date when a batch of transactions is initiated for processing and settlement.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `released_date` | `str` | Optional | Date when a group of transactions is processed and released for settlement.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `total_transactions_amount` | `float` | Optional | Total transactions amount refers to the sum of transactions that have taken place within a time period<br><br>**Constraints**: `>= 0`, `<= 1000000000000000` |
| `total_transactions_count` | `int` | Optional | Total transactions count refers to the complete number of transactions that have taken place within a time period<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `processor_error_message` | `str` | Optional | Error Message from processing Platform – RAFT<br><br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "batchNumber": 111002,
  "batchStatus": "CLOSED",
  "batchType": "AUTH",
  "openDate": "2021-12-06",
  "releasedDate": "2021-12-21",
  "totalTransactionsAmount": 895623.02,
  "totalTransactionsCount": 7845126,
  "processorErrorMessage": "DENIED HEADER RECORD"
}
```

