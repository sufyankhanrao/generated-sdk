
# Authorization 1

Resources used to retrieve the authorization details

## Structure

`Authorization1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposists or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `process_date` | `str` | Optional | Indicates the process date of a transaction that has been authorized between the two parties.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `transaction_status` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status' short and long descriptions. |
| `transaction_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates the type of transaction that occurred when funds are transfered between a merchant and a bank, including its short and long descriptions. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_currency_code` | `str` | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units.<br><br>**Constraints**: *Maximum Length*: `3` |
| `card_number` | `str` | Optional | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br>Searches can be done on the full card number, on the first 6 and last 4 digits, or on the last 4 digit searches.<br><br>**Constraints**: *Maximum Length*: `19` |
| `card_type` | `str` | Optional | Types of card used for the payment. <br> Possible values are CREDIT, DEBIT, GIFT.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Network the card is associated with facilitating the payment. |
| `card_expiry_date` | `str` | Optional | Card Expiry date in YYYY-MM format<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `phone_number` | `int` | Optional | Phone Number<br><br>**Constraints**: `>= 10`, `<= 10` |
| `hierarchy` | [`MerchantInfo`](../../doc/models/merchant-info.md) | Optional | Merchant hierarchy levels |
| `fraud_score` | `float` | Optional | Fraud score is a measure that helps gauge risk involved with orders before processing.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `fraud_rule` | `str` | Optional | Fraud rule is a condition that helps you decide whether an activity is fraudulent or not.<br><br>**Constraints**: *Maximum Length*: `256` |
| `fraud_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Predefined set of codes that determines various types of fraudulent activities to classify accordingly. |
| `fraud_rule_result` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | The result of the decision made from the Fraud rule applied for the transaction. |
| `fraud_response_time` | `str` | Optional | Time taken to verify if the transaction was fraudulent.<br><br>**Constraints**: *Maximum Length*: `4` |
| `customer_fields` | [`CustomerFields`](../../doc/models/customer-fields.md) | Optional | Customer details |

## Example (as JSON)

```json
{
  "transactionDateTime": "07/19/2016 16:41:31",
  "processDate": "2016-07-19",
  "transactionStatus": {
    "code": "NC",
    "shortDescription": "DECLINE, PICKUP",
    "longDescription": "DECLINE, PICK UP CARD"
  },
  "transactionType": {
    "code": "11",
    "shortDescription": "POS DB CRD RET",
    "longDescription": "POS DEBIT CARD RETURN"
  },
  "authorizationCode": "73994M",
  "authorizationAmount": 3445.56,
  "cardNumber": "************4353",
  "cardType": "CREDIT",
  "cardNetwork": {
    "code": "1",
    "shortDescription": "MASTERCARD",
    "longDescription": "MASTERCARD"
  },
  "cardExpiryDate": "2021-12",
  "token": "374245111181117",
  "fraudScore": 0.13,
  "fraudRule": "Fraudulent",
  "fraudResponseTime": "30",
  "transactionId": "transactionId6"
}
```

