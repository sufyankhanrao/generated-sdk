
# Profit Shares Response

## Structure

`ProfitSharesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the Login that owns this ProfitShare. |
| `entity` | `str` | Optional | The identifier of the Entity that this ProfitShare refers to. This is the entity that will receive the split income/expense. |
| `forentity` | `str` | Optional | The identifier of the Entity that will have it's earnings/expenses shared. |
| `org` | `str` | Optional | The identifier of the Org in which entities will have their earnings/expenses shares. |
| `division` | `str` | Optional | The identifier of the Division in which entities will have their earnings/expenses shares. |
| `partition` | `str` | Optional | The identifier of the Partition in which entities will have their earnings/expenses shares. |
| `mtype` | [`ProfitShareTypeEnum`](../../doc/models/profit-share-type-enum.md) | Optional | Indicates if the Profit Share should be processed when there is an income, expense, or both.<br><br><details><br><summary>Valid Values</summary><br>- `income` - **Profit Share processing for income-only.**<br>- `expense` - **Profit Share processing for expense-only.**<br>- `both` - **Profit Share processing for both income and expense.**<br></details><br> |
| `name` | `str` | Optional | The name of this ProfitShare.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this ProfitShare.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `amount` | `int` | Optional | The percentage to be shared.<br>This field is specified as an integer between 1 and 10000.<br>Percentages are calculated over the income/expense amount. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier2"
}
```

