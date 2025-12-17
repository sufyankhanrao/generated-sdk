
# Remove Clients From Classes Request

Remove Clients From Classes Request

## Structure

`RemoveClientsFromClassesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `details` | [`List[ClassClientDetail]`](../../doc/models/class-client-detail.md) | Optional | This object includes<br>`ClientIds`: List of the RSSID(string) of the clients to remove from the specified class.<br>`ClassId`: The ID(number) of the class that you want to remove the clients from. |
| `test` | `bool` | Optional | When `true`, the request ensures that its parameters are valid without affecting real data.<br /><br>When `false`, the request performs as intended and may affect live client data.<br /><br>Default: **false** |
| `send_email` | `bool` | Optional | When `true`, indicates that the client should be sent an email. Depending on the site and client settings, an email may or may not be sent.<br /><br>Default: **false**<br>**Note**: When the Authorization header is passed and the SendEmail is set to `true`, then an email will be sent.<br>When the Authorization header is passed and the SendEmail is set to `false`, then an email will not be sent.<br>When the Authorization header is not passed and the SendEmail is set to either `true` or `false`, then an email will not be sent. |
| `late_cancel` | `bool` | Optional | When `true`, indicates that the client is to be late cancelled from the class.<br /><br>When `false`, indicates that the client is to be early cancelled from the class.<br /><br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "Details": [
    {
      "ClientIds": [
        "ClientIds5"
      ],
      "ClassId": 190
    },
    {
      "ClientIds": [
        "ClientIds5"
      ],
      "ClassId": 190
    }
  ],
  "Test": false,
  "SendEmail": false,
  "LateCancel": false,
  "Limit": 132
}
```

