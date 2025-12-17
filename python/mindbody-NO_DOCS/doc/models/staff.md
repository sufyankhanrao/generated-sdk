
# Staff

The Staff

## Structure

`Staff`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `str` | Optional | The address of the staff member who is teaching the class. |
| `appointment_instructor` | `bool` | Optional | When `true`, indicates that the staff member offers appointments.<br /><br>When `false`, indicates that the staff member does not offer appointments. |
| `always_allow_double_booking` | `bool` | Optional | When `true`, indicates that the staff member can be scheduled for overlapping services.<br /><br>When `false`, indicates that the staff can only be scheduled for one service at a time in any given time-frame. |
| `bio` | `str` | Optional | The staff member’s biography. This string contains HTML. |
| `city` | `str` | Optional | The staff member’s city. |
| `country` | `str` | Optional | The staff member’s country. |
| `email` | `str` | Optional | The staff member’s email address. |
| `first_name` | `str` | Optional | The staff member’s first name. |
| `display_name` | `str` | Optional | The staff member’s Nickname. |
| `home_phone` | `str` | Optional | The staff member’s home phone number. |
| `id` | `int` | Optional | The ID assigned to the staff member. |
| `independent_contractor` | `bool` | Optional | When `true`, indicates that the staff member is an independent contractor.<br>When `false`, indicates that the staff member is not an independent contractor. |
| `is_male` | `bool` | Optional | When `true`, indicates that the staff member is male.<br>When `false`, indicates that the staff member is female. |
| `last_name` | `str` | Optional | The staff member’s last name. |
| `mobile_phone` | `str` | Optional | The staff member’s mobile phone number. |
| `name` | `str` | Optional | The staff member’s name. |
| `postal_code` | `str` | Optional | The staff member’s postal code. |
| `class_teacher` | `bool` | Optional | When `true`, indicates that the staff member can teach classes.<br>When `false`, indicates that the staff member cannot teach classes. |
| `sort_order` | `int` | Optional | If configured by the business owner, this field determines a staff member’s weight when sorting. Use this field to sort staff members on your interface. |
| `state` | `str` | Optional | The staff member’s state. |
| `work_phone` | `str` | Optional | The staff member’s work phone number. |
| `image_url` | `str` | Optional | The URL of the staff member’s image, if one has been uploaded. |
| `class_assistant` | `bool` | Optional | Is the staff an assistant |
| `class_assistant_2` | `bool` | Optional | Is the staff an assistant2 |
| `employment_start` | `datetime` | Optional | The start date of employment |
| `employment_end` | `datetime` | Optional | The end date of employment |
| `provider_i_ds` | `List[str]` | Optional | A list of ProviderIds for the staff. |
| `rep` | `bool` | Optional | return true if staff is sales Rep 1 else false. |
| `rep_2` | `bool` | Optional | return true if staff is sales Rep 2 else false. |
| `rep_3` | `bool` | Optional | return true if staff is sales Rep 3 else false. |
| `rep_4` | `bool` | Optional | return true if staff is sales Rep 4 else false. |
| `rep_5` | `bool` | Optional | return true if staff is sales Rep 5 else false. |
| `rep_6` | `bool` | Optional | return true if staff is sales Rep 6 else false. |
| `staff_settings` | [`StaffSetting`](../../doc/models/staff-setting.md) | Optional | contains the information about the staff settings. |
| `appointments` | [`List[Appointment]`](../../doc/models/appointment.md) | Optional | A list of appointments for the staff. |
| `unavailabilities` | [`List[Unavailability]`](../../doc/models/unavailability.md) | Optional | A list of unavailabilities for the staff. |
| `availabilities` | [`List[Availability]`](../../doc/models/availability.md) | Optional | A list of availabilities for the staff. |
| `emp_id` | `str` | Optional | The EmpID assigned to the staff member. |

## Example (as JSON)

```json
{
  "Address": "Address8",
  "AppointmentInstructor": false,
  "AlwaysAllowDoubleBooking": false,
  "Bio": "Bio2",
  "City": "City8"
}
```

