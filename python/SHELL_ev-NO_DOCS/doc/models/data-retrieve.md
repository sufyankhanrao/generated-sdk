
# Data Retrieve

## Structure

`DataRetrieve`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Id of the session |
| `user_id` | `str` | Optional | Id of the user that started the session<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `ema_id` | `str` | Optional | Id of the evse that the user is charging<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `36` |
| `evse_id` | `str` | Optional | Ema-id of the charge token that is used |
| `last_updated` | `str` | Optional | Last updated date |
| `started_at` | `datetime` | Optional | When the session is started |
| `stopped_at` | `datetime` | Optional | When the session is stopped |
| `session_state` | [`ChargeRetrieveState`](../../doc/models/charge-retrieve-state.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "78b5d7a3-bdba-43d7-9851-1c84fcddb782",
  "userId": "281482b6-2c9a-4fd1-b3ea-1928edb40ef9",
  "emaId": "NL-TNM-C00122045-K",
  "evseId": "NL*TNM*E02003451*0",
  "startedAt": "08/19/2015 11:20:27",
  "stoppedAt": "08/19/2015 11:20:27",
  "lastUpdated": "lastUpdated2"
}
```

