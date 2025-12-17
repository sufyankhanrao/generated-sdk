
# Team Login Response

## Structure

`TeamLoginResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `team` | `str` | Optional | The identifier of the Team resource that the Login identified in the 'login' field should be marked as part of. |
| `create` | [`CreateEnum`](../../doc/models/create-enum.md) | Optional | Create rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br> |
| `read` | [`TeamLoginReadEnum`](../../doc/models/team-login-read-enum.md) | Optional | Read rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br>**Default**: `0`<br> |
| `update` | [`UpdateEnum`](../../doc/models/update-enum.md) | Optional | Update rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br> |
| `delete` | [`DeleteEnum`](../../doc/models/delete-enum.md) | Optional | Delete rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br> |
| `reference` | [`ReferenceEnum`](../../doc/models/reference-enum.md) | Optional | Reference use rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br> |
| `team_admin` | [`TeamAdminEnum`](../../doc/models/team-admin-enum.md) | Optional | Team administration rights for this Login on this Team.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **None**<br>- `1` - **Allow**<br></details><br> |

## Example (as JSON)

```json
{
  "read": 0,
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

