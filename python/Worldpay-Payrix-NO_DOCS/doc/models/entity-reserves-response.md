
# Entity Reserves Response

## Structure

`EntityReservesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `fund` | `str` | Optional | The identifier of the Fund that this entityReserves resource relates to. |
| `total` | `int` | Optional | The amount held in this entityReserve.<br>This field is specified as an integer in cents. |
| `request_sequence` | `int` | Optional | The current sequentially numbered activity requested for this entityReserve. |
| `processed_sequence` | `int` | Optional | The current sequentially numbered activity processed for this entityReserve. |
| `name` | `str` | Optional | The name of this EntityReserve.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `description` | `str` | Optional | A description of this EntityReserve.<br>This field is stored as a text string and must be between 0 and 100 characters long. |

## Example (as JSON)

```json
{
  "id": "id4",
  "created": "created4",
  "modified": "modified8",
  "creator": "String3",
  "modifier": "modifier2"
}
```

