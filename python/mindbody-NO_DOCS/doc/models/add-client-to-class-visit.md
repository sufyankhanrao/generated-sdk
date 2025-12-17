
# Add Client to Class Visit

## Structure

`AddClientToClassVisit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `appointment_id` | `int` | Optional | The appointment’s ID. |
| `appointment_gender_preference` | [`AppointmentGenderPreference1Enum`](../../doc/models/appointment-gender-preference-1-enum.md) | Optional | The gender of staff member with whom the client prefers to book appointments. |
| `appointment_status` | [`AppointmentStatusEnum`](../../doc/models/appointment-status-enum.md) | Optional | The status of the appointment. |
| `class_id` | `int` | Optional | The class ID that was used to retrieve the visits. |
| `client_id` | `str` | Optional | The ID of the client associated with the visit. |
| `start_date_time` | `datetime` | Optional | The time this class is scheduled to start. |
| `end_date_time` | `datetime` | Optional | The date and time the visit ends. The Public API returns UTC dates and times. For example, a class that occurs on June 25th, 2018 at 2:15PM (EST) appears as “2018-06-25T19:15:00Z” because EST is five hours behind UTC. Date time pairs always return in the format YYYY-MM-DDTHH:mm:ssZ. |
| `id` | `int` | Optional | The ID of the visit. |
| `last_modified_date_time` | `datetime` | Optional | When included in the request, only records modified on or after the specified `LastModifiedDate` are included in the response. The Public API returns UTC dates and times. For example, a class that occurs on June 25th, 2018 at 2:15PM (EST) appears as “2018-06-25T19:15:00Z” because EST is five hours behind UTC. Date time pairs always return in the format YYYY-MM-DDTHH:mm:ssZ. |
| `late_cancelled` | `bool` | Optional | When `true`, indicates that the class has been `LateCancelled`.<br /><br>When `false`, indicates that the class has not been `LateCancelled`. |
| `location_id` | `int` | Optional | The ID of the location where the visit took place or is to take place. |
| `make_up` | `bool` | Optional | When `true`, the client can make up this session and a session is not deducted from the pricing option that was used to sign the client into the enrollment. When the client has the make-up session, a session is automatically removed from a pricing option that matches the service category of the enrollment and is within the same date range of the missed session.<br /><br>When `false`, the client cannot make up this session. See [Enrollments: Make-ups](https://support.mindbodyonline.com/s/article/203259433-Enrollments-Make-ups?language=en_US) for more information. |
| `name` | `str` | Optional | The name of the class. |
| `service_id` | `int` | Optional | The ID of the client's pricing option applied to the class visit. |
| `service_name` | `str` | Optional | The name of the pricing option applied to the class visit. |
| `product_id` | `int` | Optional | The business' ID of the type of pricing option used to pay for the class visit. |
| `signed_in` | `bool` | Optional | When `true`, indicates that the client has been signed in.<br /><br>When `false`, indicates that the client has not been signed in. |
| `staff_id` | `int` | Optional | The ID of the staff member who is teaching the class. |
| `web_signup` | `bool` | Optional | When `true`, indicates that the client signed up online.<br /><br>When `false`, indicates that the client was signed up by a staff member. |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Optional | The action taken. |
| `cross_regional_booking_performed` | `bool` | Optional | When `true`, indicates that the client is paying for the visit using a pricing option from one of their associated cross-regional profiles. |
| `site_id` | `int` | Optional | The ID of the business from which cross-regional payment is applied. |
| `waitlist_entry_id` | `int` | Optional | When this value is not null, it indicates that the client is on the waiting list for the requested class. The only additional fields that are populated when this is not null are:<br><br>* ClassId<br>* ClientId<br><br>You can call GET WaitlistEntries using `WaitlistEntryId` to obtain more data about this waiting list entry. |

## Example (as JSON)

```json
{
  "AppointmentId": 128,
  "AppointmentGenderPreference": "Female",
  "AppointmentStatus": "Completed",
  "ClassId": 208,
  "ClientId": "ClientId6"
}
```

