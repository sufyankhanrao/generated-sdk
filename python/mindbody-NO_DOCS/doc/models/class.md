
# Class

Represents a single class instance. The class meets at the start time, goes until the end time.

## Structure

`Class`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_schedule_id` | `int` | Optional | The ID used to retrieve the class schedule for the desired class. |
| `visits` | [`List[Visit]`](../../doc/models/visit.md) | Optional | Contains information about visits. |
| `clients` | [`List[Client]`](../../doc/models/client.md) | Optional | Contains information about clients. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `resource` | [`ResourceSlim`](../../doc/models/resource-slim.md) | Optional | Contains information about resources, such as rooms. |
| `max_capacity` | `int` | Optional | The maximum number of clients allowed in the class. |
| `web_capacity` | `int` | Optional | The maximum number of clients allowed to sign up online for the class. |
| `total_booked` | `int` | Optional | The total number of clients booked in the class. |
| `total_signed_in` | `int` | Optional | The total number of clients signed into the class. |
| `total_booked_waitlist` | `int` | Optional | The total number of booked clients on the waiting list for the class. |
| `web_booked` | `int` | Optional | The total number of clients who signed up online for the class. |
| `semester_id` | `int` | Optional | The ID of the semester that the class is a part of, if any. |
| `is_canceled` | `bool` | Optional | When `true`, indicates that the class has been cancelled.<br /><br>When `false`, indicates that the class has not been cancelled. |
| `substitute` | `bool` | Optional | When `true`, indicates that the class is being taught by a substitute teacher.<br /><br>When `false`, indicates that the class is being taught by its regular teacher. |
| `active` | `bool` | Optional | When `true`, indicates that the class is shown to clients when in consumer mode.<br /><br>When `false`, indicates that the class is not shown to clients when in consumer mode. |
| `is_waitlist_available` | `bool` | Optional | When `true`, indicates that the clients can be placed on a waiting list for the class.<br /><br>When `false`, indicates that the clients cannot be placed on a waiting list for the class. |
| `is_enrolled` | `bool` | Optional | When `true`, indicates that the client with the given `ClientId` is enrolled in this class.<br /><br>When `false`, indicates that the client with the given `ClientId` is not enrolled in this class. |
| `hide_cancel` | `bool` | Optional | When `true`, indicates that this class is hidden when cancelled.<br /><br>When `false`, indicates that this class is not hidden when cancelled. |
| `id` | `int` | Optional | The unique identifier for the class. |
| `is_available` | `bool` | Optional | When `true`, indicates that the client with the given client ID can book this class.<br /><br>When `false`, indicates that the client with the given client ID cannot book this class. |
| `start_date_time` | `datetime` | Optional | The time this class is scheduled to start. |
| `end_date_time` | `datetime` | Optional | The time this class is scheduled to end. |
| `last_modified_date_time` | `datetime` | Optional | The last time this class was modified. |
| `class_description` | [`ClassDescription`](../../doc/models/class-description.md) | Optional | Represents a class definition. The class meets at the start time, goes until the end time. |
| `staff` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `booking_window` | [`BookingWindow`](../../doc/models/booking-window.md) | Optional | The booking window for registration |
| `booking_status` | [`BookingStatusEnum`](../../doc/models/booking-status-enum.md) | Optional | Contains the booking’s payment status. |
| `virtual_stream_link` | `str` | Optional | The link to the Mindbody-hosted live stream for the class. This is `null` when no live stream is configured for the class. |
| `wait_list_size` | `int` | Optional | The maximum number allowed on the waiting list for the class. |

## Example (as JSON)

```json
{
  "ClassScheduleId": 206,
  "Visits": [
    {
      "AppointmentId": 196,
      "AppointmentGenderPreference": "Male",
      "AppointmentStatus": "Booked",
      "ClassId": 140,
      "ClientId": "ClientId4"
    },
    {
      "AppointmentId": 196,
      "AppointmentGenderPreference": "Male",
      "AppointmentStatus": "Booked",
      "ClassId": 140,
      "ClientId": "ClientId4"
    }
  ],
  "Clients": [
    {
      "AppointmentGenderPreference": "Female",
      "BirthDate": "2016-03-13T12:52:32.123Z",
      "Country": "Country4",
      "CreationDate": "2016-03-13T12:52:32.123Z",
      "CustomClientFields": [
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        },
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        }
      ]
    }
  ],
  "Location": {
    "AdditionalImageURLs": [
      "AdditionalImageURLs4"
    ],
    "Address": "Address2",
    "Address2": "Address24",
    "Amenities": [
      {
        "Id": 214,
        "Name": "Name8"
      },
      {
        "Id": 214,
        "Name": "Name8"
      },
      {
        "Id": 214,
        "Name": "Name8"
      }
    ],
    "BusinessDescription": "BusinessDescription8"
  },
  "Resource": {
    "Id": 22,
    "Name": "Name6"
  }
}
```

