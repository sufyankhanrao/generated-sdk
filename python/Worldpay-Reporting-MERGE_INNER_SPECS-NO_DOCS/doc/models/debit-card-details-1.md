
# Debit Card Details 1

This object provides debit card related information

## Structure

`DebitCardDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder_bank_acro` | `str` | Optional | Card Holder Bank<br><br>**Constraints**: *Maximum Length*: `4` |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `256` |
| `token_id` | `str` | Optional | Token ID is a host-generated numeric value created during the tokenization process using a token key assigned to a merchant. This value is returned to the POS when tokenization is requested along with the token for utilization.<br><br>**Constraints**: *Maximum Length*: `256` |
| `token_assurance_level` | `str` | Optional | A request and response field. A score or confidence level that determines the expected level of assurance associated with the approved token requestor and the identification and verification method performed at the time of token request.<br><br>**Constraints**: *Maximum Length*: `256` |
| `token_expiration_date` | `str` | Optional | This is the expiration date of the token in the YYYY-MM format with a fixed length of 6.<br><br>**Constraints**: *Maximum Length*: `7`, *Pattern*: `[0-9]{2}-[0-9]{2}` |

## Example (as JSON)

```json
{
  "cardHolderBankAcro": "MAE1",
  "token": "374245111181117",
  "tokenId": "A834GD",
  "tokenAssuranceLevel": "99",
  "tokenExpirationDate": "2022-10"
}
```

