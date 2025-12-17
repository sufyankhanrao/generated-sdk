
# Orgs VAS Efe Products Put Request

## Structure

`OrgsVASEfeProductsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org` | `str` | Optional | The identifier of the Org (group) that orgsVASEfeProducts is associated to. |
| `product` | [`Product3Enum`](../../doc/models/product-3-enum.md) | Optional | This field contains the product type of the orgsVASEfeProducts. |
| `contract_type` | `str` | Optional | The Contract type details related to the Embedded Finance product. |
| `platform` | [`PlatformEnum`](../../doc/models/platform-enum.md) | Optional | The Platform to which orgsVASEfeProducts should be applied. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "org": "t1_org_6862c1211b366bbfe87657c",
  "product": "merchantWorkingCapital",
  "contractType": "{\"residualFeeType\": \"rev_share\"}",
  "platform": "PARAFIN",
  "inactive": 0,
  "frozen": 0
}
```

