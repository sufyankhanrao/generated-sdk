
# Task Assignee Other

Information about some other entity assigned to a task.

## Structure

`TaskAssigneeOther`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignee_type` | [`TaskAssigneeTypeEnum`](../../doc/models/task-assignee-type-enum.md) | Required | The type of task assignee. |
| `text` | `str` | Required | Free-text description of the assignee. |

## Example (as JSON)

```json
{
  "assigneeType": "user",
  "text": "text0"
}
```

