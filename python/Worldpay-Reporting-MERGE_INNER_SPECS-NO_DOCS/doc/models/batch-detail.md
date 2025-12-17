
# Batch Detail

## Structure

`BatchDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_number` | `int` | Optional | Batch number is a unique identifier assigned to a group of transaction that were handled together as a single unit. |
| `batch_status` | [`BatchStatus2Enum`](../../doc/models/batch-status-2-enum.md) | Optional | The status of the batch -open, closed, error |
| `open_date` | `str` | Optional | Batch opened date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `released_date` | `str` | Optional | The date batch was released<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `expected_settlement_date` | `str` | Optional | Refers to the anticipated date when a financial transaction is expected to be completed and funds are transferred between parties.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "batchNumber": 111002,
  "batchStatus": "CLOSED",
  "openDate": "2021-12-06",
  "releasedDate": "2021-12-21",
  "expectedSettlementDate": "2021-08-21"
}
```

