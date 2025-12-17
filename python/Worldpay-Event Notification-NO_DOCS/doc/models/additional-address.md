
# Additional Address

This aggregate field includes details of address

## Structure

`AdditionalAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | Address Line 1. Field for house number, street and direction.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `address_line_2` | `str` | Optional | Address Line 2. Field for apartment or suite numbers, etc.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `city` | `str` | Required | Name of the City<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `28`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `county` | `str` | Optional | Name of County.<br><br>**Constraints**: *Maximum Length*: `20` |
| `state` | `str` | Required | Valid state, commonwealth, and territory codes are allowed.<br><br>**Constraints**: *Maximum Length*: `2` |
| `country` | `str` | Optional | Name of Country.<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Required | Postal code / zip code. The postal code must be valid for the address' country code.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5`, *Pattern*: `^[a-zA-Z0-9]` |
| `international_postal_code` | `str` | Optional | International Postal code / zip code. The international postal code must be valid for the address'.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9]` |
| `postal_code_extension` | `str` | Optional | Postal code / zip code extension.  The postal code extension must be valid for the address'.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4`, *Pattern*: `^[0-9]{4}$` |
| `timezone` | `str` | Optional | Timezone<br><br>**Constraints**: *Maximum Length*: `3` |

## Example (as JSON)

```json
{
  "addressLine1": "4355 N Coalwhipe St.",
  "addressLine2": "suite 104",
  "city": "Denver",
  "county": "Douglas",
  "state": "CO",
  "country": "US",
  "postalCode": "80237",
  "internationalPostalCode": "H4N 1K4",
  "postalCodeExtension": "1384",
  "timezone": "MST"
}
```

