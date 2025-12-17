
# Update Class Enrollment Schedule Request

## Structure

`UpdateClassEnrollmentScheduleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_id` | `int` | Optional | The class id, a block of schedules |
| `class_description_id` | `int` | Optional | Used only internally, overridden if sent |
| `location_id` | `int` | Optional | The location where the class is taking place |
| `start_date` | `datetime` | Optional | Class start time (use null for TBD) |
| `end_date` | `datetime` | Optional | Class end time (ignored if StartTime is null) |
| `start_time` | `datetime` | Optional | Class start time (use null for TBD) |
| `end_time` | `datetime` | Optional | Class end time (ignored if StartTime is null) |
| `day_sunday` | `bool` | Optional | (optional) - If the class occurs on Sunday (ignored if EndDate is null) |
| `day_monday` | `bool` | Optional | (optional) - If the class occurs on Monday (ignored if EndDate is null) |
| `day_tuesday` | `bool` | Optional | (optional) - If the class occurs on Tuesday (ignored if EndDate is null) |
| `day_wednesday` | `bool` | Optional | (optional) - If the class occurs on Wednesday (ignored if EndDate is null) |
| `day_thursday` | `bool` | Optional | (optional) - If the class occurs on Thursday (ignored if EndDate is null) |
| `day_friday` | `bool` | Optional | (optional) - If the class occurs on Friday (ignored if EndDate is null) |
| `day_saturday` | `bool` | Optional | (optional) - If the class occurs on Saturday (ignored if EndDate is null |
| `staff_id` | `int` | Optional | The staff member teaching the class |
| `staff_pay_rate` | `int` | Optional | The staff pay rate |
| `resource_id` | `int` | Optional | (optional) - The room where the class is taking place |
| `max_capacity` | `int` | Optional | How many people can attend |
| `web_capacity` | `int` | Optional | How many people can signup online (if 0 clients cannot signup online) |
| `waitlist_capacity` | `int` | Optional | One of: PaymentRequired, BookAndPayLater, Free |
| `booking_status` | `str` | Optional | One of: PaymentRequired, BookAndPayLater, Free |
| `allow_open_enrollment` | `bool` | Optional | Allow clients to choose which sessions they'd like to sign up for |
| `allow_date_forward_enrollment` | `bool` | Optional | Allow booking after the enrollment has started |
| `retain_schedule_changes` | `bool` | Optional | Whether or not to retain manual schedule changes within the date range |

## Example (as JSON)

```json
{
  "ClassId": 200,
  "ClassDescriptionId": 176,
  "LocationId": 92,
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z"
}
```

