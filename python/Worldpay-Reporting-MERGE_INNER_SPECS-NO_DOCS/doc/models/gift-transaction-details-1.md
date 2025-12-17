
# Gift Transaction Details 1

This object provides the details of the gift transactions

## Structure

`GiftTransactionDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `process_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `transaction_date_time` | `str` | Optional | Refers to the date and time when the bank has settled the transaction (deposits or withdraws funds).<br><br>**Constraints**: *Maximum Length*: `19`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}[T]{1}[0-9]{2}:[0-9]{2}:[0-9]{2}` |
| `transaction_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. |
| `authorization_code` | `str` | Optional | Authorization codes are used for any transaction that has restrictions on which users are entitled to access. Authorization Code is a six number code from the issuing bank to the vendor, that authorizes the sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_source` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the point of authorization. |
| `authorization_currency` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. Code is as per ISO Standard country code for United States". |
| `old_authorization_amount` | `float` | Optional | This field indicates the amount is the previous transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `requested_amount` | `float` | Optional | This field indicates the amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_amount` | `float` | Optional | An authorized amount is a sum that a merchant transmits to a credit or debit card processor to make sure the customer has the funds required to make a purchase—the approved amount of money to be charged.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `remaining_balance` | `float` | Optional | Refers to the amount you still owe after a payment.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `cashback_amount` | `float` | Optional | Amount refunds to the cardholder's account a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `entry_mode` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `void_indicator` | `str` | Optional | A method of confirming that a terminal received a transaction. The terminal transmits the reference number of the last EFT transaction in each request. If the terminal and host are not in sync, the last EFT transaction is reversed.<br><br>**Constraints**: *Maximum Length*: `1` |
| `origin_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Represents the origination type of the transaction. |
| `pos_condition_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the POS Condition Code for transactions. |
| `gc_retrieval_reference_number` | `str` | Optional | Gift Card Retrieval Reference Number, a key to uniquely identify a card transaction based on the ISO 8583 standard.<br><br>**Constraints**: *Maximum Length*: `12` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `avs_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valide for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `card_holder_id` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |

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
  "authorizationCode": "73994M",
  "authorizationSource": {
    "code": "5",
    "shortDescription": "Issuer Approval",
    "longDescription": "Issuer Approval"
  },
  "authorizationCurrency": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "oldAuthorizationAmount": 104.33,
  "requestedAmount": 100.02,
  "authorizationAmount": 100.04,
  "remainingBalance": 100.23,
  "cashbackAmount": 9.06,
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "voidIndicator": "A",
  "posConditionCode": {
    "code": "59",
    "shortDescription": "E-Commerce",
    "longDescription": "E-COMMERCE"
  },
  "chargeId": "G453",
  "avsResponseCode": {
    "code": "Y",
    "shortDescription": "ADDRESS AND 5 DIGIT ZIP MATCH",
    "longDescription": "ADDRESS AND 5 DIGIT ZIP MATCH"
  },
  "cardHolderId": {
    "code": "4",
    "shortDescription": "Mail\\Phone",
    "longDescription": "MAIL\\PHONE"
  }
}
```

