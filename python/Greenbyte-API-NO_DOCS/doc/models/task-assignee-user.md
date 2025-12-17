
# Task Assignee User

## Structure

`TaskAssigneeUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | - |
| `last_name` | `str` | Required | - |
| `assignee_type` | [`TaskAssigneeTypeEnum`](../../doc/models/task-assignee-type-enum.md) | Required | The type of task assignee. |

## Example (as JSON)

```json
{
  "firstName": "firstName2",
  "lastName": "lastName6",
  "assigneeType": "user"
}
```

