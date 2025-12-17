
# Add Appointment Add on Response

## Structure

`AddAppointmentAddOnResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `appointment_id` | `int` | Optional | This is the id of the main appointment we added on to |
| `add_on_appointment_id` | `int` | Optional | This is the id for the newly created add-on appointment |

## Example (as JSON)

```json
{
  "AppointmentId": 26,
  "AddOnAppointmentId": 112
}
```

