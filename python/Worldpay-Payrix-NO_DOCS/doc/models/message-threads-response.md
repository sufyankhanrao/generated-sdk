
# Message Threads Response

## Structure

`MessageThreadsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the Login that owns this messageThreads resource. |
| `forlogin` | `str` | Optional | The identifier of the receiving Login of this messageThreads resource. |
| `hold` | `str` | Optional | The identifier of the Hold that is related to this messageThread. |
| `entity_return` | `str` | Optional | This field has the ID from the EntityReturns table that hold ACH returns for disbursements or eCheck txns. |
| `opposing_message_thread` | `str` | Optional | Specifies whether this is the opposing MessageThread. |
| `folder` | `str` | Optional | Free-form text. By default, a messageThread resource is set as 'default'. |
| `sender` | `str` | Optional | Free-form text that represents the name of the sender of a messageThread resource. |
| `recipient` | `str` | Optional | Free-form text that represents the name of the recipient of a messageThread resource. |
| `subject` | `str` | Optional | Free-form text for adding a subject to a messageThread resource. |

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

