
# Profit Share Results Response

## Structure

`ProfitShareResultsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `profit_share` | `str` | Optional | The identifier of the ProfitShare that this ProfitShareResult refers to. |
| `entry` | `str` | Optional | The identifier of the Entry that this ProfitShareResult refers to. |
| `amount` | `float` | Optional | The amount that could not be shared between entities, This field is specified in cents(up to three decimal points) |
| `message` | `str` | Optional | A message regarding the failure of the ProfitShare process.<br>This field is stored as a text string and must be between 0 and 200 characters long. |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

