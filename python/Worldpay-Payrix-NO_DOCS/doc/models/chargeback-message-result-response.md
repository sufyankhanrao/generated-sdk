
# Chargeback Message Result Response

## Structure

`ChargebackMessageResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `chargeback_message` | `str` | Optional | The identifier of the chargebackMessage resource that this chargebackMessageResult relates to. |
| `mtype` | [`ChargebackMessageResultTypeEnum`](../../doc/models/chargeback-message-result-type-enum.md) | Optional | The type of this chargebackMessageResult.<br><br><details><br><summary>Valid Values</summary><br>- `general` - **A general type of result.**<br>- `platform` - **Platform message.**<br></details><br> |
| `message` | `str` | Optional | The Chargeback message itself. |

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

