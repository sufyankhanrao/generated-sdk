
# Get Batch Details Response

Detailed response for a batch

## Structure

`GetBatchDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | Current page number returned.<br><br>**Constraints**: `>= 0`, `<= 9999` |
| `page_size` | `int` | Optional | Total number of records returned per page.<br><br>**Constraints**: `>= 0`, `<= 2000` |
| `total_row_count` | `int` | Optional | Total number of records meeting the search criteria.<br><br>**Constraints**: `>= 0`, `<= 2000` |
| `total_returned_count` | `int` | Optional | Total number of records returned in the response.<br><br>**Constraints**: `>= 0`, `<= 2000` |
| `merchant_name` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `merchant_id` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `bank_number` | `int` | Optional | the acquiring institution identification code (Bank ID) |
| `batch_info` | [`TerminalBatchDetail`](../../doc/models/terminal-batch-detail.md) | Optional | Authorization Batch Details |
| `transaction_list` | [`List[TransactionLists]`](../../doc/models/transaction-lists.md) | Optional | Refers to transaction information |

## Example (as JSON)

```json
{
  "pageNumber": 1,
  "pageSize": 50,
  "totalRowCount": 85,
  "totalReturnedCount": 25,
  "merchantName": "PRODDEV 122218",
  "merchantId": "1000910955961234",
  "bankNumber": 1444
}
```

