
# Update Contact Log Request

## Structure

`UpdateContactLogRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The ID of the contact log being updated. |
| `test` | `bool` | Optional | When `true`, indicates that this is a test request and no data is inserted into the subscriber’s database.<br /><br>When `false`, the database is updated. |
| `assigned_to_staff_id` | `int` | Optional | The ID of the staff member to whom the contact log is now being assigned. |
| `text` | `str` | Optional | The contact log’s new text. |
| `contact_name` | `str` | Optional | The name of the new person to be contacted by the assigned staff member. |
| `followup_by_date` | `datetime` | Optional | The new date by which the assigned staff member should complete this contact log. |
| `contact_method` | `str` | Optional | The new method by which the client wants to be contacted. |
| `is_complete` | `bool` | Optional | When `true`, indicates that the contact log is complete.<br>When `false`, indicates the contact log isn’t complete. |
| `comments` | [`List[UpdateContactLogComment]`](../../doc/models/update-contact-log-comment.md) | Optional | Contains information about the comments being updated or added to the contact log. Comments that have an ID of `0` are added to the contact log. |
| `types` | [`List[UpdateContactLogType]`](../../doc/models/update-contact-log-type.md) | Optional | Contains information about the contact logs types being assigned to the contact log, in addition to the contact log types that are already assigned. |

## Example (as JSON)

```json
{
  "Id": 86,
  "Test": false,
  "AssignedToStaffId": 110,
  "Text": "Text8",
  "ContactName": "ContactName6"
}
```

