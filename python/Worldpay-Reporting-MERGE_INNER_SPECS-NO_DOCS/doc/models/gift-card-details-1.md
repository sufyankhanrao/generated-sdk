
# Gift Card Details 1

This object provides gift card related information

## Structure

`GiftCardDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_network` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates type of card networks, which are used for payments. |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `token_id` | `str` | Optional | Token ID is a host-generated numeric value created during the tokenization process using a token key assigned to a merchant. This value is returned to the POS when tokenization is requested along with the token for utilization.<br><br>**Constraints**: *Maximum Length*: `6` |
| `cvv_2_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This object provides the information on response for the card verification value. |
| `cvv_2_presence_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | This field indicates the presence of card verification value. Possible values CVV2 value not provided, CVV2 value provided / present, CVV2 value illegible, CVV2 value not on card. |

## Example (as JSON)

```json
{
  "cardNetwork": {
    "code": "G",
    "shortDescription": "GIFT",
    "longDescription": "GIFT"
  },
  "token": "374245111181117",
  "tokenId": "A834GD",
  "cvv2ResponseCode": {
    "code": "M",
    "shortDescription": "CVV2 Match",
    "longDescription": "CVV2 Match"
  },
  "cvv2PresenceIndicator": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  }
}
```

