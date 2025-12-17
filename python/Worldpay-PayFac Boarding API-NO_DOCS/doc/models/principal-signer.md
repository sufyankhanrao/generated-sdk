
# Principal Signer

Principal Signer for eCheck.This information is "required" for the Signer of the ACH Merchant Agreement to satisfy KYC regulations. If you do not complete these fields, your ACH Merchant Account may be subject to suspension. If you have any questions or concerns, please contact your Relationship Manager.

## Structure

`PrincipalSigner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Required | Title of the Principal Signer. This is “required” to confirm the Signer has the authority to execute the ACH Merchant Agreement on behalf of the Company. Examples can be President, CEO, CFO, CTO or Owner.”<br><br>**Constraints**: *Maximum Length*: `40` |
| `first_name` | `str` | Required | First Name of the Principal Signer<br><br>**Constraints**: *Maximum Length*: `15` |
| `middle_initial` | `str` | Optional | Middle Initial of the Principal Signer<br><br>**Constraints**: *Maximum Length*: `1` |
| `last_name` | `str` | Required | Last Name of the Principal Signer<br><br>**Constraints**: *Maximum Length*: `25` |
| `dob` | `date` | Required | Principal Signer's Date of Birth. |
| `ownership_percentage` | `int` | Required | Principal Signer's Ownership Percentage.<br><br>**Constraints**: `>= 1`, `<= 100` |
| `email` | `str` | Required | Email address of the Principal Signer. Must have @ and a .<br><br>**Constraints**: *Maximum Length*: `64` |
| `address_line_1` | `str` | Required | Address Line 1. Field for House Number, Street and Direction<br><br>**Constraints**: *Maximum Length*: `40` |
| `address_line_2` | `str` | Optional | Address Line 2. Field for Apt No, Suite No etc.<br><br>**Constraints**: *Maximum Length*: `40` |
| `city` | `str` | Required | **Constraints**: *Maximum Length*: `28` |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Required | Only valid US state codes (including Puerto Rico, Guam and Virgin Islands), Canadian province codes and Military state codes (AE - Armed Forces Africa, Canada, Europe, Middle East; AA - Armed Forces Americas (except Canada) ; AP - Armed Forces Pacific) are allowed |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Required | Only USA and Canada is allowed now. |
| `postal_code` | `str` | Required | Postal Code / Zip Code. The postalCode must be valid for the address’s country code. US codes must be exactly 5 digits long (regular expression [0-9]{5}). Canadian Postal Codes must be exactly 6 alphanumeric characters long.<br><br>**Constraints**: *Pattern*: `^\d{5}$` |
| `postal_code_extension` | `str` | Optional | Postal Code / Zip Code Extension.  The postalCode extension must be valid for the address’s country code. US codes must be exactly 4 digits long (regular expression [0-9]{4}). Does not exist for Canadian submerchants.<br><br>**Constraints**: *Pattern*: `^\d{4}$` |
| `phone_number` | `str` | Required | Phone Number of the Principal Signer. 10 digt number of the format 5131234567<br><br>**Constraints**: *Pattern*: `^\d{10}$` |
| `phone_number_ext` | `str` | Optional | Phone Number Extension of the Principal Signer<br><br>**Constraints**: *Maximum Length*: `8` |
| `ssn` | `str` | Optional | Principal Signer's SSN.<br><br>**Constraints**: *Pattern*: `^\d{9}$` |
| `driver_license_number` | `str` | Optional | Driver's License Number of the Principal Signer<br><br>**Constraints**: *Maximum Length*: `40` |
| `driver_license_state` | [`DriverLicenseStateEnum`](../../doc/models/driver-license-state-enum.md) | Optional | State in which ID has been issued. Only valid US state codes (including Puerto Rico, Guam and Virgin Islands), Canadian province codes and Military state codes (AE - Armed Forces Africa, Canada, Europe, Middle East; AA - Armed Forces Americas (except Canada) ; AP - Armed Forces Pacific) are allowed |

## Example (as JSON)

```json
{
  "title": "President",
  "firstName": "John",
  "middleInitial": "S",
  "lastName": "Smith",
  "dob": "1948-12-05",
  "ownershipPercentage": 51,
  "email": "jsmith@payfacsm.com",
  "addressLine1": "123 South St",
  "addressLine2": "Apt 500",
  "city": "Anchorage",
  "state": "PA",
  "country": "US",
  "postalCode": "99501",
  "postalCodeExtension": "1234",
  "phoneNumber": "5135551234",
  "ssn": "123456789",
  "driverLicenseNumber": "1234567",
  "phoneNumberExt": "phoneNumberExt2"
}
```

