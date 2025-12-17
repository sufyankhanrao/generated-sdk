
# Availability 1

The availability of a specific staff

## Structure

`Availability1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Id of the availability |
| `staff` | [`Staff1`](../../doc/models/staff-1.md) | Optional | - |
| `session_type` | [`SessionType1`](../../doc/models/session-type-1.md) | Optional | - |
| `programs` | [`List[Program1]`](../../doc/models/program-1.md) | Optional | Availabilities program list. |
| `start_date_time` | `datetime` | Optional | Availabilities start date and time. |
| `end_date_time` | `datetime` | Optional | Availabilities end date and time. |
| `bookable_end_date_time` | `datetime` | Optional | Availabilities bookable end date and time. |
| `location` | [`Location1`](../../doc/models/location-1.md) | Optional | - |
| `prep_time` | `int` | Optional | Appointment prep time |
| `finish_time` | `int` | Optional | Appointment finish time |
| `is_masked` | `bool` | Optional | - |
| `show_public` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "Id": 176,
  "Staff": {
    "Id": 176,
    "FirstName": "FirstName6",
    "LastName": "LastName6",
    "DisplayName": "DisplayName4",
    "Email": "Email6"
  },
  "SessionType": {
    "Type": "DropIn",
    "DefaultTimeLength": 30,
    "StaffTimeLength": 52,
    "ProgramId": 60,
    "NumDeducted": 64
  },
  "Programs": [
    {
      "CancelOffset": 182,
      "Id": 192,
      "Name": "Name8",
      "ScheduleType": "Appointment",
      "ContentFormat": "Mindbody"
    }
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

