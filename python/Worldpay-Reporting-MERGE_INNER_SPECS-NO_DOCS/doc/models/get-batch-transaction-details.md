
# Get Batch Transaction Details

Full details on an individual transaction within the batch

## Structure

`GetBatchTransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_info` | [`BatchInfo1`](../../doc/models/batch-info-1.md) | Optional | Authorization Batch Details |
| `transaction_info` | [`TransactionDetail`](../../doc/models/transaction-detail.md) | Optional | Refers to the transaction information |

## Example (as JSON)

```json
{
  "batchInfo": {
    "batchNumber": 22,
    "batchStatus": "CLOSED",
    "openDate": "openDate2",
    "releasedDate": "releasedDate6",
    "expectedSettlementDate": "expectedSettlementDate4"
  },
  "transactionInfo": {
    "retrievalReferenceNumber": "retrievalReferenceNumber8",
    "transactionAmount": 187.26,
    "transactionType": {
      "code": "code2",
      "shortDescription": "shortDescription0",
      "longDescription": "longDescription4"
    },
    "transactionTimeStamp": "transactionTimeStamp8",
    "transactionStatus": null
  }
}
```

