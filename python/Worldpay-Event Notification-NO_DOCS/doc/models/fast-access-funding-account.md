
# Fast Access Funding Account

## Structure

`FastAccessFundingAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | Status of the Fast Access Funding<br><br>**Constraints**: *Maximum Length*: `1` |
| `cardholder_name` | `str` | Optional | Name of the card holder<br><br>**Constraints**: *Maximum Length*: `50` |
| `card_number` | `str` | Optional | Card Number<br><br>**Constraints**: *Maximum Length*: `19` |
| `card_expiration_date` | `date` | Optional | Using ISO 8601 'yyyy-mm-dd' |

## Example (as JSON)

```json
{
  "status": "O",
  "cardholderName": "John Doe",
  "cardNumber": "XXXXXXXXX8586",
  "cardExpirationDate": "2025-01-31"
}
```

