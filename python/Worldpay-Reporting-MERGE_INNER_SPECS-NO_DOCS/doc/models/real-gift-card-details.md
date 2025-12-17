
# Real Gift Card Details

Real gift card details.

## Structure

`RealGiftCardDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Network the card is associated with facilitating the payment. |
| `card_holder_id` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |
| `card_holder_verification_method` | `str` | Optional | Refers to when card used on a  payment terminal, credit and debit cards can require a cardholder verification method (CVM) to make sure that the person using the card is the legitimate cardholder.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_account_term` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This fields refers to the term set for card account |
| `cvv_2_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates card verification value, which used for payments. |
| `cvv_2_presence_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the presence of card verification value. Possible values CVV2 value not provided, CVV2 value provided / present, CVV2 value illegible, CVV2 value not on card. |
| `token_assurance_level` | `str` | Optional | A request and response field. A score or confidence level that determines the expected level of assurance associated with the approved token requestor and the identification and verification method performed at the time of token request.<br><br>**Constraints**: *Maximum Length*: `2` |
| `token_expiry` | `str` | Optional | This is the expiration date of the token in the YYYY-MM format with a fixed length of 6.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `avs_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valid for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `remaining_balance` | `float` | Optional | Refers to the amount you still owe after a payment.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "cardNetwork": {
    "code": "C",
    "shortDescription": "DISCOVER",
    "longDescription": "DISCOVER"
  },
  "cardHolderId": {
    "code": "4",
    "shortDescription": "Mail/Phone",
    "longDescription": "MAIL/PHONE"
  },
  "cardHolderVerificationMethod": "Direct",
  "tokenAssuranceLevel": "99",
  "tokenExpiry": "2022-10",
  "avsResponseCode": {
    "code": "Y",
    "shortDescription": "ADDRESS AND 5 DIGIT ZIP MATCH",
    "longDescription": "ADDRESS AND 5 DIGIT ZIP MATCH"
  },
  "remainingBalance": 100.23,
  "cardAccountTerm": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "cvv2ResponseCode": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  }
}
```

