
# Billing Events Response

## Structure

`BillingEventsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `billing` | `str` | Optional | The billing to which this billingEvent applies. |
| `event` | [`BillingEventEnum`](../../doc/models/billing-event-enum.md) | Optional | The type of event that triggers billing.<br><br><details><br><summary>Valid Values</summary><br>- `fees` - **Fee.** Fee events trigger the billing configuration.<br>- `chargebacks` - **Chargebacks.** Chargeback events trigger the billing configuration.<br>- `returns` - **Returns.** Return events trigger the billing configuration.<br>- `profitShares` - **Profit Shares.** Profit Sharing events trigger the billing configuration.<br>- `revShares` - **RevShares.** Rev Sharing events trigger the billing configuration.<br></details><br> |
| `event_schedule` | `str` | Optional | The record ID of a specific schedule for the event chosen for which the billing configuration applies, all other records of the same event are excluded. |
| `deduct_from_balance` | [`DeductFromBalanceEnum`](../../doc/models/deduct-from-balance-enum.md) | Optional | Whether to deduct the billing amount from the entity's account balance.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Do not deduct from balance.**<br>- `1` - **Deduct from balance.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier6"
}
```

