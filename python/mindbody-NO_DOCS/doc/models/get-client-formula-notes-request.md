
# Get Client Formula Notes Request

## Structure

`GetClientFormulaNotesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | The client ID of the client whose formula notes are being requested. |
| `appointment_id` | `int` | Optional | The appointment ID of an appointment in the studio specified in the header of the request. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "AppointmentId": 38,
  "Limit": 16,
  "Offset": 82
}
```

