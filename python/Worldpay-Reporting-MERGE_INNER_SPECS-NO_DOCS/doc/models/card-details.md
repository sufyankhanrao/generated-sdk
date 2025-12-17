
# Card Details

Card details.

## Structure

`CardDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_network` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Network the card is associated with facilitating the payment. |
| `card_holder_id` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the unique identification number issued by the provider to the insured. |
| `card_account_term` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This fields refers to the term set for card account. |
| `card_product_results` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This fields refers to the results of card products. |
| `card_emv` | `bool` | Optional | This field indicates the Card EMV Capability Flag , when it Set the value to Y if the card is EMV capable. Possible Values True or False |
| `card_holder_verification_method` | `str` | Optional | Refers to when card used on a  payment terminal, credit and debit cards can require a cardholder verification method (CVM) to make sure that the person using the card is the legitimate cardholder.<br><br>**Constraints**: *Maximum Length*: `6` |
| `cvv_2_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates card verification value, which used for payments. |
| `cvv_2_presence_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the presence of card verification value. Possible values CVV2 value not provided, CVV2 value provided / present, CVV2 value illegible, CVV2 value not on card. |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `token_id` | `str` | Optional | Token ID is a host-generated numeric value created during the tokenization process using a token key assigned to a merchant. This value is returned to the POS when tokenization is requested along with the token for utilization.<br><br>**Constraints**: *Maximum Length*: `6` |
| `token_requestor_id` | `str` | Optional | An identifier to request network tokens from the card networks.<br><br>**Constraints**: *Maximum Length*: `11` |
| `token_assurance_level` | `str` | Optional | A request and response field. A score or confidence level that determines the expected level of assurance associated with the approved token requestor and the identification and verification method performed at the time of token request.<br><br>**Constraints**: *Maximum Length*: `2` |
| `token_expiry` | `str` | Optional | This is the expiration date of the token in the YYYY-MM format with a fixed length of 6.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `cavv_response` | `str` | Optional | This field indicates Cardholder Authentication Verification Value, used by eCommerce websites when authentication is desired for Verified by VISA.<br><br>**Constraints**: *Maximum Length*: `1` |
| `avs_response_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Address Verification Service (AVS) data is the address and/or zip code of the cardholder. AVS data is only valid for credit.AVS data is not valid for fleet, debit, or EBT cards.Store policy dictates if a transaction is approved or denied based on the AVS response. ( Length - 2 Character) |
| `master_card_tic_indicator` | `str` | Optional | Master Card Transaction Integrity Class Indicator<br><br>**Constraints**: *Maximum Length*: `2` |

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
  "cardEMV": true,
  "cardHolderVerificationMethod": "Direct",
  "token": "374245111181117",
  "tokenId": "A834GD",
  "tokenRequestorId": "AZDAJAKAYHE",
  "tokenAssuranceLevel": "99",
  "tokenExpiry": "2022-10",
  "cavvResponse": "B",
  "avsResponseCode": {
    "code": "Y",
    "shortDescription": "ADDRESS AND 5 DIGIT ZIP MATCH",
    "longDescription": "ADDRESS AND 5 DIGIT ZIP MATCH"
  },
  "masterCardTICIndicator": "MC",
  "cardAccountTerm": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "cardProductResults": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  }
}
```

