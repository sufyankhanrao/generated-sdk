
# Transaction Lists

Refers to transaction information

## Structure

`TransactionLists`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_amount` | `float` | Optional | Amount involved in a financial transaction.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `transaction_type` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Type of transaction |
| `transaction_date_time` | `str` | Optional | Indicates date time of transaction<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `transaction_status` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status code,short and long descriptions. |
| `network_transaction_id` | `str` | Optional | Network reference ID  (VISA/AMEX/DISCOVER etc. transaction  identifier)<br><br>**Constraints**: *Maximum Length*: `15` |
| `banknet_reference_number` | `str` | Optional | Banknet data for VISA and MC transactions<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `card_number` | `str` | Optional | Card Number<br><br>**Constraints**: *Minimum Length*: `16`, *Maximum Length*: `16` |
| `card_type` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Refers to the category or classification of a payment card based on the issuing network. |
| `retrieval_reference_number` | `int` | Optional | A unique identifier used to reference and locate the batch of transactions. |
| `sequence_number` | `str` | Optional | Sequence Number (system trace Audit number or STAN)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |

## Example (as JSON)

```json
{
  "transactionAmount": 2654.0,
  "transactionDateTime": "07/19/2021 16:41:31",
  "transactionStatus": {
    "code": "2",
    "shortDescription": "DENIED",
    "longDescription": "DENIED"
  },
  "networkTransactionId": "1236547823543",
  "cardType": {
    "code": "C",
    "shortDescription": "Credit",
    "longDescription": "Credit"
  },
  "retrievalReferenceNumber": 9154359,
  "transactionType": {
    "code": "code2",
    "shortDescription": "shortDescription0",
    "longDescription": "longDescription4"
  }
}
```

