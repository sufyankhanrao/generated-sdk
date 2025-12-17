
# Settle Transaction Info

## Structure

`SettleTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the date and time when the bank has settled the transaction (deposits or withdraws funds).<br><br>**Constraints**: *Maximum Length*: `19`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}[T]{1}[0-9]{2}:[0-9]{2}:[0-9]{2}` |
| `process_date` | `str` | Optional | Refers to the date when the transaction has been processed for settlement between the two parties.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `transaction_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. |
| `transaction_status` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates the functions performed in a transaction. |
| `authorization_code` | `str` | Optional | Authorization codes are used for any transaction that has restrictions on which users are entitiled to access. Authorization Code is a six number code from the issuing bank to the vendor, that authorizes the sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `amount` | `float` | Optional | Refers to the settled amount between the parties. |
| `authorization_currency` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. Code is as per ISO Standard country code for United States". |
| `reference_number` | `str` | Optional | Refers to a key to uniquely identify a card transaction based on the ISO 8583 standard.<br><br>**Constraints**: *Maximum Length*: `16` |
| `entry_mode` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `avs_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valide for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Characters) |
| `terminal_number` | `str` | Optional | Terminal number is an eight-digit sequence of characters used by financial institutions to monitor which terminal is used to process a transaction.<br><br>**Constraints**: *Maximum Length*: `16777216` |

## Example (as JSON)

```json
{
  "transactionId": "141710009519",
  "transactionDateTime": "07/19/2016 16:41:31",
  "processDate": "2021-07-19",
  "transactionType": {
    "code": "253",
    "description": "SALE",
    "longDescription": "SALE",
    "shortDescription": "shortDescription0"
  },
  "transactionStatus": {
    "code": "NC",
    "description": "DECLINE, PICKUP",
    "longDescription": "DECLINE, PICK UP CARD",
    "shortDescription": "shortDescription4"
  },
  "authorizationCode": "112920",
  "amount": 3445.56,
  "authorizationCurrency": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "referenceNumber": "2444600338440029",
  "terminalNumber": "D0640450"
}
```

