
# Update Staff Permissions Request

## Structure

`UpdateStaffPermissionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Required | The ID of the staff member whose permission you want to change. Staff member must have a login. |
| `permission_group_name` | `str` | Required | The name of the permission group. |

## Example (as JSON)

```json
{
  "StaffId": 60,
  "PermissionGroupName": "PermissionGroupName6"
}
```

