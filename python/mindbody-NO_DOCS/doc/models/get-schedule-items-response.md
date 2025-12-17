
# Get Schedule Items Response

## Structure

`GetScheduleItemsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `staff_members` | [`List[Staff]`](../../doc/models/staff.md) | Optional | Contains information about staff members with schedule items. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "StaffMembers": [
    {
      "Address": "Address2",
      "AppointmentInstructor": false,
      "AlwaysAllowDoubleBooking": false,
      "Bio": "Bio6",
      "City": "City2"
    },
    {
      "Address": "Address2",
      "AppointmentInstructor": false,
      "AlwaysAllowDoubleBooking": false,
      "Bio": "Bio6",
      "City": "City2"
    }
  ]
}
```

