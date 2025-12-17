
# User Update

The parameters used to update a user

## Structure

`UserUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `party_id` | `str` | Required | the unique party id for the user to be updated |
| `first_name` | `str` | Required | First name of the account user |
| `last_name` | `str` | Required | Last name of account user |
| `user_role` | [`UserRolesEnum`](../../doc/models/user-roles-enum.md) | Required | - |
| `active` | `bool` | Required | Choose whether to activate this account immediately on creation<br><br>**Default**: `True` |
| `address` | `str` | Optional | The location of this account user |
| `department` | `str` | Optional | Department of the user |
| `title` | `str` | Optional | Designation/Title of account user |
| `manager_id` | `str` | Optional | The ID of one of the Admins or Super-Admins from your account, which will act as manager for this user |

## Example (as JSON)

```json
{
  "partyId": "54",
  "firstName": "eSign",
  "lastName": "Demo",
  "address": "Miami, Florida",
  "userRole": "super_admin",
  "department": "DEV",
  "title": "Tech Lead",
  "active": false,
  "managerId": "managerId2"
}
```

