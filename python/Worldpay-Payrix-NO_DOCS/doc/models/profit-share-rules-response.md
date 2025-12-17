
# Profit Share Rules Response

## Structure

`ProfitShareRulesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `profit_share` | `str` | Optional | The identifier of the ProfitShare that this ProfitShare Rule applies to. |
| `name` | `str` | Optional | The name of this ProfitShare Rule.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | Description of the Profit Share Rules. |
| `mtype` | [`ProfitShareRuleTypeEnum`](../../doc/models/profit-share-rule-type-enum.md) | Optional | The type of logic to apply with this ProfitShare Rule.<br><br><details><br><summary>Valid Values</summary><br>- `less` - **The ProfitShare applies only if the entry amount is lower than the amount set in the 'value' field of the ProfitShare Rule.**<br>- `equal` - **The ProfitShare applies only if the entry amount is exactly the same as the amount set in the 'value' field of the ProfitShare Rule.**<br>- `notEqual` - **The ProfitShare applies only if the entry amount is not exactly equal to the amount set in the 'value' field of the ProfitShare Rule.**<br>- `greater` - **The ProfitShare applies only if the entry amount is higher than the amount set in the 'value' field of the ProfitShare Rule.**<br>- `event` - **The ProfitShare applies only if the entry event is exactly the same as the event set in the 'value' field of the ProfitShare Rule.**<br>- `notEvent` - **The ProfitShare applies only if the entry event is not exactly equal to the event set in the 'value' field of the ProfitShare Rule.**<br>- `fee` - **The ProfitShare applies only if the entry fee is exactly the same as the fee set in the 'value' field of the ProfitShare Rule.**<br>- `notFee` - **The ProfitShare applies only if the entry fee is not exactly equal to the fee set in the 'value' field of the ProfitShare Rule.**<br>- `fromentity` - **The ProfitShare applies only if the entry fromentity (or opposingEntryfromentity) is exactly the same as the entity set in the 'value' field of the ProfitShare Rule.**<br>- `notFromentity` - **The ProfitShare applies only if the entry fromentity (or opposingEntryfromentity) is not exactly equal to the entity set in the 'value' field of the ProfitShare Rule.**<br></details><br> |
| `value` | `str` | Optional | The value to compare against when evaluating this ProfitShare Rule. |
| `grouping` | `str` | Optional | A name for a group of rules to be applied in conjunction when evaluating this ProfitShare Rule.<br>When grouping is used the ProfitShare will be allowed to be processed if at least one of the rules are matched. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

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

