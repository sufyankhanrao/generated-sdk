
# User Creation

The parameters used to create a user

## Structure

`UserCreation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | First name of the account user |
| `last_name` | `str` | Required | Last name of account user |
| `email_id` | `str` | Required | Email address of account user |
| `user_role` | [`UserRolesEnum`](../../doc/models/user-roles-enum.md) | Required | - |
| `active` | `bool` | Required | Choose whether to activate this account immediately on creation<br><br>**Default**: `True` |
| `send_mail_for_password_reset` | `bool` | Required | Choose whether to send the user an email to reset his password upon user creation<br><br>**Default**: `True` |
| `allow_advanced_email_validation` | `bool` | Optional | Choose whether to validate the user's email address when creating this account<br><br>**Default**: `False` |
| `address` | `str` | Optional | The location of this account user |
| `department` | `str` | Optional | Department of the user |
| `title` | `str` | Optional | Designation/Title of account user |
| `manager_id` | `str` | Optional | The ID of one of the Admins or Super-Admins from your account, which will act as manager for this user |
| `login_password` | `str` | Optional | The initial  password for this user, it can be combination of Uppercase/Lowercase letters, numbers and special characters |

## Example (as JSON)

```json
{
  "firstName": "eSign",
  "lastName": "Demo",
  "emailId": "esigndemo@foxitsoftware.com",
  "allowAdvancedEmailValidation": true,
  "address": "Miami, Florida",
  "userRole": "admin",
  "department": "DEV",
  "title": "Tech Lead",
  "active": true,
  "loginPassword": "TXxgjjezFLAqnR",
  "sendMailForPasswordReset": true,
  "managerId": "managerId8"
}
```

