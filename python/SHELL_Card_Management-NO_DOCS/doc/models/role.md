
# Role

## Structure

`Role`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_name` | `str` | Optional | Role Name of the user |
| `is_customer_admin` | `bool` | Optional | Whether the role is an administrator.<br><br>**Default**: `True` |
| `is_customer_user` | `bool` | Optional | Whether the role is a customer user.<br><br>**Default**: `False` |
| `is_shell_admin` | `bool` | Optional | True if the role is Shell user, else false.<br><br>**Default**: `False` |
| `is_service_account` | `bool` | Optional | True/False.<br>True if the role is Service accounts, else false.<br><br>**Default**: `False` |
| `is_user_admin` | `bool` | Optional | True/False.<br>True, if the role allows user administration, else false.<br><br>**Default**: `True` |

## Example (as JSON)

```json
{
  "RoleName": "FleetManager",
  "IsCustomerAdmin": true,
  "IsCustomerUser": false,
  "IsShellAdmin": false,
  "IsServiceAccount": false,
  "IsUserAdmin": true
}
```

