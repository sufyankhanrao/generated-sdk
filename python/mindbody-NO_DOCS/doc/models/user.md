
# User

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The user’s ID at the business. This is always 0 for Admin and Owner type users. |
| `first_name` | `str` | Optional | The user’s first name. |
| `last_name` | `str` | Optional | The user’s last name. |
| `mtype` | `str` | Optional | The user’s type. Possible values are:<br><br>* Staff<br>* Owner<br>* Admin |

## Example (as JSON)

```json
{
  "Id": 116,
  "FirstName": "FirstName8",
  "LastName": "LastName2",
  "Type": "Type6"
}
```

