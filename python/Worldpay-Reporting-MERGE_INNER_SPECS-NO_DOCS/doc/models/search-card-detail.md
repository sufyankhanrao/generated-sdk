
# Search Card Detail

## Structure

`SearchCardDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_type` | `str` | Optional | Type of the payment card. Possible values CREDIT, DEBIT, GIFTCARD<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_network` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Network which facilitates the payment card transactions as per the card association. |
| `token` | `str` | Optional | A Token is a substitution for Primary AccountNumber (PAN which is the card number) with proxy data which is a measure to avoid fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `network_token` | `str` | Optional | Token associated to a transaction by the Card Network<br><br>**Constraints**: *Maximum Length*: `20` |
| `hierarchy` | [`MerchantHierarchyDetails1`](../../doc/models/merchant-hierarchy-details-1.md) | Optional | This object holds the entity and its hierarchy level |

## Example (as JSON)

```json
{
  "cardType": "CREDIT",
  "token": "374245111181117",
  "networkToken": "3434343",
  "cardNetwork": {
    "code": "code8",
    "shortDescription": "shortDescription6",
    "longDescription": "longDescription0"
  },
  "hierarchy": {
    "chainCode": "chainCode0",
    "storeNumber": "storeNumber2",
    "merchantId": "merchantId0",
    "merchantName": "merchantName4"
  }
}
```

