
# Gift Transaction Details

Gift transaction details.

## Structure

`GiftTransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposits or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `business_date` | `str` | Optional | Indicates date  when business happened<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `transaction_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates the type of transaction that occurred when funds are transfered between a merchant and a bank, including its short and long descriptions. |
| `entry_mode` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_currency_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. |
| `transaction_status` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status' short and long descriptions. |
| `old_authorization_amount` | `float` | Optional | This field indicates the amount is the previous transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `requested_amount` | `float` | Optional | This field indicates the amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `cashback_amount` | `float` | Optional | Amount refunds to the cardholder's account a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_source` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the point of authorization. |
| `mail_phone_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates mail/phone for transaction. |
| `origin_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Type of origin for transactions. |
| `pos_condition_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the POS Condition Code for transactions. |
| `void_indicator` | `str` | Optional | A method of confirming that a terminal received a transaction. The terminal transmits the reference number of the last EFT transaction in each request. If the terminal and host are not in sync, the last EFT transaction is reversed.<br><br>**Constraints**: *Maximum Length*: `1` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |
| `card_holder_id` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |
| `avs_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valid for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `remaining_balance` | `float` | Optional | Refers to the outstanding balance.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `terminal_capability` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Refers to the code of terminal capabilities. |

## Example (as JSON)

```json
{
  "transactionId": "186354016598",
  "transactionDateTime": "07/19/2016 16:41:31",
  "businessDate": "2022-01-01",
  "transactionType": {
    "code": "11",
    "shortDescription": "POS DB CRD RET",
    "longDescription": "POS DEBIT CARD RETURN"
  },
  "entryMode": {
    "code": "1",
    "shortDescription": "KEY ENTERED",
    "longDescription": "KEY ENTERED"
  },
  "authorizationCode": "73994M",
  "authorizationCurrencyCode": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "transactionStatus": {
    "code": "NC",
    "shortDescription": "DECLINE, PICKUP",
    "longDescription": "DECLINE, PICK UP CARD"
  },
  "oldAuthorizationAmount": 104.33,
  "requestedAmount": 100,
  "authorizationAmount": 100,
  "cashbackAmount": 100,
  "authorizationSource": {
    "code": "5",
    "shortDescription": "Issuer Approval",
    "longDescription": "Issuer Approval"
  },
  "posConditionCode": {
    "code": "59",
    "shortDescription": "E-Commerce",
    "longDescription": "E-COMMERCE"
  },
  "voidIndicator": "A",
  "chargeId": "G453",
  "cardHolderId": {
    "code": "4",
    "shortDescription": "Mail/Phone",
    "longDescription": "MAIL/PHONE"
  },
  "avsResponseCode": {
    "code": "Y",
    "shortDescription": "ADDRESS AND 5 DIGIT ZIP MATCH",
    "longDescription": "ADDRESS AND 5 DIGIT ZIP MATCH"
  },
  "remainingBalance": 100.23,
  "terminalCapability": {
    "code": "0",
    "shortDescription": "UNKNOWN",
    "longDescription": "UNKNOWN"
  }
}
```

