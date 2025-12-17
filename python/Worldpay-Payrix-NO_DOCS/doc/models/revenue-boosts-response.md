
# Revenue Boosts Response

## Structure

`RevenueBoostsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that networkPaymentManager is associated with. |
| `platform` | [`Platform3Enum`](../../doc/models/platform-3-enum.md) | Optional | The platform used to process this transaction.<br>Valid Values :  - `VCORE` - **VCORE** |
| `org` | `str` | Optional | The identifier of the Org (group) that networkPaymentManager is associated with. |
| `division` | `str` | Optional | The identifier of the Division that networkPaymentManager is associated with. |
| `partition` | `str` | Optional | The identifier of the Partition that networkPaymentManager is associated with. |
| `enablement_date` | `str` | Optional | The Date and time when an entity was enabled for networkPaymentManager. The date is specified as an eight digit string in YYYY-MM-DD hh:mm:ss format, for example, '2023-06-01 01:00:00' for June 01, 2023. 1:00 am.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `enable_revenue_boost` | [`EnableRevenueBoostEnum`](../../doc/models/enable-revenue-boost-enum.md) | Optional | Flag to depict if entity was enabled for networkPaymentManager.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **NotEnabled.**<br>- `1` - **Enabled.**<br></details><br> |
| `resource_id` | `str` | Optional | The identifier of the record created/updated in the original request. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `deleted` | `str` | Optional | The date and time at which this resource was deleted.\nThe date is specified as an eight digit string in YYYY-MM-DD hh:mm:ss format, for example, '2023-06-01 01:00:00' for June 01, 2023. 1:00 am.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `deleter` | `str` | Optional | The id of user who deleted the revenueBoost entity. |

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

