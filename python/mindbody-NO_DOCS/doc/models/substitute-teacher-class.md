
# Substitute Teacher Class

Represents a single class instance. Used in SubstituteClassTeacher endpoint.

## Structure

`SubstituteTeacherClass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_schedule_id` | `int` | Optional | The class schedule ID of the requested class. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `max_capacity` | `int` | Optional | The total number of bookings allowed in the class. |
| `web_capacity` | `int` | Optional | The total number of online bookings allowed in the class. |
| `total_booked` | `int` | Optional | The total number of clients who are booked into the class prior to this call being made. |
| `total_booked_waitlist` | `int` | Optional | The total number of booked clients who are on the waiting list for the class prior to this call being made. |
| `web_booked` | `int` | Optional | The total number of bookings in the class made by online users, prior to this call being made. This property is the current number of bookings counted toward the `WebCapacity` limit. |
| `semester_id` | `int` | Optional | Identifies the semester assigned to this class. |
| `is_canceled` | `bool` | Optional | When `true`, indicates that the class has been canceled.<br /><br>When `false`, indicates that the class has not been canceled and may still be bookable. |
| `substitute` | `bool` | Optional | When `true`, indicates that the class is being taught by a substitute teacher. |
| `active` | `bool` | Optional | When `true`, indicates that the class is being shown to clients in consumer mode. |
| `is_waitlist_available` | `bool` | Optional | When `true`, indicates that the class has a waiting list and there is space available on the waiting list for another client.<br /><br>When `false`, indicates either that the class does not have a waiting list or there is no space available on the class waiting list. |
| `hide_cancel` | `bool` | Optional | When `true`, indicates that this class is should not be shown to clients when `IsCancelled` is `true`.<br /><br>When `false`, indicates that this class is should be shown to clients when `IsCancelled` is `true`.<br /><br>This property can be ignored when the `IsCancelled` property is `false`. |
| `id` | `int` | Optional | The unique identifier of the class. |
| `is_available` | `bool` | Optional | When `true`, indicates that the class can be booked.<br /><br>When `false`, that the class cannot be booked at this time. |
| `start_date_time` | `datetime` | Optional | The date and time that this class is scheduled to start. |
| `end_date_time` | `datetime` | Optional | The date and time when this class is scheduled to end. |
| `last_modified_date_time` | `datetime` | Optional | The last time the class was modified. |
| `class_description` | [`ClassDescription`](../../doc/models/class-description.md) | Optional | Represents a class definition. The class meets at the start time, goes until the end time. |
| `staff` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `virtual_stream_link` | `str` | Optional | The URL for the pre-recorded live stream for the class if hosted on the mindbody virtual wellness platform |

## Example (as JSON)

```json
{
  "ClassScheduleId": 190,
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
  "MaxCapacity": 108,
  "WebCapacity": 154,
  "TotalBooked": 170
}
```

