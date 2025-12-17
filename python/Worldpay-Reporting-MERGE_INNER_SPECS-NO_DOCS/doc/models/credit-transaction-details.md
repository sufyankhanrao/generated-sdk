
# Credit Transaction Details

This object provides transaction amount related information

## Structure

`CreditTransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `process_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `transaction_date_time` | `str` | Optional | Refers to the date and time when the bank has settled the transaction (deposits or withdraws funds).<br><br>**Constraints**: *Maximum Length*: `19`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}[T]{1}[0-9]{2}:[0-9]{2}:[0-9]{2}` |
| `authorization_amount` | `float` | Optional | An authorized amount is a sum that a merchant transmits to a credit or debit card processor to make sure the customer has the funds required to make a purchase—the approved amount of money to be charged.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_code` | `int` | Optional | Authorization codes are used for any transaction that has restrictions on which users are entitiled to access. Authorization Code is a six number code from the issuing bank to the vendor, that authorizes the sale. |
| `authorization_currency` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. Code is as per ISO Standard country code for United States". |
| `transaction_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. |
| `entry_mode` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `avs_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valide for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `cardholder_id` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |
| `sequence_number` | `str` | Optional | Sequence Number<br><br>**Constraints**: *Maximum Length*: `256` |
| `customer_identifier` | `str` | Optional | This field indicates the ecom customer identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_order_identifier` | `str` | Optional | This field indicates the ecom merchant order identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `campaign` | `str` | Optional | This field indicates the ecom campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `affiliate` | `str` | Optional | This field indicates the ecom affiliate.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_grouping_identifier` | `str` | Optional | This field indicates the ecom merchant grouping identifier<br><br>**Constraints**: *Maximum Length*: `25` |
| `report_group` | `str` | Optional | This field indicates the ecom report group<br><br>**Constraints**: *Maximum Length*: `25` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `aci` | `str` | Optional | It determines whether the authorization qualifies for Visa Custom Payment Service (CPS).<br><br>**Constraints**: *Maximum Length*: `256` |
| `mail_phone_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicator for mail/phone order and description of the code - card not present transaction |
| `origin_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Represents the origination type of the transaction. |
| `validation_code` | `str` | Optional | Refers to visa validation code<br><br>**Constraints**: *Maximum Length*: `256` |
| `mastercard_wallet_id` | `str` | Optional | Master card wallet identifier<br><br>**Constraints**: *Maximum Length*: `3` |
| `mastercard_tic_indicator` | `str` | Optional | Mastercard transaction integrity class indicator<br><br>**Constraints**: *Maximum Length*: `3` |
| `bank_net_date` | `str` | Optional | Payments network operated by master card, value will be present only if transaction is master card, otherwise null.<br><br>**Constraints**: *Maximum Length*: `8`, *Pattern*: `--[0-9]{2}-[0-9]{2}` |
| `bank_net_reference_number` | `str` | Optional | Bank Reference Number<br><br>**Constraints**: *Maximum Length*: `256` |
| `pos_register_number` | `str` | Optional | Refers to registered POS Number<br><br>**Constraints**: *Maximum Length*: `256` |
| `terminal_number` | `str` | Optional | Terminal number is an eight-digit sequence of characters used by financial institutions to monitor which terminal is used to process a transaction.<br><br>**Constraints**: *Maximum Length*: `256` |
| `reference_number` | `str` | Optional | Refers to a key to uniquely identify a card transaction based on the ISO 8583 standard.<br><br>**Constraints**: *Maximum Length*: `16` |
| `merchant_reference_number` | `str` | Optional | Refers to merchant reference or draft locator number<br><br>**Constraints**: *Maximum Length*: `11` |
| `terminal_capability` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Refers to the code of terminal capabilities. |

## Example (as JSON)

```json
{
  "transactionId": "141710009519",
  "processDate": "2022-06-16",
  "transactionDateTime": "07/19/2016 16:41:31",
  "authorizationAmount": 100.04,
  "authorizationCode": 112920,
  "authorizationCurrency": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "transactionType": {
    "code": "253",
    "description": "SALE",
    "longDescription": "SALE"
  },
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "cardholderId": {
    "code": "4",
    "shortDescription": "Mail\\Phone",
    "longDescription": "MAIL\\PHONE"
  },
  "sequenceNumber": "34",
  "customerIdentifier": "G768",
  "merchantOrderIdentifier": "A453",
  "campaign": "D453",
  "affiliate": "G123",
  "merchantGroupingIdentifier": "S673",
  "reportGroup": "E874",
  "chargeId": "G453",
  "aci": "Card Present",
  "validationCode": "TN2S",
  "mastercardWalletId": "DR1",
  "mastercardTICIndicator": "EU9",
  "bankNetDate": "--12-02",
  "bankNetReferenceNumber": "65678787979",
  "posRegisterNumber": "0050",
  "terminalNumber": "D0640450",
  "referenceNumber": "2444600338440029",
  "merchantReferenceNumber": "65678787979"
}
```

