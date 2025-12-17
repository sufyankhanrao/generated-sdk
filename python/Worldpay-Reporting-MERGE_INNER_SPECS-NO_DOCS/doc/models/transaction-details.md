
# Transaction Details

Transaction details.

## Structure

`TransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposits or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `transaction_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates the type of transaction that occurred when funds are transfered between a merchant and a bank, including its short and long descriptions. |
| `transaction_status` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status' short and long descriptions. |
| `entry_mode` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_currency` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the response code is another name for a credit card authorization code. |
| `old_authorization_amount` | `float` | Optional | This field indicates the amount is the previous transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `requested_amount` | `float` | Optional | This field indicates the amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `terminal_capability` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Refers to the code of terminal capabilities. |
| `aci` | `str` | Optional | It determines whether the authorization qualifies for visa custom payment service (CPS).<br><br>**Constraints**: *Maximum Length*: `256` |
| `affiliate` | `str` | Optional | The merchant-specified identifier used to track transactions associated with your affiliate organizations.<br><br>**Constraints**: *Maximum Length*: `25` |
| `application_identifier` | `str` | Optional | An application identifier is a number at the beginning of a string of data that identifies the intended interpretation of the data.<br><br>**Constraints**: *Maximum Length*: `32` |
| `authorization_source` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the point of authorization. |
| `avs_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valid for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `campaign` | `str` | Optional | This field indicates the ecom campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `card_holder_id` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |
| `card_holder_verification_method` | `str` | Optional | Refers to when card used on a  payment terminal, credit and debit cards can require a cardholder verification method (CVM) to make sure that the person using the card is the legitimate cardholder.<br><br>**Constraints**: *Maximum Length*: `6` |
| `void_indicator` | `str` | Optional | A method of confirming that a terminal received a transaction. The terminal transmits the reference number of the last EFT transaction in each request. If the terminal and host are not in sync, the last EFT transaction is reversed.<br><br>**Constraints**: *Maximum Length*: `1` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `customer_identifier` | `str` | Optional | The unique identifier of the purchaser associated with the transaction.<br><br>**Constraints**: *Maximum Length*: `25` |
| `mail_phone_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicator of mail/phone for transactions. |
| `merchant_grouping_identifier` | `str` | Optional | The merchant-specified identifier for grouping transactions by an additional transaction level ID outside of Affiliate or Campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_order_identifier` | `str` | Optional | The merchant-designated identifier for this transaction (i.e., value of the orderId element).<br><br>**Constraints**: *Maximum Length*: `25` |
| `card_emv` | `bool` | Optional | Refers when the value is set to Y if the card is EMV capable. Possible Values True or False. |
| `offline_emv` | `bool` | Optional | Refers when the value is set to Y if the authorization used the chip EMV Offline Transaction Flag. Possible values True or False |
| `terminal_emv` | `bool` | Optional | Refers when the value is set to Y if the terminal was EMV chip card capable. .Possible values True or False |
| `transaction_emv` | `bool` | Optional | Refers when the value is set to Y if this is an EMV Chip Card transaction.Possible values True or False |
| `origin_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Type of origin for transactions. |
| `pos_condition_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the POS Condition Code for transactions. |
| `report_group` | `str` | Optional | The Reporting Group category to which the transaction belongs.<br><br>**Constraints**: *Maximum Length*: `50` |
| `validation_code` | `str` | Optional | This field indicates the validation code for card networks- visa transactions.<br><br>**Constraints**: *Maximum Length*: `4` |
| `authorization_communication_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization communication details. |
| `issuer_country_code` | `str` | Optional | Indicates the country of the issuer according to ISO 3166.<br><br>**Constraints**: *Maximum Length*: `3` |
| `unique_serial_device` | `str` | Optional | This field indicates the unique id of device.<br><br>**Constraints**: *Maximum Length*: `16` |
| `bank_net_date` | `str` | Optional | Payments network operated by master card, value will be present only if transaction is master card, otherwise null.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^--[0-9]{2}-[0-9]{2}$` |
| `master_card_tic_indicator` | `str` | Optional | Master Card Transaction Integrity Class Indicator<br><br>**Constraints**: *Maximum Length*: `2` |

## Example (as JSON)

```json
{
  "transactionId": "186354016598",
  "transactionDateTime": "07/19/2016 16:41:31",
  "transactionType": {
    "code": "11",
    "shortDescription": "POS DB CRD RET",
    "longDescription": "POS DEBIT CARD RETURN"
  },
  "transactionStatus": {
    "code": "NC",
    "shortDescription": "DECLINE, PICKUP",
    "longDescription": "DECLINE, PICK UP CARD"
  },
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "authorizationAmount": 100,
  "authorizationCurrency": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "authorizationCode": "73994M",
  "authorizationResponseCode": {
    "code": "0",
    "shortDescription": "Transaction approved",
    "longDescription": "Transaction approved"
  },
  "oldAuthorizationAmount": 100,
  "requestedAmount": 100,
  "terminalCapability": {
    "code": "0",
    "shortDescription": "UNKNOWN",
    "longDescription": "UNKNOWN"
  },
  "aci": "Card Present",
  "affiliate": "1009648",
  "applicationIdentifier": "E",
  "authorizationSource": {
    "code": "5",
    "shortDescription": "Issuer Approval",
    "longDescription": "Issuer Approval"
  },
  "avsResponseCode": {
    "code": "Y",
    "shortDescription": "ADDRESS AND 5 DIGIT ZIP MATCH",
    "longDescription": "ADDRESS AND 5 DIGIT ZIP MATCH"
  },
  "campaign": "D453",
  "cardHolderId": {
    "code": "4",
    "shortDescription": "Mail/Phone",
    "longDescription": "MAIL/PHONE"
  },
  "cardHolderVerificationMethod": "Direct",
  "voidIndicator": "A",
  "chargeId": "G453",
  "customerIdentifier": "98765",
  "merchantGroupingIdentifier": "1098675",
  "merchantOrderIdentifier": "45356",
  "cardEMV": true,
  "offlineEMV": true,
  "terminalEMV": true,
  "transactionEMV": true,
  "posConditionCode": {
    "code": "59",
    "shortDescription": "E-Commerce",
    "longDescription": "E-COMMERCE"
  },
  "reportGroup": "1098675",
  "validationCode": "3435",
  "authorizationCommunicationType": {
    "code": "0",
    "shortDescription": "STANDARD RAFT",
    "longDescription": "STANDARD RAFT"
  },
  "issuerCountryCode": "USA",
  "uniqueSerialDevice": "B8973827348H43",
  "bankNetDate": "--12-02",
  "masterCardTICIndicator": "DE"
}
```

