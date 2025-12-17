
# Debit Transaction Details 1

This object provides the details of the debit transactions

## Structure

`DebitTransactionDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `process_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `transaction_date_time` | `str` | Optional | Refers to the date and time when the bank has settled the transaction (deposits or withdraws funds).<br><br>**Constraints**: *Maximum Length*: `19`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}[T]{1}[0-9]{2}:[0-9]{2}:[0-9]{2}` |
| `transaction_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. |
| `authorization_amount` | `float` | Optional | An authorized amount is a sum that a merchant transmits to a credit or debit card processor to make sure the customer has the funds required to make a purchase—the approved amount of money to be charged.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `entry_mode` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `batch_number` | `str` | Optional | Batch Number<br><br>**Constraints**: *Maximum Length*: `256` |
| `sequence_number` | `str` | Optional | Sequence number.<br><br>**Constraints**: *Maximum Length*: `256` |
| `cashback_amount` | `float` | Optional | Amount refunds to the cardholder's account a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `denial_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Denial Code and its description |
| `interchange` | `str` | Optional | Interchange details<br><br>**Constraints**: *Maximum Length*: `256` |
| `interchange_fees` | `str` | Optional | Interchange Fees<br><br>**Constraints**: *Maximum Length*: `255` |
| `customer_identifier` | `str` | Optional | This field indicates the ecom customer identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_order_identifier` | `str` | Optional | This field indicates the ecom merchant order identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `campaign` | `str` | Optional | This field indicates the ecom campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `affiliate` | `str` | Optional | This field indicates the ecom affiliate.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_grouping_identifier` | `str` | Optional | This field indicates the ecom merchant grouping identifier<br><br>**Constraints**: *Maximum Length*: `25` |
| `report_group` | `str` | Optional | This field indicates the ecom report group<br><br>**Constraints**: *Maximum Length*: `25` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `network_id` | `str` | Optional | Indicates network id<br><br>**Constraints**: *Maximum Length*: `5` |
| `network_group` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | A network group is a collection on hosts,gateways,networks, or other groups.Groups can be used to facilitate and simplify network management. |
| `voucher_number` | `str` | Optional | Refers the unique reference number associated with a voucher.<br><br>**Constraints**: *Maximum Length*: `256` |
| `from_account` | `str` | Optional | Refers the type of settlement account<br><br>**Constraints**: *Maximum Length*: `256` |
| `to_account` | `str` | Optional | Refers the type of settlement account<br><br>**Constraints**: *Maximum Length*: `256` |
| `terminal_id` | `int` | Optional | Terminal Id or Terminal Locator is a 15-digit terminal identification number. |
| `pos_register_number` | `str` | Optional | Refers to registered POS Number<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "transactionId": "141710009519",
  "processDate": "2022-07-19",
  "transactionDateTime": "07/19/2016 16:41:31",
  "transactionType": {
    "code": "253",
    "description": "SALE",
    "longDescription": "SALE",
    "shortDescription": "shortDescription0"
  },
  "authorizationAmount": 100.04,
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "batchNumber": "00000000000",
  "sequenceNumber": "823040",
  "cashbackAmount": 9.06,
  "denialCode": {
    "code": "0",
    "shortDescription": "TRANSACTION AUTHORIZED",
    "longDescription": "TRANSACTION AUTHORIZED"
  },
  "interchange": "000145253-VS DEBIT REGULATED",
  "interchangeFees": "DDDDDDDDDCC",
  "customerIdentifier": "G768",
  "merchantOrderIdentifier": "A453",
  "campaign": "D453",
  "affiliate": "G123",
  "merchantGroupingIdentifier": "S673",
  "reportGroup": "E874",
  "chargeId": "G453",
  "networkId": "STAR",
  "networkGroup": {
    "code": "6",
    "shortDescription": "Other",
    "longDescription": "OTHER"
  },
  "voucherNumber": "484426",
  "fromAccount": "AB",
  "toAccount": "DE",
  "terminalId": 90123123,
  "posRegisterNumber": "0010"
}
```

