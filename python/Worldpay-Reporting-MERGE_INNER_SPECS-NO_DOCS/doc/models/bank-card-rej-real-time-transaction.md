
# Bank Card Rej Real Time Transaction

## Structure

`BankCardRejRealTimeTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `batch_number` | `int` | Optional | Settlement transactions are processed in batches and each batch file must have a unique sequential identifier within the file called Batch Number of length 6 bytes.<br><br>**Constraints**: `>= 100000`, `<= 999999` |
| `batch_amount` | `float` | Optional | Total Batch Amount of all the transactions that are part of the batch file<br><br>**Constraints**: `>= 1000000000`, `<= 9999999999` |
| `sale_count` | `int` | Optional | Indicates sale count of the transaction<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `sale_amount` | `float` | Optional | Indicates sale amount of the transaction<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `return_count` | `int` | Optional | Indicates return count of the transaction<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `return_amount` | `float` | Optional | Indicates return amount of the transaction<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `rejection_reason` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Reject Reason code states why the transaction was rejected as per the predefined set of reasons in MDB Database and Mainframes. |
| `batch_hold_status` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Status of the batch file. |
| `hierarchy` | [`MerchantHierarchy`](../../doc/models/merchant-hierarchy.md) | Optional | This object holds the entity and its hierarchy level such as<br> SalesOrganization/Sales Channel max limit 1 Entity<br> National, SuperChain, Partner and PartnerGroup with maximum limit of 10 Entities<br> Chain, Division, Store and Merchant with maximum limit of 2,000 Entities. |

## Example (as JSON)

```json
{
  "processDate": "2021-07-19",
  "saleCount": 7,
  "saleAmount": 37551.08,
  "returnCount": 2,
  "returnAmount": 113.08,
  "rejectionReason": {
    "code": "103",
    "shortDescription": "FORCEPOST",
    "longDescription": "FORCEPOST"
  },
  "batchHoldStatus": {
    "code": "5",
    "shortDescription": "RELEASE BATCH",
    "longDescription": "RELEASE BATCH"
  },
  "batchNumber": 100000,
  "batchAmount": 1000000000.0
}
```

