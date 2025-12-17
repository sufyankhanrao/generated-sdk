
# Primary Principal

The Primary Principal.

## Structure

`PrimaryPrincipal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | Signer's first name<br><br>**Constraints**: *Maximum Length*: `20` |
| `last_name` | `str` | Optional | Signer's last name<br><br>**Constraints**: *Maximum Length*: `20` |
| `middle_name` | `str` | Optional | Signer's middle name<br><br>**Constraints**: *Maximum Length*: `20` |
| `title` | `str` | Optional | Signer's title<br><br>**Constraints**: *Maximum Length*: `20` |
| `date_of_birth` | `str` | Optional | Signer's date of birth<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `address_line_1` | `str` | Optional | Signer's residential address line 1<br><br>**Constraints**: *Maximum Length*: `100` |
| `address_line_2` | `str` | Optional | Signer's residential address line 2<br><br>**Constraints**: *Maximum Length*: `20` |
| `city` | `str` | Optional | Signer's city<br><br>**Constraints**: *Maximum Length*: `50` |
| `state_province` | `str` | Optional | Signer's two-digit state code<br><br>**Constraints**: *Maximum Length*: `2` |
| `postal_code` | `str` | Optional | Signer's postal code<br><br>**Constraints**: *Maximum Length*: `10` |
| `ssn` | `str` | Optional | Last four digits of the primary principal or Signer's social security number<br><br>**Constraints**: *Maximum Length*: `4` |
| `ownership_percent` | `int` | Optional | Percentage of business owned by primary principal or signer<br><br>**Constraints**: `>= 0`, `<= 100` |
| `phone_number` | `str` | Optional | Signer's phone number<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "first_name": "Bob",
  "last_name": "Fairview",
  "middle_name": "Nathaniel",
  "title": "Dr",
  "date_of_birth": "2021-12-01",
  "address_line_1": "1354 Oak St.",
  "address_line_2": "Unit 203",
  "city": "Dover",
  "state_province": "DE",
  "postal_code": "55022",
  "ownership_percent": 100,
  "phone_number": "555-555-1234"
}
```

