
# Auth Non Real Time Transaction Card Detail

Card details of real time authorization transaction.

## Structure

`AuthNonRealTimeTransactionCardDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_type` | `str` | Optional | Types of card used for the payment. <br> Possible values are CREDIT, DEBIT, GIFT.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Network the card is associated with facilitating the payment. |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `phone_number` | `int` | Optional | Phone Number<br><br>**Constraints**: `>= 10`, `<= 10` |
| `hierarchy` | [`MerchantInfo`](../../doc/models/merchant-info.md) | Optional | Merchant hierarchy levels |

## Example (as JSON)

```json
{
  "cardType": "CREDIT",
  "cardNetwork": {
    "code": "1",
    "shortDescription": "MASTERCARD",
    "longDescription": "MASTERCARD"
  },
  "token": "374245111181117",
  "phoneNumber": 10,
  "hierarchy": {
    "chainCode": "chainCode0",
    "merchantId": "merchantId0",
    "merchantName": "merchantName4"
  }
}
```

