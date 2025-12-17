
# Auth Real Time Transaction Card Detail

Card details of real time authorization transaction.

## Structure

`AuthRealTimeTransactionCardDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number` | `str` | Optional | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br>Searches can be done on the full card number, on the first 6 and last 4 digits, or on the last 4 digit searches.<br><br>**Constraints**: *Maximum Length*: `19` |
| `card_type` | `str` | Optional | Types of card used for the payment. <br> Possible values are CREDIT, DEBIT, GIFT.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Network the card is associated with facilitating the payment. |
| `card_expiry_date` | `str` | Optional | Card Expiry date in YYYY-MM format<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `phone_number` | `int` | Optional | Phone Number<br><br>**Constraints**: `>= 10`, `<= 10` |
| `hierarchy` | [`MerchantInfo`](../../doc/models/merchant-info.md) | Optional | Merchant hierarchy levels |

## Example (as JSON)

```json
{
  "cardNumber": "************4353",
  "cardType": "CREDIT",
  "cardNetwork": {
    "code": "1",
    "shortDescription": "MASTERCARD",
    "longDescription": "MASTERCARD"
  },
  "cardExpiryDate": "2021-12",
  "token": "374245111181117"
}
```

