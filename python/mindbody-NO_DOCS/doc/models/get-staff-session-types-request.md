
# Get Staff Session Types Request

## Structure

`GetStaffSessionTypesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Required | The ID of the staff member whose session types you want to return. |
| `program_ids` | `List[int]` | Optional | Filters results to session types that belong to one of the given program IDs. If omitted, all program IDs return. |
| `online_only` | `bool` | Optional | When `true`, indicates that only the session types that can be booked online should be returned.<br>Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StaffId": 168,
  "ProgramIds": [
    218
  ],
  "OnlineOnly": false,
  "Limit": 12,
  "Offset": 202
}
```

