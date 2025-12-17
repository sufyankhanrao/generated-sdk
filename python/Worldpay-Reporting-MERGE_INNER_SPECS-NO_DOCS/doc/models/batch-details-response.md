
# Batch Details Response

## Structure

`BatchDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Used for pagination. |
| `merchant_id` | `str` | Optional | A Merchant ID (card acceptor identification code) is a unique identifier assigned to a merchant by a payment processor or bank.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `merchant_name` | `str` | Optional | Refers to the name of a business or registered name of the company or entity operating the business.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `bank_number` | `int` | Optional | the acquiring institution identification code (Bank ID) |
| `batch_info` | [`List[BatchInfo]`](../../doc/models/batch-info.md) | Optional | Authorization batch details |

## Example (as JSON)

```json
{
  "merchantId": "1000910955961234",
  "merchantName": "PRODDEV 122218",
  "bankNumber": 1444,
  "pagination": {
    "pageNumber": 8999,
    "pageSize": 1000,
    "totalRowCount": 1000,
    "totalReturnedCount": 1000
  },
  "batchInfo": [
    {
      "terminalNumber": 120,
      "terminalSettlementType": "MANUAL",
      "batchNumber": 22,
      "batchStatus": "CLOSED",
      "batchType": "AUTH"
    },
    {
      "terminalNumber": 120,
      "terminalSettlementType": "MANUAL",
      "batchNumber": 22,
      "batchStatus": "CLOSED",
      "batchType": "AUTH"
    },
    {
      "terminalNumber": 120,
      "terminalSettlementType": "MANUAL",
      "batchNumber": 22,
      "batchStatus": "CLOSED",
      "batchType": "AUTH"
    }
  ]
}
```

