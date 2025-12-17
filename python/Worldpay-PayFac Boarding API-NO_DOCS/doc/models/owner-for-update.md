
# Owner for Update

Owner of a Sub Merchant.

Please refer to the Beneficial Ownership section under Submerchant Boarding on the left hand side menu in the developer portal for specific requiremets on Owner's SSN and DOB and other attributes. They can be required based on Ownership Type and Ownership Percentage.
https://developerengine.fisglobal.com/apis/payfac#PFBeneficialOwners

## Structure

`OwnerForUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Title of the Owner. Required for Amex OptBlue merchants. For Amex ESA, the title would default to “Principal” if not sent in the request.<br><br>**Constraints**: *Maximum Length*: `40` |
| `first_name` | `str` | Required | First Name of the Owner<br><br>**Constraints**: *Maximum Length*: `15` |
| `middle_initial` | `str` | Optional | Middle Initial of the Owner<br><br>**Constraints**: *Maximum Length*: `1` |
| `last_name` | `str` | Required | Last Name of the Owner<br><br>**Constraints**: *Maximum Length*: `25` |
| `phone_number` | `str` | Required | Phone Number of the Owner. 10 digt number of the format 5131234567<br><br>**Constraints**: *Pattern*: `^\d{10}$` |
| `phone_number_ext` | `str` | Optional | Phone Number Extension of the Owner<br><br>**Constraints**: *Maximum Length*: `8` |
| `fax_number` | `str` | Optional | Fax Number of the Owner. Must be 10 digit number of the format 5131234567<br><br>**Constraints**: *Pattern*: `^\d{10}$` |
| `email` | `str` | Required | Email address of the contact. Must have @ and a .<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: ``^[a-zA-Z0-9.!#$%&’*+=?^_`{\|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$`` |
| `ownership_percentage` | `int` | Required | Owner Stake Percentage.OwnershipPercentage must be provided whenever it is greater than or equal to 25% for US and greater than or equal to 10% for Canada.<br><br>**Constraints**: `>= 1`, `<= 100` |
| `ssn` | `str` | Optional | Owner SSN. Please refer to the Beneficial Ownership section under Submerchant Boarding on the left hand side menu in the developer portal for specific requirements on Owner SSN.https://developerengine.fisglobal.com/apis/payfac#PFBeneficialOwners<br><br>**Constraints**: *Pattern*: `^\d{9}$` |
| `dob` | `date` | Optional | Owner Date of Birth. Please refer to the Beneficial Ownership section under Submerchant Boarding on the left hand side menu in the developer portal for specific requirements on Owner DOB.https://developerengine.fisglobal.com/apis/payfac#PFBeneficialOwners |
| `address_line_1` | `str` | Required | Address Line 1. Field for House Number, Street and Direction<br><br>**Constraints**: *Maximum Length*: `40` |
| `address_line_2` | `str` | Optional | Address Line 2. Field for Apt No, Suite No etc.<br><br>**Constraints**: *Maximum Length*: `40` |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `28` |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Required | Only valid US state codes (including Puerto Rico, Guam and Virgin Islands), Canadian province codes and Military state codes (AE - Armed Forces Africa, Canada, Europe, Middle East; AA - Armed Forces Americas (except Canada) ; AP - Armed Forces Pacific) are allowed |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Required | Only USA and Canada is allowed now. |
| `postal_code` | `str` | Required | Postal Code / Zip Code. The postalCode must be valid for the address’s country code. US codes must be exactly 5 digits long. Canadian Postal Codes must be exactly 6 alphanumeric characters long. expression [0-9]{5}). (regular expression [0-9]{5}). example: '99501'<br><br>**Constraints**: *Pattern*: `^\d{5}$` |
| `postal_code_extension` | `str` | Optional | Postal Code / Zip Code Extension.  The postalCode extension must be valid for the address’s country code. US codes must be exactly 4 digits long (regular expression [0-9]{4}). Doesn't exist for Canadian submerchants.<br><br>**Constraints**: *Pattern*: `^\d{4}$` |

## Example (as JSON)

```json
{
  "title": "President",
  "firstName": "John",
  "middleInitial": "S",
  "lastName": "Smith",
  "phoneNumber": "5135551234",
  "phoneNumberExt": "5678",
  "faxNumber": "5135551234",
  "email": "jsmith@payfacsm.com",
  "ownershipPercentage": 51,
  "ssn": "123456789",
  "dob": "1948-12-05",
  "addressLine1": "123 South St",
  "addressLine2": "Apt 500",
  "city": "Anchorage",
  "state": "MD",
  "country": "US",
  "postalCode": "postalCode6",
  "postalCodeExtension": "1234"
}
```

