
# Add Formula Note Request

## Structure

`AddFormulaNoteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client who needs to have a formula note added. |
| `appointment_id` | `int` | Optional | The appointment ID that the formula note is related to. |
| `note` | `str` | Required | The new formula note text. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "AppointmentId": 120,
  "Note": "Note0"
}
```

