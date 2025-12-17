
# Task Assignee Personnel

## Structure

`TaskAssigneePersonnel`

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
| `assignee_type` | [`TaskAssigneeTypeEnum`](../../doc/models/task-assignee-type-enum.md) | Required | The type of task assignee. |

## Example (as JSON)

```json
{
  "personnelId": 22,
  "firstName": "firstName2",
  "lastName": "lastName0",
  "email": "email0",
  "phone": "phone6",
  "assigneeType": "user"
}
```

