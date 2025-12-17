
# Site Access Personnel

Site access personnel.

## Structure

`SiteAccessPersonnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `personnel_id` | `int` | Optional | The id of a person in the personnel list.<br><br>**Constraints**: `>= 1` |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `company` | `str` | Optional | - |
| `phone_number` | `str` | Optional | - |
| `vehicle_registration` | `str` | Optional | - |
| `comment` | `str` | Optional | - |
| `timestamp_start` | `datetime` | Optional | - |
| `timestamp_end` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "personnelId": 138,
  "firstName": "firstName8",
  "lastName": "lastName0",
  "company": "company4",
  "phoneNumber": "phoneNumber4"
}
```

