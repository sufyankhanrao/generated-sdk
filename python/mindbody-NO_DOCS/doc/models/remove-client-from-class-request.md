
# Remove Client From Class Request

## Structure

`RemoveClientFromClassRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The RSSID of the client to remove from the specified class. |
| `class_id` | `int` | Required | The ID of the class that you want to remove the client from. |
| `test` | `bool` | Optional | When `true`, the request ensures that its parameters are valid without affecting real data.<br /><br>When `false`, the request performs as intended and may affect live client data.<br /><br>Default: **false** |
| `send_email` | `bool` | Optional | When `true`, indicates that the client should be sent an email. Depending on the site and client settings, an email may or may not be sent.<br /><br>Default: **false**<br>Note: When the Authorization header is passed and the SendEmail is set to `true`, then an email will be sent.<br>When the Authorization header is passed and the SendEmail is set to `false`, then an email will not be sent.<br>When the Authorization header is not passed and the SendEmail is set to either `true` or `false`, then an email will not be sent. |
| `late_cancel` | `bool` | Optional | When `true`, indicates that the client is to be late cancelled from the class.<br /><br>When `false`, indicates that the client is to be early cancelled from the class.<br /><br>Default: **false** |
| `visit_id` | `int` | Optional | The ID of the client visit that you want to remove from the class.<br>Default: **0** |

## Example (as JSON)

```json
{
  "ClientId": "ClientId8",
  "ClassId": 6,
  "Test": false,
  "SendEmail": false,
  "LateCancel": false,
  "VisitId": 8
}
```

