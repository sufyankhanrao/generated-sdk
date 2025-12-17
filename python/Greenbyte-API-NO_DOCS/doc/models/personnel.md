
# Personnel

A person in the personnel list.

## Structure

`Personnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `personnel_id` | `int` | Optional | The id of a person in the personnel list.<br><br>**Constraints**: `>= 1` |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `phone` | `str` | Optional | - |
| `mobile` | `str` | Optional | - |
| `organization` | [`Organization`](../../doc/models/organization.md) | Optional | An organization used for tasks and personnel. |
| `qualifications` | [`List[PersonnelQualification]`](../../doc/models/personnel-qualification.md) | Optional | - |
| `site_inductions` | [`List[PersonnelSiteInduction]`](../../doc/models/personnel-site-induction.md) | Optional | - |

## Example (as JSON)

```json
{
  "personnelId": 196,
  "firstName": "firstName4",
  "lastName": "lastName4",
  "email": "email6",
  "phone": "phone0"
}
```

