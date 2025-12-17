
# Transaction Detail

## Structure

`TransactionDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `retrieval_reference_number` | `str` | Optional | A unique identifier used to reference and locate the batch of transactions.<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `transaction_amount` | `float` | Optional | Total transaction amount<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `transaction_type` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Type of transaction |
| `transaction_time_stamp` | `str` | Optional | TimeStamp of transaction<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `transaction_status` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status code,short and long descriptions. |
| `sequence_number` | `str` | Optional | Sequence Number (system trace Audit number or STAN)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `retrieval_reference_number_original` | `str` | Optional | Original Retrival Reference Number<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `retrieval_reference_number_expected` | `str` | Optional | Expected Retrival Reference Number<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `authentication_number` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `payment_type` | `str` | Optional | Payment type refers to the method or mechanism used to transfer funds from one party to another in exchange for goods, services, or debts.<br><br>**Constraints**: *Maximum Length*: `6` |
| `is_authentication_transaction` | `bool` | Optional | Authentication transaction refers to a process where an individual or entity's identity is verified and validated. |
| `aci` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Authorization characteristics indicator is a data element used in financial transactions to indicate specific authorization characteristics associated with a payment request. |
| `ani` | `str` | Optional | Automatic number identification is a technology used in telecommunications to automatically identify and display the phone number of call.<br><br>**Constraints**: *Maximum Length*: `10` |
| `r_pin` | `str` | Optional | Refers to resident permanent indentification number.<br><br>**Constraints**: *Maximum Length*: `10` |
| `cash_back_amount` | `float` | Optional | Amount refunds to the cardholder's account a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `manual_entry` | `bool` | Optional | Indicates if transaction entry  is manual - Y or N |
| `mail_order` | `bool` | Optional | Indicates if the transaction is a mail or telephone order (MOTO) - Y or N |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `bank_net_reference_number` | `str` | Optional | Reference number assigned by network for the transaction<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `bank_net_settle_date` | `str` | Optional | Banknet settlement date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `mc_payment_indicator` | `bool` | Optional | Indicates the type of master card payment being used. |
| `validation` | `str` | Optional | This field indicates the validation code for card networks- visa transactions.<br><br>**Constraints**: *Maximum Length*: `4` |
| `tip_amount` | `float` | Optional | Tip amount refers to an additional payment made by a customer to express gratitude or appreciation for the service received.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `network_id` | `str` | Optional | Network id refers to a unique identifier assigned to a computer network to distinguish it from other networks. It is a numerical or alphanumeric code that serves as the networks.<br><br>**Constraints**: *Maximum Length*: `4` |
| `transaction_result` | `bool` | Optional | Result of the transaction |
| `is_ecomm_transaction` | `bool` | Optional | Indicates if a transaction is ecomm |
| `internal_tps` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Internal Third Party Sender acts as an intermediary for another party to originate ACH transactions. |
| `authorization_comm` | `str` | Optional | Authorization communication refers to the process of transmitting and verifying permission or approvals for certain actions, transactions, or access to specific resources.<br><br>**Constraints**: *Maximum Length*: `4` |
| `line_ip_address` | `str` | Optional | Refers to IP address<br><br>**Constraints**: *Maximum Length*: `15` |
| `merchant_reference_number` | `str` | Optional | Merchant reference number is a unique identifier assigned by a merchant or seller to a specific transaction or purchase made by a customer.<br><br>**Constraints**: *Maximum Length*: `15` |
| `draft_locator_id` | `str` | Optional | Draft locator id refers to a unique identifier assigned to a specific transaction or check draft. Helps to track and identify the individual transaction within the system.<br><br>**Constraints**: *Maximum Length*: `11` |
| `authorizer_response` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Detailed response from authorizer |
| `avs_response` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Address Verification System response code |
| `avs_postal_code` | `str` | Optional | ZIP code/postal code<br><br>**Constraints**: *Maximum Length*: `9` |
| `avs_address` | `str` | Optional | address Verification System - address<br><br>**Constraints**: *Maximum Length*: `20` |
| `fee_code` | `str` | Optional | Fee Code<br><br>**Constraints**: *Maximum Length*: `3` |
| `pos_entry_mode` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Point of sale entry mode |
| `e_2_ee_indicator` | `bool` | Optional | Refers to indicator of end to end encrypted. <br> Possible Value True and False. |
| `cvv_2_presence_indicator` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | This field indicates the presence of card verification value. Possible values CVV2 value not provided, CVV2 value provided / present, CVV2 value illegible, CVV2 value not on card. |
| `cvv_2_response_code` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | This field indicates card verification value, which used for payments. |
| `terminal_emv` | `bool` | Optional | possible values True or False |
| `card_emv` | `bool` | Optional | This field indicates the Card EMV Capability Flag , when it Set the value to Y if the card is EMV capable. Possible Values True or False |
| `is_emv_offline_transaction` | `bool` | Optional | An indication as to whether the EMV transaction was offline |
| `is_emv_transaction` | `bool` | Optional | Transaction in line with the EMV standards |
| `actual_authorization_code` | `str` | Optional | Authorization actual code refers to a unique code provided by a payment processor or financial institution that verifies the successful authorization of a transaction.<br><br>**Constraints**: *Maximum Length*: `6` |
| `network_issuer_code` | `str` | Optional | Refers to a unique identifier assigned to financial institutions, such as banks or credit card issuers, that participate in electronic payment networks.<br><br>**Constraints**: *Maximum Length*: `3` |
| `voucher_number` | `str` | Optional | Refers the unique reference number associated with a voucher.<br><br>**Constraints**: *Maximum Length*: `10` |
| `card_number` | `str` | Optional | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br><br>**Constraints**: *Maximum Length*: `19` |
| `card_type` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | Refers to the category or classification of a payment card based on the issuing network. |
| `token` | `str` | Optional | Tokenization is a substitution for primary account number (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `token_id` | `str` | Optional | Token ID is a host-generated numeric value created during the tokenization process using a token key assigned to a merchant. This value is returned to the POS when tokenization is requested along with the token for utilization.<br><br>**Constraints**: *Maximum Length*: `6` |
| `token_status` | `str` | Optional | Token status<br><br>**Constraints**: *Maximum Length*: `1` |
| `card_expiry_date` | `str` | Optional | Card Expiry date in YYYY-MM format<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "retrievalReferenceNumber": "111118119558",
  "transactionAmount": 2654.0,
  "transactionTimeStamp": "01/09/2023 15:43:59",
  "transactionStatus": {
    "code": "2",
    "shortDescription": "DENIED",
    "longDescription": "DENIED"
  },
  "retrievalReferenceNumberOriginal": "111119154359",
  "retrievalReferenceNumberExpected": "123455432123",
  "authenticationNumber": "73883M",
  "paymentType": "DEBIT",
  "isAuthenticationTransaction": true,
  "ani": "5551234567",
  "rPIN": "ABCDE1234F",
  "cashBackAmount": 100,
  "manualEntry": true,
  "mailOrder": false,
  "bankNetReferenceNumber": "123786453",
  "bankNetSettleDate": "2022-02-28",
  "mcPaymentIndicator": true,
  "validation": "3435",
  "tipAmount": 10,
  "networkId": "STAR",
  "transactionResult": true,
  "isEcommTransaction": true,
  "authorizationComm": "189",
  "lineIPAddress": "10.102.17.21",
  "merchantReferenceNumber": "651238254805765",
  "draftLocatorId": "11222100008",
  "avsPostalCode": "ABCD1234",
  "avsAddress": "111 EDGE AVE",
  "feeCode": "WY",
  "e2EEIndicator": true,
  "terminalEMV": true,
  "cardEMV": true,
  "isEMVOfflineTransaction": false,
  "isEMVTransaction": false,
  "actualAuthorizationCode": "73994M",
  "networkIssuerCode": "VVS",
  "voucherNumber": "888826",
  "cardNumber": "**********0001",
  "cardType": {
    "code": "C",
    "shortDescription": "Credit",
    "longDescription": "Credit"
  },
  "token": "374245111181117",
  "tokenId": "A123GD",
  "tokenStatus": "N",
  "cardExpiryDate": "2021-12",
  "transactionType": {
    "code": "code2",
    "shortDescription": "shortDescription0",
    "longDescription": "longDescription4"
  }
}
```

