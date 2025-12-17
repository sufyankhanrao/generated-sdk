
# Checkout Appointment Booking Request

## Structure

`CheckoutAppointmentBookingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | The ID of the staff member who is to provide the service being booked. |
| `location_id` | `int` | Optional | The ID of the location where the appointment is to take place. |
| `session_type_id` | `int` | Optional | The ID of the session type of this appointment. |
| `resources` | [`List[ResourceSlim]`](../../doc/models/resource-slim.md) | Optional | Contains information about the resources to be used for the appointment. |
| `start_date_time` | `datetime` | Optional | The date and time that the appointment is to start in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss. |
| `end_date_time` | `datetime` | Optional | The date and time that the appointment is to end in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss. |
| `provider_id` | `str` | Optional | The National Provider Identifier (NPI) of the staff member who is to provide the service. For an explanation of Provider IDs, see [Provider IDs](https://support.mindbodyonline.com/s/article/204075743-Provider-IDs?language=en_US). |

## Example (as JSON)

```json
{
  "StaffId": 136,
  "LocationId": 186,
  "SessionTypeId": 30,
  "Resources": [
    {
      "Id": 216,
      "Name": "Name6"
    }
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

