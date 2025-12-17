
# Get Staff Session Types Response

## Structure

`GetStaffSessionTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `staff_session_types` | [`List[StaffSessionType]`](../../doc/models/staff-session-type.md) | Optional | Contains information about staff member session types. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "StaffSessionTypes": [
    {
      "StaffId": 44,
      "Type": "Enrollment",
      "Id": 34,
      "Name": "Name6",
      "NumDeducted": 82
    },
    {
      "StaffId": 44,
      "Type": "Enrollment",
      "Id": 34,
      "Name": "Name6",
      "NumDeducted": 82
    },
    {
      "StaffId": 44,
      "Type": "Enrollment",
      "Id": 34,
      "Name": "Name6",
      "NumDeducted": 82
    }
  ]
}
```

