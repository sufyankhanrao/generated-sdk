
# Availability

A staff availability entry

## Structure

`Availability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The ID of the availability. |
| `staff` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `session_type` | [`SessionType`](../../doc/models/session-type.md) | Optional | SessionType contains information about the session types in a business. |
| `programs` | [`List[Program]`](../../doc/models/program.md) | Optional | Contains information about the programs. |
| `start_date_time` | `datetime` | Optional | The date and time the availability starts. |
| `end_date_time` | `datetime` | Optional | The date and time the availability ends. |
| `bookable_end_date_time` | `datetime` | Optional | The time of day that the last appointment can start. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `prep_time` | `int` | Optional | Prep time in minutes |
| `finish_time` | `int` | Optional | Finish time in minutes |
| `is_masked` | `bool` | Optional | When `true`, indicates that the staff member's name for availabilty is masked.<br>When `false`, indicates that the staff member's name for availabilty is not masked. |
| `show_public` | `bool` | Optional | When `true`, indicates that the schedule is shown to the clients.<br>When `false`, indicates that the schedule is hidden from the clients. |

## Example (as JSON)

```json
{
  "Id": 158,
  "Staff": {
    "Address": "Address8",
    "AppointmentInstructor": false,
    "AlwaysAllowDoubleBooking": false,
    "Bio": "Bio2",
    "City": "City8"
  },
  "SessionType": {
    "Type": "Class",
    "DefaultTimeLength": 30,
    "StaffTimeLength": 52,
    "Id": 52,
    "Name": "Name8"
  },
  "Programs": [
    {
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "CancelOffset": 182,
      "ContentFormats": [
        "ContentFormats9"
      ]
    },
    {
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "CancelOffset": 182,
      "ContentFormats": [
        "ContentFormats9"
      ]
    },
    {
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "CancelOffset": 182,
      "ContentFormats": [
        "ContentFormats9"
      ]
    }
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

