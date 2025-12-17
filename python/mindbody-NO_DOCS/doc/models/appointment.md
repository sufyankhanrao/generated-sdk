
# Appointment

Contains information about an appointment.

## Structure

`Appointment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gender_preference` | [`GenderPreferenceEnum`](../../doc/models/gender-preference-enum.md) | Optional | The prefered gender of the appointment provider.<br>Possible values are:<br><br>* None<br>* Female<br>* Male |
| `duration` | `int` | Optional | The duration of the appointment. |
| `provider_id` | `str` | Optional | If a user has Complementary and Alternative Medicine features enabled, this property indicates the provider assigned to the appointment. |
| `id` | `int` | Optional | The unique ID of the appointment. |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | The status of this appointment.<br>Possible values are:<br><br>* None<br>* Requested<br>* Booked<br>* Completed<br>* Confirmed<br>* Arrived<br>* NoShow<br>* Cancelled<br>* LateCancelled |
| `start_date_time` | `datetime` | Optional | The date and time the appointment is to start. |
| `end_date_time` | `datetime` | Optional | The date and time the appointment is to end. |
| `notes` | `str` | Optional | Any notes associated with the appointment. |
| `partner_external_id` | `str` | Optional | Optional external key for api partners. |
| `staff_requested` | `bool` | Optional | When `true`, indicates that the staff member was requested specifically by the client. |
| `program_id` | `int` | Optional | The ID of the program to which this appointment belongs. |
| `session_type_id` | `int` | Optional | The ID of the session type of this appointment. |
| `location_id` | `int` | Optional | The ID of the location where this appointment is to take place. |
| `staff_id` | `int` | Optional | The ID of the staff member providing the service for this appointment. |
| `client_id` | `str` | Optional | The RSSID of the client who is booked for this appointment. |
| `first_appointment` | `bool` | Optional | When `true`, indicates that this is the client’s first appointment at this site. |
| `is_waitlist` | `bool` | Optional | When `true`, indicates that the client should be added to a specific appointment waiting list.<br>When `false`, the client should not be added to the waiting list.<br>Default: *false* |
| `waitlist_entry_id` | `int` | Optional | The unique ID of the appointment waitlist. |
| `client_service_id` | `int` | Optional | The ID of the pass on the client’s account that is to pay for this appointment. |
| `resources` | [`List[ResourceSlim]`](../../doc/models/resource-slim.md) | Optional | The resources this appointment is to use. |
| `add_ons` | [`List[AddOnSmall]`](../../doc/models/add-on-small.md) | Optional | Any AddOns associated with the appointment |
| `online_description` | `str` | Optional | Online Description associated with the appointment |

## Example (as JSON)

```json
{
  "GenderPreference": "None",
  "Duration": 182,
  "ProviderId": "ProviderId6",
  "Id": 136,
  "Status": "None"
}
```

