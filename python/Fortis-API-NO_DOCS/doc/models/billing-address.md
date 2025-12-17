
# Billing Address

Billing Address Object

## Structure

`BillingAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `postal_code` | `str` | Optional | The Zip or 'Postal Code' portion of the address associated with the Credit Card (CC) or Bank Account (ACH).<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9\-\s]+$` |
| `street` | `str` | Optional | The Street portion of the address associated with the Credit Card (CC) or Bank Account (ACH).<br><br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |
| `city` | `str` | Optional | The City portion of the address associated with the Credit Card (CC) or Bank Account (ACH).<br><br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[\w\#\,\.\-\'\&\s\/]+$` |
| `state` | `str` | Optional | The State portion of the address associated with the Credit Card (CC) or Bank Account (ACH).<br><br>**Constraints**: *Maximum Length*: `24` |
| `phone` | `str` | Optional | The Phone # to be used to contact Payer if there are any issues processing a transaction.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^\d{10}$` |
| `country` | `str` | Optional | The alpha 3 format country code. |

## Example (as JSON)

```json
{
  "postal_code": "48375",
  "city": "Novi",
  "state": "Michigan",
  "phone": "3339998822",
  "country": "USA",
  "street": "street6"
}
```

