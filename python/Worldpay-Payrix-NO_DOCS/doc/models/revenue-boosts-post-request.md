
# Revenue Boosts Post Request

A request body for creating new networkPaymentManager

## Structure

`RevenueBoostsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | `str` | Required | The identifier of the Entity that networkPaymentManager is associated with. |
| `platform` | `str` | Required, Constant | The platform used to process this transaction.<br>Valid Values : - `VCORE` - **VCORE**<br><br>**Value**: `'VCORE'` |
| `org` | `str` | Optional | The identifier of the Org (group) that networkPaymentManager is associated with. |
| `division` | `str` | Optional | The identifier of the Division that networkPaymentManager is associated with. |
| `partition` | `str` | Optional | The identifier of the Partition that networkPaymentManager is associated with. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "entity": "t1_ent_5a1pf5a1234531155a12345",
  "platform": "VCORE",
  "org": "t1_org_5a1pf5a1234531155a12345",
  "division": "t1_div_67b51635da21f7399ce2af1",
  "partition": "t1_ptn_666834d4d504f11234578f5",
  "inactive": 0,
  "frozen": 0
}
```

