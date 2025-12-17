
# Task Comment

A comment added to a task.

## Structure

`TaskComment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comment_id` | `int` | Required | The id of a task comment.<br><br>**Constraints**: `>= 1` |
| `task_id` | `int` | Required | The id of a task.<br><br>**Constraints**: `>= 1` |
| `text` | `str` | Required | - |
| `timestamp_created` | `datetime` | Required | The timestamp when the comment was created (added to the<br>task). The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `created_by` | [`User`](../../doc/models/user.md) | Required | - |

## Example (as JSON)

```json
{
  "commentId": 140,
  "taskId": 172,
  "text": "Task updated",
  "timestampCreated": "01/01/2020 00:00:00",
  "createdBy": {
    "firstName": "firstName2",
    "lastName": "lastName6"
  }
}
```

