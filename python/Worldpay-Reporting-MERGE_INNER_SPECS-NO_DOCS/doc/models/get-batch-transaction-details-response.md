
# Get Batch Transaction Details Response

## Structure

`GetBatchTransactionDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `merchant_id` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `bank_number` | `int` | Optional | the acquiring institution identification code (Bank ID) |
| `merchant_category_code` | `int` | Optional | Merchant category code is a four-digit number assigned to businesses by payment card networks. It helps identify the nature of merchant's business and the industry in which they operate.<br><br>**Constraints**: `<= 4` |
| `batch_info` | [`BatchInfo1`](../../doc/models/batch-info-1.md) | Optional | Authorization Batch Details |
| `transaction_info` | [`TransactionDetail`](../../doc/models/transaction-detail.md) | Optional | Refers to the transaction information |

## Example (as JSON)

```json
{
  "merchantName": "PRODDEV 122218",
  "merchantId": "1000910955961234",
  "bankNumber": 1444,
  "merchantCategoryCode": 4,
  "batchInfo": {
    "batchNumber": 22,
    "batchStatus": "CLOSED",
    "openDate": "openDate2",
    "releasedDate": "releasedDate6",
    "expectedSettlementDate": "expectedSettlementDate4"
  }
}
```

