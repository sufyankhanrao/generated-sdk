
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | Address Line 1. Field for House Number, Street and Direction<br><br>**Constraints**: *Maximum Length*: `40` |
| `address_line_2` | `str` | Optional | Address Line 2. Field for Apt No, Suite No etc.<br><br>**Constraints**: *Maximum Length*: `40` |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `28` |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Required | Only valid US state codes (including Puerto Rico, Guam and Virgin Islands), Canadian province codes and Military state codes (AE - Armed Forces Africa, Canada, Europe, Middle East; AA - Armed Forces Americas (except Canada) ; AP - Armed Forces Pacific) are allowed |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Required | Only USA and Canada is allowed now. |
| `postal_code` | `str` | Required | Postal Code / Zip Code. The postalCode must be valid for the address’s country code. US codes must be exactly 5 digits long (regular expression [0-9]{5}). Canadian Postal Codes must be exactly 6 alphanumeric characters long.<br><br>**Constraints**: *Pattern*: `^\d{5}$` |
| `postal_code_extension` | `str` | Optional | Postal Code / Zip Code Extension.  The postalCode extension must be valid for the address’s country code. US codes must be exactly 4 digits long (regular expression [0-9]{4}). Doesn't exist for Canadian submerchants.<br><br>**Constraints**: *Pattern*: `^\d{4}$` |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Required | Required. Address Type   1) Only Physical address is mandatory.  2) For any address type, streetAddress1, city, state, postalCode and countryCode are mandatory. |

## Example (as JSON)

```json
{
  "addressLine1": "100 West St",
  "addressLine2": "Suite 200",
  "city": "Anchorage",
  "state": "MO",
  "country": "US",
  "postalCode": "99501",
  "postalCodeExtension": "5555",
  "type": "TerminalDeployment"
}
```

