
# Delete Contact Log Request

## Structure

`DeleteContactLogRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The client ID of the client whose Contact Log is being deleted. |
| `contact_log_id` | `int` | Required | The Contact Log ID. |
| `test` | `bool` | Optional | When `true`, indicates that this is a test request and no data is inserted into the subscriber’s database.<br>When `false`, the database is updated. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "ContactLogId": 218,
  "Test": false
}
```

