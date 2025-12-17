
# Staff Setting

contains the information about the staff settings.

## Structure

`StaffSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `use_staff_nicknames` | `bool` | Optional | When `true`, `DisplayName` of the staff will be displayed.<br>When `false`, `DisplayName` will be displayed as null. |
| `show_staff_last_names_on_schedules` | `bool` | Optional | When `true`, indicates that the Name contains both the `FirstName` and `LastName` of the staff.<br>When `false`, indicates that the Name contains only the `FirstName` of the staff. |

## Example (as JSON)

```json
{
  "UseStaffNicknames": false,
  "ShowStaffLastNamesOnSchedules": false
}
```

