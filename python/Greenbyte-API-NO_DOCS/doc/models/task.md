
# Task

A task.

## Structure

`Task`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `int` | Required | The id of a task.<br><br>**Constraints**: `>= 1` |
| `title` | `str` | Required | - |
| `created_by` | [`User`](../../doc/models/user.md) | Required | - |
| `description` | `str` | Optional | - |
| `category` | [`TaskCategory`](../../doc/models/task-category.md) | Optional | Basic information about a task category. |
| `priority` | [`TaskPriorityEnum`](../../doc/models/task-priority-enum.md) | Required | The priority of a task.<br><br>**Default**: `"medium"` |
| `timestamp_start` | `datetime` | Required | The timestamp when the task is/was planned to start. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `timestamp_end` | `datetime` | Required | The timestamp when the is/was planned to end. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `state` | [`TaskStateEnum`](../../doc/models/task-state-enum.md) | Required | The state of a task. |
| `resolved` | `bool` | Required | - |
| `timestamp_resolved` | `datetime` | Optional | The timestamp when the task was resolved. The timestamp is in the time zone configured in the Greenbyte Platform without UTC offset. |
| `device_ids` | `List[int]` | Optional | Ids of the devices assigned to the task.<br><br>**Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Optional | Ids of the sites assigned to the task.<br><br>**Constraints**: `>= 1` |
| `site_access_ids` | `List[int]` | Optional | Ids of the site accesses linked to the task.<br><br>**Constraints**: `>= 1` |
| `downtime_event_ids` | `List[int]` | Optional | Ids of the downtime events linked to the task.<br><br>**Constraints**: `>= 1` |
| `status_ids` | `List[int]` | Optional | Ids of the statuses linked to the task.<br><br>**Constraints**: `>= 1` |
| `number_of_comments` | `int` | Required | **Constraints**: `>= 0` |
| `comments` | [`List[TaskComment]`](../../doc/models/task-comment.md) | Optional | The comments belonging to the task. |
| `recurrence` | [`Recurrence`](../../doc/models/recurrence.md) | Optional | Recurrence settings for the task. To calculate when the<br>task is recurring, use the `timestampStart` field and<br>then add to it multiples of the specified interval; the<br>`intervalType` field determines if the task is recurring<br>on daily, weekly, monthly, or yearly basis.<br><br>If the task is not recurring, this field is null.<br><br>**Note:** Only the main (first) task in a recurring<br>series have recurrence settings. For the other tasks in<br>the series, the field `mainTaskId` can be used to find<br>it. |
| `main_task_id` | `int` | Optional | **Constraints**: `>= 1` |
| `assignee` | [TaskAssigneeUser](../../doc/models/task-assignee-user.md) \| [TaskAssigneePersonnel](../../doc/models/task-assignee-personnel.md) \| [TaskAssigneeManufacturer](../../doc/models/task-assignee-manufacturer.md) \| [TaskAssigneeOther](../../doc/models/task-assignee-other.md) \| None | Optional | This is a container for one-of cases. |
| `metadata` | [`List[MetadataField]`](../../doc/models/metadata-field.md) | Optional | A list of metadata fields and their values. |

## Example (as JSON)

```json
{
  "taskId": 208,
  "title": "Maintenance",
  "createdBy": {
    "firstName": "firstName2",
    "lastName": "lastName6"
  },
  "description": "Gearbox maintenance",
  "priority": "medium",
  "timestampStart": "01/01/2020 00:00:00",
  "timestampEnd": "01/08/2020 00:00:00",
  "state": "unresolved",
  "resolved": true,
  "timestampResolved": "01/08/2020 00:00:00",
  "numberOfComments": 3,
  "category": {
    "categoryId": 120,
    "title": "title2"
  },
  "deviceIds": [
    190,
    191,
    192
  ],
  "siteIds": [
    170
  ]
}
```

