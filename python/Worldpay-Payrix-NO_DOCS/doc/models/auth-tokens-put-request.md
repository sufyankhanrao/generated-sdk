
# Auth Tokens Put Request

## Structure

`AuthTokensPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `used` | `int` | Optional | Timestamp of when the AuthToken was used. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "used": 202503141414,
  "inactive": 0,
  "frozen": 0
}
```

