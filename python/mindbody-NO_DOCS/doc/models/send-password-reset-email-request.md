
# Send Password Reset Email Request

Request to send a password reset email to a user

## Structure

`SendPasswordResetEmailRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_email` | `str` | Required | The user’s email address. The software uses this parameter as the username. |
| `user_first_name` | `str` | Required | The user’s first name. The software uses this parameter to verify the user. |
| `user_last_name` | `str` | Required | The user’s last name. The software uses this parameter to verify the user. |

## Example (as JSON)

```json
{
  "UserEmail": "UserEmail6",
  "UserFirstName": "UserFirstName0",
  "UserLastName": "UserLastName6"
}
```

