
# Plans Response

## Structure

`PlansResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `merchant` | `str` | Optional | The identifier of the Merchant associated with this Plan. |
| `billing` | `str` | Optional | The attached billing for which recurring payments should be made to pay off statements. |
| `mtype` | [`PlanTypeEnum`](../../doc/models/plan-type-enum.md) | Optional | The type of plan.<br><br><details><br><summary>Valid Values</summary><br>- `recurring` - **A recurring payment plan (subcription).**<br>- `installment`  - **A deferred payment installment plan.**<br><br></details><br> |
| `name` | `str` | Optional | The name of this Plan.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Plan.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `txn_description` | `str` | Optional | The description of the Txn that will be created through this Plan. |
| `order` | `str` | Optional | The order of the Txn that will be created through this Plan. |
| `schedule` | [`PlanScheduleEnum`](../../doc/models/plan-schedule-enum.md) | Optional | The schedule that determines when the subscription related to this Plan is triggered.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Daily**<br>- `2` - **Weekly**<br>- `3` - **Monthly**<br>- `4` - **Annually**<br></details><br> |
| `schedule_factor` | `int` | Optional | A multiplier that you can use to adjust the schedule set in the 'schedule' field, such as daily, weekly, monthly, or annually.<br>This field is specified as an integer and its value determines how the interval is multiplied. |
| `um` | [`PlanUmEnum`](../../doc/models/plan-um-enum.md) | Optional | The unit of measure for the amount on the plan.<br><br><details><br><summary>Valid Values</summary><br>- `actual` - **An actual amount to charge, in cents.**<br>- `percent` - **A percentage of another amount, in basis points.**<br></details><br>**Default**: `"actual"`<br> |
| `amount` | `int` | Optional | The amount to charge with each payment under this Plan.<br>This field is specified as an integer in cents. |
| `max_failures` | `int` | Optional | The maximum consecutive amount of payment failures to allow for a subscription before inactivating it. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "um": "actual",
  "inactive": 0,
  "frozen": 0,
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

