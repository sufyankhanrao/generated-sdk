
# Teams Put Request

## Structure

`TeamsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
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
  "login": "t1_log_6801559c6218199cb0820df",
  "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
  "description": "Esmeralda McCullough Team",
  "autoCascadeDisabled": 0,
  "autoCascadeOwner": 0,
  "inactive": 0,
  "frozen": 0
}
```

