
# Additional Contact

This aggregate field includes details of contacts

## Structure

`AdditionalContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | First name. Region based validations will be applied to this field.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `15`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `middle_initial` | `str` | Optional | Middle initial.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `last_name` | `str` | Required | Last name. Region based validations will be applied to this field.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `phone_number` | `str` | Optional | 10-digit phone number of the format  5131234567.<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{10}$` |
| `phone_number_ext` | `str` | Optional | Phone number extension. Up to 8 digits of the format 12345678.<br><br>**Constraints**: *Maximum Length*: `8`, *Pattern*: `([0-9]{8})$` |
| `email` | `str` | Required | Email address of the contact. Must have @ and a .<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `(\\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\\.)+[A-Za-z0-9]{2,}\\b{0,64})` |
| `fax_number` | `str` | Optional | 10-digit fax number of the format 5131234567<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9]{10}$` |

## Example (as JSON)

```json
{
  "firstName": "John",
  "middleInitial": "M",
  "lastName": "Doe",
  "phoneNumber": "5139004357",
  "phoneNumberExt": "12345678",
  "email": "email0",
  "faxNumber": "5139003344"
}
```

