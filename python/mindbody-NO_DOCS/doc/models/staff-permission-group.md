
# Staff Permission Group

## Structure

`StaffPermissionGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `permission_group_name` | `str` | Optional | The name of the permission group. |
| `ip_restricted` | `bool` | Optional | When `true`, the staff member’s permissions are restricted to specific IP addresses.<br /><br>When `false`, the staff member’s permissions are not restricted to specific IP addresses. |
| `allowed_permissions` | [`List[AllowedPermissionEnum]`](../../doc/models/allowed-permission-enum.md) | Optional | A list of the permissions allowed to the staff member. See [Permission Values](https://developers.mindbodyonline.com/PublicDocumentation/V6#epermission-values) for descriptions of the possible permissions. |
| `denied_permissions` | [`List[DeniedPermissionEnum]`](../../doc/models/denied-permission-enum.md) | Optional | A list of the permissions that the staff member is not allowed to exercise. See [Permission Values](https://developers.mindbodyonline.com/PublicDocumentation/V6#epermission-values) for descriptions of the possible permissions. |

## Example (as JSON)

```json
{
  "PermissionGroupName": "PermissionGroupName4",
  "IpRestricted": false,
  "AllowedPermissions": [
    "ExportReports",
    "ManageTaggedClients"
  ],
  "DeniedPermissions": [
    "AccountBalancesReport",
    "PersonalCancellationsReport",
    "CancellationsReport"
  ]
}
```

