
# Send Auto Email Request

## Structure

`SendAutoEmailRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client email will be sent to. |
| `email_type` | `str` | Required | The type of the email that will be sent to a client.<br>Possible values are:<br><br>* BusinessWelcomeEmail<br>* ConsumerWelcomeEmail |

## Example (as JSON)

```json
{
  "ClientId": "ClientId0",
  "EmailType": "EmailType4"
}
```

