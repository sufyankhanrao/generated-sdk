
# Team Login Post Request

## Structure

`TeamLoginPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The Login that owns this resource. |
| `team` | `str` | Required | The identifier of the Team resource that the Login identified in the 'login' field should be marked as part of. |
| `create` | [`CreateEnum`](../../doc/models/create-enum.md) | Required | Create rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `read` | [`TeamLoginReadEnum`](../../doc/models/team-login-read-enum.md) | Required | Read rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `update` | [`UpdateEnum`](../../doc/models/update-enum.md) | Required | Update rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `delete` | [`DeleteEnum`](../../doc/models/delete-enum.md) | Required | Delete rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `reference` | [`ReferenceEnum`](../../doc/models/reference-enum.md) | Required | Reference use rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `team_admin` | [`TeamAdminEnum`](../../doc/models/team-admin-enum.md) | Required | Team administration rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "t1_log_6802c54cba888f6abfd88cc",
  "team": "t1_tem_6621af6c10f4a29427a2d35",
  "create": 0,
  "read": 0,
  "update": 0,
  "delete": 0,
  "reference": 0,
  "teamAdmin": 0
}
```

