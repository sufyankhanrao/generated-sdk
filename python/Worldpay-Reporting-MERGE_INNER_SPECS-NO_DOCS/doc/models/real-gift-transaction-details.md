
# Real Gift Transaction Details

Real gift card transaction details.

## Structure

`RealGiftTransactionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposits or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `business_date` | `str` | Optional | Indicates date  when business happened<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `transaction_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates transaction identification code. |
| `entry_mode` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | POS Entry Mode defines the conditions under which the card account number/PAN is entered and the terminal PIN capabilities. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_currency_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. |
| `transaction_status` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status' short and long descriptions. |
| `old_authorization_amount` | `float` | Optional | This field indicates the amount is the previous transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `requested_amount` | `float` | Optional | This field indicates the amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `cashback_amount` | `float` | Optional | Amount refunds to the cardholder's account a small percentage of the sum spent on purchases.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "transactionDateTime": "07/19/2016 16:41:31",
  "businessDate": "2022-01-01",
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
  "requestedAmount": 100.02,
  "authorizationAmount": 100.02,
  "cashbackAmount": 9.06,
  "transactionId": "transactionId6",
  "transactionCode": {
    "code": "code8",
    "shortDescription": "shortDescription6",
    "longDescription": "longDescription0"
  }
}
```

