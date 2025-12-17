
# Get Bookable Items Response

## Structure

`GetBookableItemsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `availabilities` | [`List[Availability]`](../../doc/models/availability.md) | Optional | Contains information about the availabilities for appointment booking. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Availabilities": [
    {
      "Id": 96,
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
        }
      ],
      "StartDateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 96,
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
        }
      ],
      "StartDateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 96,
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
        }
      ],
      "StartDateTime": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

