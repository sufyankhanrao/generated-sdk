
# Staff 1

## Structure

`Staff1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The ID assigned to the staff member. |
| `first_name` | `str` | Optional | The staff member’s first name. |
| `last_name` | `str` | Optional | The staff member’s last name. |
| `display_name` | `str` | Optional | The display name of the staff member. |
| `email` | `str` | Optional | The staff member’s email address. |
| `bio` | `str` | Optional | The staff member’s biography. This string contains HTML. |
| `address` | `str` | Optional | The address of the staff member who is teaching the class. |
| `address_2` | `str` | Optional | The address2 of the staff member who is teaching the class. |
| `city` | `str` | Optional | The staff member’s city. |
| `state` | `str` | Optional | The staff member’s state. |
| `postal_code` | `str` | Optional | The staff member’s postal code. |
| `foreign_zip` | `str` | Optional | The staff member’s Foreign Zip code. |
| `country` | `str` | Optional | The staff member’s country. |
| `work_phone` | `str` | Optional | The staff member’s work phone number. |
| `home_phone` | `str` | Optional | The staff member’s home phone number. |
| `cell_phone` | `str` | Optional | The staff member’s mobile phone number. |
| `active` | `bool` | Optional | When `true`, indicates that the staff member is Active.<br>When `false`, indicates that the staff member is not Active. |
| `is_system` | `bool` | Optional | When `true`, indicates that the staff member is a system .<br>When `false`, indicates that the staff member is not system. |
| `smode_id` | `int` | Optional | The Staff's Smode Id |
| `appointment_trn` | `bool` | Optional | When `true`, indicates that the staff member offers appointments.<br>When `false`, indicates that the staff member does not offer appointments. |
| `always_allow_double_booking` | `bool` | Optional | When `true`, indicates that the staff member can be scheduled for overlapping services.<br>When `false`, indicates that the staff can only be scheduled for one service at a time in any given time-frame. |
| `independent_contractor` | `bool` | Optional | When `true`, indicates that the staff member is an independent contractor.<br>When `false`, indicates that the staff member is not an independent contractor. |
| `image_url` | `str` | Optional | The URL of the staff member’s image, if one has been uploaded. |
| `is_male` | `bool` | Optional | When `true`, indicates that the staff member is male.<br>When `false`, indicates that the staff member is female. |
| `reservation_trn` | `bool` | Optional | When `true`, indicates that the staff member offers Reservation.<br>When `false`, indicates that the staff member does not offer Reservation. |
| `sort_order` | `int` | Optional | If configured by the business owner, this field determines a staff member’s weight when sorting. Use this field to sort staff members on your interface. |
| `multi_location_permission` | `bool` | Optional | When `true`, indicates that the staff member has Multi Location Permission.<br>When `false`, indicates that the staff member does not has Multi Location Permission. |
| `name` | `str` | Optional | The staff member’s name. |
| `provider_i_ds` | `List[str]` | Optional | A list of ProviderIds for the staff. |
| `staff_settings` | [`StaffSetting`](../../doc/models/staff-setting.md) | Optional | contains the information about the staff settings. |
| `rep` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 1 else `false`. |
| `rep_2` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 2 else `false`. |
| `rep_3` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 3 else `false`. |
| `rep_4` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 4 else `false`. |
| `rep_5` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 5 else `false`. |
| `rep_6` | `bool` | Optional | When `true`, indicates that the staff is sales Rep 6 else `false`. |
| `assistant` | `bool` | Optional | When `true`, indicates that the staff is assistant.<br>When `false`, indicates that the staff is not assistant. |
| `assistant_2` | `bool` | Optional | When `true`, indicates that the staff is assistant2.<br>When `false`, indicates that the staff is not assistant2. |
| `employment_start` | `datetime` | Optional | The start date of employment. |
| `employment_end` | `datetime` | Optional | The end date of employment. |
| `emp_id` | `str` | Optional | The custom staff ID assigned to the staff member. |
| `appointments` | [`List[Appointment1]`](../../doc/models/appointment-1.md) | Optional | A list of appointments for the staff. |
| `unavailabilities` | [`List[Unavailability1]`](../../doc/models/unavailability-1.md) | Optional | A list of unavailabilities for the staff. |
| `availabilities` | [`List[Availability1]`](../../doc/models/availability-1.md) | Optional | A list of availabilities for the staff. |
| `login_locations` | [`List[Location1]`](../../doc/models/location-1.md) | Optional | A list of LoginLocations for the staff |

## Example (as JSON)

```json
{
  "Id": 94,
  "FirstName": "FirstName6",
  "LastName": "LastName4",
  "DisplayName": "DisplayName8",
  "Email": "Email6"
}
```

