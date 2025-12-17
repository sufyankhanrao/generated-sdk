
# Sensitive Gift Real Card Details

sensitive Card Details.

## Structure

`SensitiveGiftRealCardDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number` | `str` | Optional | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br>Searches can be done on the full card number, on the first 6 and last 4 digits, or on the last 4 digit searches.<br><br>**Constraints**: *Maximum Length*: `19` |
| `expiration_date` | `str` | Optional | An expiration date is a set time when a card will need to be replaced.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `last_four_of_pan` | `str` | Optional | Field is used to provide the last 4-digits of the PAN on the receipt.<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "cardNumber": "************1111",
  "expirationDate": "2022-12",
  "lastFourOfPAN": "3245"
}
```

