
# Cancel Single Class Request

## Structure

`CancelSingleClassRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_id` | `int` | Optional | Class ID to lookup. |
| `hide_cancel` | `bool` | Optional | When `true`, indicates that this class is hidden when cancelled.<br>When `false`, indicates that this class is not hidden when cancelled. |
| `send_client_email` | `bool` | Optional | When `true`, sends the client an automatic email about the cancellation, if the client has opted to receive email. |
| `send_staff_email` | `bool` | Optional | When `true`, sends the staff an automatic email about the cancellation, if the staff has opted to receive email. |

## Example (as JSON)

```json
{
  "ClassID": 124,
  "HideCancel": false,
  "SendClientEmail": false,
  "SendStaffEmail": false
}
```

