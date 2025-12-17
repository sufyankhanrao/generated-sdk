
# Txn Sessions Response

## Structure

`TxnSessionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The login under which to perform this action. If you do not supply a login in this field, then the API defaults to the login that is currently authenticated. |
| `merchant` | `str` | Optional | The Merchant being used to create this txn session. |
| `status` | `str` | Optional | The current status of this key. |
| `configurations` | [`TxnSessionsConfigurations`](../../doc/models/txn-sessions-configurations.md) | Optional | Configurable data to be used to enhance security. |
| `origin` | `str` | Optional | The origin from this request. |
| `duration_available` | `int` | Optional | Specifies the number of minutes for which the key remains valid. Once this duration expires, the key will be automatically voided and cannot be used. |
| `times_used` | `int` | Optional | Indicates the number of times the key has been used to make requests. |
| `times_approved` | `int` | Optional | Indicates the number of approved transactions that have been made using this key. |
| `key` | `str` | Optional | The randomly generated key used to authenticate a user. |

## Example (as JSON)

```json
{
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier8"
}
```

