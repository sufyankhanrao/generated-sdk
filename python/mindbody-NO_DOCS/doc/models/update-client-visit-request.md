
# Update Client Visit Request

## Structure

`UpdateClientVisitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visit_id` | `int` | Required | The ID of the visit to be updated. |
| `makeup` | `bool` | Optional | When `true`, indicates that the visit is eligible to be made up. |
| `signed_in` | `bool` | Optional | When `true`, indicates that the client has signed in for the visit. |
| `client_service_id` | `int` | Optional | The ID of the service to assign to the visit. |
| `execute` | `str` | Optional | The execute code used to update this visit. Possible values are:<br><br>* Cancel<br>* Latecancel<br>* Unlatecancel |
| `test` | `bool` | Optional | When `true`, indicates that test mode is enabled. When test mode is enabled, input information is validated, but not committed.<br /><br>Default: **false** |
| `send_email` | `bool` | Optional | When `true`, indicates that the client should be sent an email for cancellations. Note that email is not sent unless the client has an email address and automatic emails have been set up correctly.<br /><br>Default: **false** |

## Example (as JSON)

```json
{
  "VisitId": 154,
  "Makeup": false,
  "SignedIn": false,
  "ClientServiceId": 50,
  "Execute": "Execute8",
  "Test": false
}
```

