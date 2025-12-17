
# Get Staff Response

## Structure

`GetStaffResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `staff_members` | [`List[Staff]`](../../doc/models/staff.md) | Optional | A list of staff members. See Staff for a description of the 'Staff' information. |

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

