
# Orgs VAS Pinless Debit Conversions Put Request

## Structure

`OrgsVASPinlessDebitConversionsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org` | `str` | Optional | The identifier of the Org (group) that OrgsVASPinlessDebitConversions is associated to. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "org": "t1_org_680bfd2cea2729081810000",
  "inactive": 0,
  "frozen": 0
}
```

