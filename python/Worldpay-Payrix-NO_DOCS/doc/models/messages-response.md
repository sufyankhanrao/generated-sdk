
# Messages Response

## Structure

`MessagesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `message_thread` | `str` | Optional | The identifier of the messageThreads that owns this Messages resource. |
| `opposing_message` | `str` | Optional | Specifies whether this is the opposingMessage or not. |
| `mtype` | [`MessageTypeEnum`](../../doc/models/message-type-enum.md) | Optional | Whether this resource is incoming or outgoing.<br><br><details><br><summary>Valid Values</summary><br>- `incoming` - **Incoming messages is assigned.**<br>- `outgoing` - **Outgoing message is assigned.**<br><br> </details><br> |
| `generated` | [`GeneratedEnum`](../../doc/models/generated-enum.md) | Optional | Whether this resource was automatically generated or not.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Message was auomatically generated and a value of '0' means it was manually generated.**<br>- `1` - **Message was manually generated.**<br><br> </details><br> |
| `secure` | [`SecureEnum`](../../doc/models/secure-enum.md) | Optional | Whether this resource is marked as secure.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Messages will protected in email notifications.**<br>- `1` - **Message will display entirely.**<br><br></details><br> |
| `read` | [`MessagesReadEnum`](../../doc/models/messages-read-enum.md) | Optional | Whether this resource is marked as read.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Message has not been read yet.**<br>- `1` - **Message has been read and a value.**<br><br></details><br> |
| `message` | `str` | Optional | Free-form text for adding a message to a messageThread resource. |

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

