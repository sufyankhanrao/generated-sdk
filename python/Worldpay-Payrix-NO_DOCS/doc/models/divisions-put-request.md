
# Divisions Put Request

## Structure

`DivisionsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The Login that owns this resource. |
| `name` | `str` | Optional | The name of the division, which may be used for some white-label purposes. |
| `email` | `str` | Optional | The white-labeled outgoing email for all automated emails generated throughout this division. |
| `change_management_enabled` | [`ChangeManagementEnabledEnum`](../../doc/models/change-management-enabled-enum.md) | Optional | <details><br><summary>Valid Values</summary> <br>- `0` - **Enabled.**<br>- `1` - **Disabled.**<br><br> </details><br> |
| `min_password_length` | `int` | Optional | Limit for password validations length. |
| `min_password_complexity` | [`MinPasswordComplexityEnum`](../../doc/models/min-password-complexity-enum.md) | Optional | Complexity that the password must have. How many of this types needs to include: lowercase, uppercase, number and symbols.<br><br><details><br><summary>Valid Values</summary> <br>- `1` - **Needs to include one type**<br>- `2` - **Needs to include two type**<br><br>- `3` - **Needs to include three type**<br><br>- `4` - **Needs to include four type**<br><br> </details><br> |

## Example (as JSON)

```json
{
  "login": "t1_log_67e150467ee225924163f18",
  "name": "sampleDivision",
  "email": "testuse1@example.com",
  "changeManagementEnabled": 0,
  "minPasswordLength": 9,
  "minPasswordComplexity": 1
}
```

