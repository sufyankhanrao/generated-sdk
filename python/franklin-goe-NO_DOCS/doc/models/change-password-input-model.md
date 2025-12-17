
# Change Password Input Model

*This model accepts additional fields of type Any.*

## Structure

`ChangePasswordInputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | Email of the user for change password. |
| `old_password` | `str` | Required | oldPassword for password change. |
| `new_password` | `str` | Required | newPassword which will be used from now. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "email": "abc@abc.com",
  "oldPassword": "oldpass@#&7",
  "newPassword": "newpass@#&7",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

