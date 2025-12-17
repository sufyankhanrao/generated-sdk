
# Read Owner

## Structure

`ReadOwner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Required | Required.<br><br>**Constraints**: *Maximum Length*: `21` |
| `title` | `str` | Optional | Required for AMEX acquired merchants otherwise optional.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `first_name` | `str` | Required | First name. Region based validations will be applied to this field.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `15`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `middle_initial` | `str` | Optional | Middle initial.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `last_name` | `str` | Required | Last name. Region based validations will be applied to this field.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `ssn` | `str` | Optional | Social security number. Dashes not included.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9`, *Pattern*: `^[0-9]{9}$` |
| `dob` | `date` | Optional | Date of Birth (CCYY-MM-DD). Must be at least 18 years old. |
| `email` | `str` | Optional | Email address of the contact. Must have @ and a .<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `(\\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\\.)+[A-Za-z0-9]{2,}\\b{0,64})` |
| `phone_number` | `str` | Optional | 10-digit phone number of the format  5131234567.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{10}$` |
| `phone_number_ext` | `str` | Optional | Phone number extension. Up to 8 digits of the format 12345678.<br><br>**Constraints**: *Maximum Length*: `8`, *Pattern*: `([0-9]{8})$` |
| `phone_type` | [`PhoneTypeEnum`](../../doc/models/phone-type-enum.md) | Optional | Phone type.<br><br>**Constraints**: *Maximum Length*: `8` |
| `alternate_phone` | `str` | Optional | 10-digit alternate phone number of the format  1234567890.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{10}$` |
| `alternate_phone_type` | [`AlternatePhoneTypeEnum`](../../doc/models/alternate-phone-type-enum.md) | Optional | Alternate phone type.<br><br>**Constraints**: *Maximum Length*: `10` |
| `fax_number` | `str` | Optional | 10-digit fax number of the format 5131234567<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{10}$` |
| `ownership_percentage` | `int` | Optional | Ownership stake percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `address_line_1` | `str` | Required | Address Line 1. Field for house number, street and direction.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `address_line_2` | `str` | Optional | Address Line 2. Field for apartment or suite numbers, etc.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `city` | `str` | Required | Name of the City<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `28`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `state` | `str` | Optional | Valid state, commonwealth, and territory codes are allowed.<br><br>**Constraints**: *Maximum Length*: `2` |
| `country` | `str` | Required | Name of Country.<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Required | Postal code / zip code. The postal code must be valid for the address' country code.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5`, *Pattern*: `^[a-zA-Z0-9]` |
| `postal_code_extension` | `str` | Optional | Postal code / zip code extension.  The postal code extension must be valid for the address'.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4`, *Pattern*: `^[0-9]{4}$` |

## Example (as JSON)

```json
{
  "type": "Owner 2 Contact",
  "title": "President",
  "firstName": "John",
  "middleInitial": "M",
  "lastName": "Doe",
  "dob": "1954-01-01",
  "phoneNumber": "5139004357",
  "phoneNumberExt": "12345678",
  "phoneType": "Mobile",
  "alternatePhone": "1234567890",
  "alternatePhoneType": "Mobile",
  "faxNumber": "5139003344",
  "OwnershipPercentage": 10,
  "addressLine1": "4355 N Coalwhipe St.",
  "addressLine2": "suite 104",
  "city": "Denver",
  "state": "CO",
  "country": "US",
  "postalCode": "80237",
  "postalCodeExtension": "1384",
  "ssn": "ssn0",
  "email": "email2"
}
```

