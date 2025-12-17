
# Teams Response

## Structure

`TeamsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this Team. |
| `name` | `str` | Optional | The name of this Team.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Team.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `auto_cascade_disabled` | [`AutoCascadeDisabledEnum`](../../doc/models/auto-cascade-disabled-enum.md) | Optional | Whether new Logins created by member Logins of this Team will be added to this team or not. Default is 0 (enabled).<br><br><details><br><summary>Valid Values</summary> <br>- `0` - **Disabled**<br>- `1` - **Enabled**<br><br> </details><br> |
| `auto_cascade_owner` | [`AutoCascadeOwnerEnum`](../../doc/models/auto-cascade-owner-enum.md) | Optional | An integer-boolean indicating whether or not the cascading functionality should extend to the owner of this team.<br><br><details><br><summary>Valid Values</summary> <br>- `0` - **OFF**<br>- `1` - **ON**<br><br> </details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

