
# Divisions Response 1

## Structure

`DivisionsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The login ID of the user that owns this division record |
| `name` | `str` | Optional | The name of the division, which may be used for some white-label purposes |
| `email` | `str` | Optional | The white-labeled outgoing email for all automated emails generated throughout this division |
| `change_management_enabled` | [`ChangeManagementEnabledEnum`](../../doc/models/change-management-enabled-enum.md) | Optional | Whether change request management is enabled <details> <summary>Valid Values</summary><br><br>- `0` - **Disabled.** - `1` - **Enabled.** </details> |
| `min_password_length` | `int` | Optional | Minimum password length |
| `min_password_complexity` | [`MinPasswordComplexityEnum`](../../doc/models/min-password-complexity-enum.md) | Optional | Password Complexity <details> <summary>Valid Values</summary><br><br>- `1` - **Needs to include one type.** - `2` - **Needs to include two types.** - `3` - **Needs to include three types.** - `4` - **Needs to include the four types.** </details> |
| `can_use_plaid_wrapper_microservice` | [`CanUsePlaidWrapperMicroserviceEnum`](../../doc/models/can-use-plaid-wrapper-microservice-enum.md) | Optional | Describes if the user can use the Plaid Wrapper Microservice or not<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No.**<br>- `1` - **Yes.**<br></details><br> |
| `simplified_deposit_enabled` | [`SimplifiedDepositEnabledEnum`](../../doc/models/simplified-deposit-enabled-enum.md) | Optional | Allows automatic enablement of simplified deposits for new boardings and allows enablement of existing boardings. Restricted to admin.<br>Valid Values :  - `1` - **Enabled** |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified2",
  "creator": "String9",
  "modifier": "modifier6"
}
```

