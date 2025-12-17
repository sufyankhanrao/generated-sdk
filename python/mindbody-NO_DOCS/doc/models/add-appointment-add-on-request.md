
# Add Appointment Add on Request

Creates an add-on for an appointment

## Structure

`AddAppointmentAddOnRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apply_payment` | `bool` | Optional | When `true`, indicates that a payment should be applied to the appointment. Currently only ApplyPayment=false is implemented.<br>Default: **true** |
| `appointment_id` | `int` | Optional | The appointment ID the add-on is getting added to. |
| `session_type_id` | `int` | Optional | The session type associated with the new appointment add-on. |
| `staff_id` | `int` | Optional | The ID of the staff member who is adding the new appointment add-on.<br>Default: staff member performing the appointment. |
| `test` | `bool` | Optional | When `true`, indicates that the method is to be validated, but no new appointment add-on data is added.<br>Default: **false** |

## Example (as JSON)

```json
{
  "ApplyPayment": false,
  "AppointmentId": 8,
  "SessionTypeId": 64,
  "StaffId": 170,
  "Test": false
}
```

