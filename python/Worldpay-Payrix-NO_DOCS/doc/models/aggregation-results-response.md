
# Aggregation Results Response

## Structure

`AggregationResultsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `aggregation_result_group` | `str` | Optional | The identifier of the AggregationResultGroup that this AggregationResult refers to. |
| `grouping` | `str` | Optional | Grouping is a process used in data aggregation to organize data into specific categories or groups based on certain attributes. This allows for detailed analysis and reporting on subsets of data. For example, grouping transactions by merchant and payment method enables you to see the breakdown of transactions for each merchant and payment method combination. |
| `field` | `str` | Optional | The field of the resource where calculations were made based on.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `count` | `int` | Optional | The value calculated by the count aggregation function.<br>This field is specified as an integer. |
| `sum` | `float` | Optional | The value calculated by the sum aggregation function.<br>This field is specified in cents(up to three decimal points). |
| `min` | `float` | Optional | The value calculated by the min aggregation function.<br>This field is specified in cents(up to three decimal points). |
| `max` | `float` | Optional | The value calculated by the max aggregation function.<br>This field is specified in cents(up to three decimal points). |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

