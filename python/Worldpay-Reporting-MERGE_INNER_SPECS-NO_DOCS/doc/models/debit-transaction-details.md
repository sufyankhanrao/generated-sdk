
# Debit Transaction Details

Debit transaction details.

## Structure

`DebitTransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposits or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `transaction_process_date` | `str` | Optional | Date when transaction processed<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `transaction_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates the type of transaction that occurred when funds are transfered between a merchant and a bank, including its short and long descriptions. |
| `denial_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Denial Code indicates that payment can't be processed, due to various reason. |
| `entry_mode` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `cashback_amount` | `float` | Optional | Amount refunds to the cardholder's account, a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `batch_number` | `str` | Optional | Fields refers to the process for the settlement in batches.<br><br>**Constraints**: *Maximum Length*: `6` |
| `settled` | `str` | Optional | Possible Values 'YES' or 'NO'<br><br>**Constraints**: *Maximum Length*: `3` |
| `card_holder_bank_acro` | `str` | Optional | Refers to card holder bank acro<br><br>**Constraints**: *Maximum Length*: `4` |
| `network_id` | `str` | Optional | Indicates network id<br><br>**Constraints**: *Maximum Length*: `4` |
| `network_group` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | A network group is a collection on hosts,gateways,networks, or other groups.Groups can be used to facilitate and simplify network management. |
| `voucher_number` | `str` | Optional | Refers the unique reference number associated with a voucher.<br><br>**Constraints**: *Maximum Length*: `10` |
| `transaction_emv` | `bool` | Optional | possible values True or False |
| `offline_emv` | `bool` | Optional | possible values True or False |
| `pos_condition_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the POS Condition Code for transactions. |
| `terminal_emv` | `bool` | Optional | possible values True or False |
| `authorization_communication_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization communication details. |
| `customer_identifier` | `str` | Optional | The unique identifier of the purchaser associated with the transaction.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_order_identifier` | `str` | Optional | This field indicates the ecom merchant order identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `campaign` | `str` | Optional | This field indicates the ecom campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `affiliate` | `str` | Optional | This field indicates the ecom affiliate.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_grouping_identifier` | `str` | Optional | This field indicates the ecom merchant grouping identifier<br><br>**Constraints**: *Maximum Length*: `25` |
| `report_group` | `str` | Optional | This field indicates the ecom report group<br><br>**Constraints**: *Maximum Length*: `25` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `sequence_number` | `str` | Optional | Sequence number.<br><br>**Constraints**: *Maximum Length*: `6` |
| `force_post` | `bool` | Optional | possible values True or False |
| `has_adjustment_records` | `str` | Optional | Indicates whether the transaction has any adjustments.<br><br>**Constraints**: *Maximum Length*: `12` |
| `terminal_id` | `str` | Optional | Id of terminal<br><br>**Constraints**: *Maximum Length*: `15` |
| `pos_register_number` | `str` | Optional | Refers to registered POS Number<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "transactionId": "186354016598",
  "transactionDateTime": "07/19/2016 16:41:31",
  "transactionProcessDate": "2022-01-01",
  "transactionType": {
    "code": "11",
    "shortDescription": "POS DB CRD RET",
    "longDescription": "POS DEBIT CARD RETURN"
  },
  "denialCode": {
    "code": "0",
    "shortDescription": "TRANSACTION AUTHORIZED",
    "longDescription": "TRANSACTION AUTHORIZED"
  },
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "authorizationAmount": 100,
  "cashbackAmount": 100,
  "batchNumber": "000101",
  "settled": "YES",
  "cardHolderBankAcro": "MAE1",
  "networkId": "STAR",
  "networkGroup": {
    "code": "6",
    "shortDescription": "Other",
    "longDescription": "OTHER"
  },
  "voucherNumber": "484426",
  "transactionEMV": true,
  "offlineEMV": true,
  "posConditionCode": {
    "code": "59",
    "shortDescription": "E-Commerce",
    "longDescription": "E-COMMERCE"
  },
  "terminalEMV": true,
  "authorizationCommunicationType": {
    "code": "0",
    "shortDescription": "STANDARD RAFT",
    "longDescription": "STANDARD RAFT"
  },
  "customerIdentifier": "98765",
  "merchantOrderIdentifier": "A453",
  "campaign": "D453",
  "affiliate": "G123",
  "merchantGroupingIdentifier": "S673",
  "reportGroup": "E874",
  "chargeId": "G453",
  "sequenceNumber": "823040",
  "forcePost": true,
  "hasAdjustmentRecords": "Not Adjusted",
  "terminalId": "0000000000",
  "posRegisterNumber": "7546"
}
```

