
# Billings Response

## Structure

`BillingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `entity` | `str` | Optional | The alphanumeric identifier of the Entity associated with this Account. |
| `forentity` | `str` | Optional | The alphanumeric identifier of the Entity associated with this Account. |
| `org` | `str` | Optional | The identifier of the Org associated with this invoiceParameter. |
| `division` | `str` | Optional | ID of the division associated with this vendor |
| `partition` | `str` | Optional | The identifier of the Partition associated with this invoiceParameter. |
| `description` | `str` | Optional | The billing details. |
| `schedule` | [`BillingScheduleEnum`](../../doc/models/billing-schedule-enum.md) | Optional | The schedule that determines when this Billing is triggered to start collecting data.<br><br><details><br><summary>Valid Values</summary><br>- `days` - **Daily schedule.**<br>- `weeks` - **Weekly schedule.**<br>- `months` - **Monthly schedule.**<br>- `years` - **Annual schedule.**<br></details><br> |
| `schedule_factor` | `int` | Optional | A multiplier that you can use to adjust the schedule set in the 'schedule' field, if it is set to a duration-based trigger, such as daily, weekly, monthly, or annually.<br>This field is specified as an integer and its value determines how the interval is multiplied. |
| `start` | `int` | Optional | The date on which this Billing period should start. |
| `finish` | `int` | Optional | The date on which this Billing period should end. |
| `collection_factor` | [`CollectionFactorEnum`](../../doc/models/collection-factor-enum.md) | Optional | A multiplier that you can use to adjust the set of data to be used in the collection calculation.<br><br><details><br><summary>Valid Values</summary><br>- `days` - **Days.** Multiplier based on days.<br>- `weeks` - **Weeks.** Multiplier based on weeks.<br>- `months` - **Months.** Multiplier based on months.<br>- `years` - **Years.** Multiplier based on years.<br></details><br> |
| `collection_offset` | `int` | Optional | The number of days, weeks, months or years to go back when selecting data for collection calculation. |
| `collection_include_current` | [`CollectionIncludeCurrentEnum`](../../doc/models/collection-include-current-enum.md) | Optional | Whether to include the current period in the collection calculation.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Exclude Current Period.** Do not include the current period in the calculation.<br>- `1` - **Include Current Period.** Include the current period in the calculation.<br></details><br> |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of the amount in this billing. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `collection` | [`BillingCollectionEnum`](../../doc/models/billing-collection-enum.md) | Optional | Determines who will be billed.<br><br><details><br><summary>Valid Values</summary><br>- `entity` - **The entity will be billed.**<br></details><br>**Default**: `"entity"`<br> |

## Example (as JSON)

```json
{
  "currency": "USD",
  "inactive": 0,
  "frozen": 0,
  "collection": "entity",
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier8"
}
```

