
# Contact

The Contact.

## Structure

`Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | Contact's first name.<br><br>**Constraints**: *Maximum Length*: `20` |
| `last_name` | `str` | Optional | Contact's last name.<br><br>**Constraints**: *Maximum Length*: `20` |
| `email` | `str` | Optional | Contact's email address.<br><br>**Constraints**: *Maximum Length*: `100` |
| `phone_number` | `str` | Optional | Contact's phone.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "first_name": "Jeffery",
  "last_name": "Todd",
  "email": "jtodd@example.com",
  "phone_number": "555-555-3456"
}
```

