
# Embedded Finance Post Request

## Structure

`EmbeddedFinancePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enablement_date` | `str` | Optional | The Date and time when an entity was enabled for embeddedFinance.\nThe date is specified as an eight digit string in YYYY-MM-DD hh:mm:ss format, for example, '2023-06-01 01:00:00' for June 01, 2023. 1:00 am.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `product` | [`ProductEnum`](../../doc/models/product-enum.md) | Optional | The Product type to which embeddedFinance belongs to. |
| `platform` | [`PlatformEnum`](../../doc/models/platform-enum.md) | Optional | The Platform to which embeddedFinance should be applied. |
| `entity` | `str` | Optional | The identifier of the Entity that this embeddedFinance is associated to. |
| `org` | `str` | Optional | The identifier of the Org (group) that embeddedFinance is associated to. |
| `division` | `str` | Optional | The identifier of the Division that embeddedFinance  is associated to. |
| `partition` | `str` | Optional | The identifier of the Partition that embeddedFinance is associated to. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `product_contract` | `str` | Optional | TBD |
| `accumulated_loan_total` | `str` | Optional | TBD |

## Example (as JSON)

```json
{
  "enablementDate": "2023-06-01 01:00:00",
  "product": "merchantWorkingCapital",
  "platform": "PARAFIN",
  "entity": "t1_ent_685d27bc1611a5c48c0000f",
  "org": "t1_org_685d27bd878c0a8cf00ad0c",
  "division": "t1_div_67b51635da21f7399ce2af1",
  "partition": "t1_ptn_666834d4d504f11234578f0",
  "inactive": 0,
  "frozen": 0
}
```

