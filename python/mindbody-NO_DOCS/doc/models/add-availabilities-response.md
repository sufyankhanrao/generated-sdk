
# Add Availabilities Response

Add Availabilities Response Model

## Structure

`AddAvailabilitiesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_members` | [`List[Staff1]`](../../doc/models/staff-1.md) | Optional | Contains information about the staff. |
| `errors` | [`List[ApiError1]`](../../doc/models/api-error-1.md) | Optional | Contains information about the error. |

## Example (as JSON)

```json
{
  "StaffMembers": [
    {
      "Id": 98,
      "FirstName": "FirstName0",
      "LastName": "LastName0",
      "DisplayName": "DisplayName2",
      "Email": "Email0"
    },
    {
      "Id": 98,
      "FirstName": "FirstName0",
      "LastName": "LastName0",
      "DisplayName": "DisplayName2",
      "Email": "Email0"
    },
    {
      "Id": 98,
      "FirstName": "FirstName0",
      "LastName": "LastName0",
      "DisplayName": "DisplayName2",
      "Email": "Email0"
    }
  ],
  "Errors": [
    {
      "Message": "Message0",
      "Code": "Code4"
    },
    {
      "Message": "Message0",
      "Code": "Code4"
    }
  ]
}
```

