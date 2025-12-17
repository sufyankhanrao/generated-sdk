
# Batch Info 1

Authorization Batch Details

## Structure

`BatchInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_number` | `int` | Optional | Batch number is a unique identifier assigned to a group of transaction that were handled together as a single unit. |
| `batch_status` | [`BatchStatus2Enum`](../../doc/models/batch-status-2-enum.md) | Optional | The status of the batch -open, closed, error |
| `open_date` | `str` | Optional | Batch opened date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `released_date` | `str` | Optional | The date batch was released<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `expected_settlement_date` | `str` | Optional | Refers to the anticipated date when a financial transaction is expected to be completed and funds are transferred between parties.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `terminal_number` | `int` | Optional | The Unique identification number for every terminal of a merchant |
| `iias_certified` | `bool` | Optional | Inventory Information Approval System |
| `terminal_type` | `str` | Optional | Refer to device used in payments to process card transactions and authorize payments.<br><br>**Constraints**: *Maximum Length*: `2` |
| `terminal_application` | `str` | Optional | Software for managing transactions, payments, or data in a specific location or device like a point-of-sale system.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `register_number` | `str` | Optional | Unique id of point-of-sale terminals to identify and track transactions securely and accurately<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "batchNumber": 111002,
  "batchStatus": "CLOSED",
  "openDate": "2021-12-06",
  "releasedDate": "2021-12-21",
  "expectedSettlementDate": "2021-08-21",
  "terminalNumber": 5,
  "iiasCertified": false,
  "terminalType": "03",
  "terminalApplication": "ABC Software Inc",
  "registerNumber": "1111"
}
```

