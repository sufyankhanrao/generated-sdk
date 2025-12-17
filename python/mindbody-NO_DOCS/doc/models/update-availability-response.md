
# Update Availability Response

This is the update avaialability response

## Structure

`UpdateAvailabilityResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_members` | [`List[Staff]`](../../doc/models/staff.md) | Optional | This is the success list of the trainer availability |
| `errors` | [`List[ApiError]`](../../doc/models/api-error.md) | Optional | - |

## Example (as JSON)

```json
{
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
  ],
  "Errors": [
    {
      "Message": "Message0",
      "Code": "Code4"
    }
  ]
}
```

