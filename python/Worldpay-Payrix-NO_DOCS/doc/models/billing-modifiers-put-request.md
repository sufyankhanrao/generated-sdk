
# Billing Modifiers Put Request

## Structure

`BillingModifiersPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing` | `str` | Optional | The identifier of the Billing that this Billing Modifier applies to. |
| `entity` | `str` | Optional | The identifier of the Entity that this Billing Modifier applies to. |
| `org` | `str` | Optional | The identifier of the Org that this Billing Modifier applies to. |
| `division` | `str` | Optional | The identifier of the Division that this Billing Modifier applies to. |
| `partition` | `str` | Optional | The identifier of the Partition that this Billing Modifier applies to. |
| `fromentity` | `str` | Optional | The identifier of the Entity that is responsible for paying this Bill on behalf of the Entity specified in the 'entity' field. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "billing": "t1_bil_67d9c8a7df33cf77a3e5e4a",
  "entity": "t1_ent_5cd987a735c33bab09e7570",
  "org": "t1_org_67d9c6a866e5d47dca276c3",
  "division": "t1_div_67c56806728fbbf0bae0b00",
  "partition": "t1_ptn_666834d4d504f21414970z0",
  "fromentity": "t1_ent_67d851660b5836731a89ee3",
  "inactive": 0,
  "frozen": 0
}
```

