
# Settlement Rej Real Time Transaction

## Structure

`SettlementRejRealTimeTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `processed_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `transaction_date` | `str` | Optional | Refers to the date and time when the bank has settled/rejected the transaction (deposits or withdraws funds).<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `resubmit_date` | `str` | Optional | Indicates resubmission date  of the transaction<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `account_number` | `str` | Optional | Account number or Card number involved in the rejected transaction<br><br>**Constraints**: *Maximum Length*: `19` |
| `dda_number` | `str` | Optional | Demand deposit account is a type of bank account that offers access to money.<br><br>**Constraints**: *Maximum Length*: `16` |
| `amount` | `float` | Optional | Rejected transaction amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `rejection_reason` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Reject Reason code states why the transaction was rejected as per the predefined set of reasons in MDB Database and Mainframes. |
| `hierarchy` | [`MerchantHierarchyDetail`](../../doc/models/merchant-hierarchy-detail.md) | Optional | Merchant hierarchy information |

## Example (as JSON)

```json
{
  "processedDate": "2016-07-19",
  "transactionDate": "2022-07-19",
  "resubmitDate": "2022-07-21",
  "accountNumber": "4445123456789012",
  "ddaNumber": "4020016689",
  "amount": 5000.89,
  "rejectionReason": {
    "code": "D",
    "shortDescription": "BAD MCC CODE",
    "longDescription": "INVALID MCC CODE"
  }
}
```

