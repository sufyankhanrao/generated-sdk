
# Update Staff Permissions Response

## Structure

`UpdateStaffPermissionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_group` | [`StaffPermissionGroup`](../../doc/models/staff-permission-group.md) | Optional | - |

## Example (as JSON)

```json
{
  "UserGroup": {
    "PermissionGroupName": "PermissionGroupName8",
    "IpRestricted": false,
    "AllowedPermissions": [
      "ViewAppointmentSchedule",
      "ManageClassNotes"
    ],
    "DeniedPermissions": [
      "CashDrawerReportAnyDate",
      "DailyCloseoutReport"
    ]
  }
}
```

