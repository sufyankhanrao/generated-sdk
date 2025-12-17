
# Subscription Tokens Post Request

## Structure

`SubscriptionTokensPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | `str` | Required | The identifier of the Subscription resource that this Subscription Token is associated with. This is the Subscription that the Token identified in the 'token' field of this resource is responsible for paying for. |
| `token` | `str` | Required | The identifier of the Token resource that this Subscription Token is associated with. This resource identifies the means of payment for the Subscription identified in the 'subscription' field of this resource. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "subscription": "p1_sbn_5a1ef5e556583e67e5d55a2",
  "token": "ae1abb3aaa18e4c374ca83fa75a7fff6",
  "inactive": 0,
  "frozen": 0
}
```

