
# Owner

Array of merchant owners.

## Structure

`Owner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | Owner's first name.<br><br>**Constraints**: *Maximum Length*: `20` |
| `last_name` | `str` | Required | Owner's last name.<br><br>**Constraints**: *Maximum Length*: `20` |
| `middle_name` | `str` | Optional | Owner's middle name.<br><br>**Constraints**: *Maximum Length*: `20` |
| `title` | `str` | Required | Owner's title.<br><br>**Constraints**: *Maximum Length*: `20` |
| `date_of_birth` | `str` | Required | Owner's date of birth.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `address_line_1` | `str` | Required | Owner's street address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `address_line_2` | `str` | Required | Line 2 of owner's address.<br><br>**Constraints**: *Maximum Length*: `20` |
| `city` | `str` | Required | Owner's address city.<br><br>**Constraints**: *Maximum Length*: `50` |
| `state_province` | `str` | Required | Owner's address state/province.<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Required | Owner's address postal code.<br><br>**Constraints**: *Maximum Length*: `10` |
| `country_code` | `str` | Required | Owner's address country.<br><br>**Constraints**: *Maximum Length*: `2` |
| `ssn` | `str` | Required | Owner's full SSN.<br><br>**Constraints**: *Maximum Length*: `10` |
| `ownership_percent` | `int` | Required | Owner's ownership percent.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `phone_number` | `str` | Required | Owner's phone number.<br><br>**Constraints**: *Maximum Length*: `20` |
| `email_address` | `str` | Required | Owner's email address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `is_controller` | `bool` | Required | Flag indicating whether this owner is the control owner. Maximum of 1 owner can be marked as control.. |
| `is_signer` | `bool` | Required | Flag indicating whether or not the owner is a signer for the business. Maximum of 1 owner can be marked as signer. |

## Example (as JSON)

```json
{
  "first_name": "James",
  "last_name": "Bond",
  "middle_name": "Tyler",
  "title": "CEO",
  "date_of_birth": "2021-12-01",
  "address_line_1": "133 S Goliad St",
  "address_line_2": "Suite 120",
  "city": "Rockwall",
  "state_province": "TX",
  "postal_code": "75429",
  "country_code": "US",
  "ssn": "000000000",
  "ownership_percent": 100,
  "phone_number": "9042142323",
  "email_address": "james@example.com",
  "is_controller": true,
  "is_signer": true
}
```

