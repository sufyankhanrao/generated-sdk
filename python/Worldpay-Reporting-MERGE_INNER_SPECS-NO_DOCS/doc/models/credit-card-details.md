
# Credit Card Details

This object provides gift card related information

## Structure

`CreditCardDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_network` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates type of card networks, which are used for payments. |
| `cvv_2_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This object provides the information on response for the card verification value. |
| `cvv_2_presence_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the presence of card verification value. Possible values CVV2 value not provided, CVV2 value provided / present, CVV2 value illegible, CVV2 value not on card. |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `token_id` | `str` | Optional | Token id is a host-generated numeric value created during the tokenization process using a token key assigned to a merchant. This value is returned to the POS when tokenization is requested along with the token for utilization.<br><br>**Constraints**: *Maximum Length*: `256` |
| `token_assurance_level` | `str` | Optional | A request and response field. A score or confidence level that determines the expected level of assurance associated with the approved token requestor and the identification and verification method performed at the time of token request.<br><br>**Constraints**: *Maximum Length*: `256` |
| `token_expiration_date` | `str` | Optional | This is the expiration date of the token in the YYYY-MM format with a fixed length of 6.<br><br>**Constraints**: *Maximum Length*: `7`, *Pattern*: `[0-9]{4}-[0-9]{2}` |
| `international_indicator` | `bool` | Optional | Indicator for international transaction |
| `network_reject_indicator` | `bool` | Optional | Possible values are true and false |

## Example (as JSON)

```json
{
  "cardNetwork": {
    "code": "C",
    "shortDescription": "DISCOVER",
    "longDescription": "DISCOVER"
  },
  "token": "374245111181117",
  "tokenId": "A834GD",
  "tokenAssuranceLevel": "99",
  "tokenExpirationDate": "2022-12",
  "internationalIndicator": true,
  "networkRejectIndicator": true,
  "cvv2ResponseCode": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  },
  "cvv2PresenceIndicator": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  }
}
```

