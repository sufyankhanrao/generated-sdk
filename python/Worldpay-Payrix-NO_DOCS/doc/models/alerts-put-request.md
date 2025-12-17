
# Alerts Put Request

## Structure

`AlertsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The Login that owns this resource. |
| `forlogin` | `str` | Optional | The identifier of the Login that this Alert relates to.<br>The Alert is triggered based on the activity of this Login. |
| `team` | `str` | Optional | The identifier (ID) of the team that this Alert relates to. The Alert is triggered based on the activity of this Team. |
| `division` | `str` | Optional | The division for which this Alerts applies. |
| `partition` | `str` | Optional | The partition for which this Alerts applies. |
| `name` | `str` | Optional | The name of this Alert.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `description` | `str` | Optional | Description of Alerts. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "t1_log_61f2efc258eb7bf6d380000",
  "forlogin": "t1_log_61f2efc258eb7bf6d380000",
  "team": "t1_tem_67c202b908935b505104500",
  "division": "t1_div_67c56806728fbbf0bae0z00",
  "partition": "t1_ptn_666834d4d504f21414978f0",
  "name": "williamson",
  "description": "Used by the FrontDesk system to keep information up to date via webhook alerts",
  "inactive": 0,
  "frozen": 0
}
```

