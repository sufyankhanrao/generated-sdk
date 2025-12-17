
# Update Staff Request

## Structure

`UpdateStaffRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | The unique ID of the staff member. |
| `first_name` | `str` | Optional | The staff member first name. You must specify a first name when you add a staff member. |
| `last_name` | `str` | Optional | The staff member last name. You must specify a last name when you add a staff member. |
| `email` | `str` | Optional | The staff member’s email address. |
| `is_male` | `bool` | Optional | When `true`, indicates that the staff member is male.<br>When `false`, indicates that the staff member is female. |
| `home_phone` | `str` | Optional | The staff member’s home phone number. |
| `work_phone` | `str` | Optional | The staff member’s work phone number. |
| `mobile_phone` | `str` | Optional | The staff member’s mobile phone number. |
| `bio` | `str` | Optional | The staff member’s biography. This string contains HTML. |
| `address` | `str` | Optional | The first line of the staff member street address |
| `address_2` | `str` | Optional | The second line of the staff member street address, if needed. |
| `city` | `str` | Optional | The staff member’s city. |
| `state` | `str` | Optional | The staff member’s state. |
| `country` | `str` | Optional | The staff member’s country. |
| `postal_code` | `str` | Optional | The staff member’s postal code. |
| `class_assistant` | `bool` | Optional | When `true`, indicates that the staff member can be a class assistant. |
| `class_assistant_2` | `bool` | Optional | When `true`, indicates that the staff member can be a class assistant. |
| `independent_contractor` | `bool` | Optional | When `true`, indicates that the staff member is an independent contractor.<br>When `false`, indicates that the staff member is not an independent contractor. |
| `appointment_instructor` | `bool` | Optional | When `true`, indicates that the staff member offers appointments.<br /><br>When `false`, indicates that the staff member does not offer appointments. |
| `always_allow_double_booking` | `bool` | Optional | When `true`, indicates that the staff member can be scheduled for overlapping services.<br /><br>When `false`, indicates that the staff member does not offer appointments. |
| `class_teacher` | `bool` | Optional | When `true`, indicates that the staff member can teach classes.<br>When `false`, indicates that the staff member cannot teach classes. |
| `employment_start` | `datetime` | Optional | The start date of employment |
| `employment_end` | `datetime` | Optional | The end date of employment |
| `sort_order` | `int` | Optional | If configured by the business owner, this field determines a staff member’s weight when sorting. Use this field to sort staff members on your interface. |
| `provider_i_ds` | `List[str]` | Optional | A list of providerIDs for the staff.  In the US it is one per staff and is numeric, otherwise it can be a list and is alpha-numeric<br>for more information see <a href=" https://support.mindbodyonline.com/s/article/204075743-Provider-IDs?language=en_US" target="blank">Provider IDs</a> |
| `active` | `bool` | Optional | Indicates if the staff member is active. Staff member cannot be deactivated if they have future classes or appointments. |
| `notes` | `str` | Optional | Staff Member Private Notes |
| `emp_id` | `str` | Optional | The custom staff ID assigned to the staff member. |

## Example (as JSON)

```json
{
  "ID": 160,
  "FirstName": "FirstName8",
  "LastName": "LastName2",
  "Email": "Email8",
  "IsMale": false,
  "HomePhone": "HomePhone8"
}
```

