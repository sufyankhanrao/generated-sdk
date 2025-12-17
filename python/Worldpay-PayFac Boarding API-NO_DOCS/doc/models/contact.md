
# Contact

## Structure

`Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Title of the Contact.<br><br>**Constraints**: *Maximum Length*: `40` |
| `first_name` | `str` | Required | First Name of the Contact<br><br>**Constraints**: *Maximum Length*: `15` |
| `middle_initial` | `str` | Optional | Middle Initial of the Contact<br><br>**Constraints**: *Maximum Length*: `1` |
| `last_name` | `str` | Required | Last Name of the Contact<br><br>**Constraints**: *Maximum Length*: `25` |
| `phone_number` | `str` | Required | Phone Number of the Contact. 10 digt number of the format 5131234567<br><br>**Constraints**: *Pattern*: `^\d{10}$` |
| `phone_number_ext` | `str` | Optional | Phone Number Extension of the Contact<br><br>**Constraints**: *Maximum Length*: `8` |
| `email` | `str` | Required | Email address of the contact. Must have @ and a .<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: ``^[a-zA-Z0-9.!#$%&’*+=?^_`{\|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$`` |
| `fax_number` | `str` | Optional | Fax Number of the Contact. Must be 10 digit number of the format 5131234567<br><br>**Constraints**: *Pattern*: `^\d{10}$` |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Required | Required. Type of Sub-Merchant Contact.   1) Only CustomerService Contact is mandatory. It could be same as any Owner Contact information.  2) For Customer Service Contact, firstName, lastName, phoneNumber and email are mandatory during POST.   3) For all other contact types, firstName and lastName are mandatory during POST. |

## Example (as JSON)

```json
{
  "title": "Relationship Manager",
  "firstName": "Jane",
  "middleInitial": "S",
  "lastName": "Smith",
  "phoneNumber": "5135559876",
  "phoneNumberExt": "5432",
  "email": "jasmith@payfacsm.com",
  "faxNumber": "5135559876",
  "type": "Primary"
}
```

