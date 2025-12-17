
# Contact Log

A contact log.

## Structure

`ContactLog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The contact log’s ID. |
| `text` | `str` | Optional | The contact log’s body text. |
| `created_date_time` | `datetime` | Optional | The local date and time when the contact log was created. |
| `followup_by_date` | `datetime` | Optional | The date by which the assigned staff member should close or follow up on this contact log. |
| `contact_method` | `str` | Optional | The method by which the client wants to be contacted. |
| `contact_name` | `str` | Optional | The name of the client to contact. |
| `client` | [`Client`](../../doc/models/client.md) | Optional | The Client. |
| `created_by` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `assigned_to` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `comments` | [`List[ContactLogComment]`](../../doc/models/contact-log-comment.md) | Optional | Information about the comment. |
| `types` | [`List[ContactLogType]`](../../doc/models/contact-log-type.md) | Optional | Information about the type of contact log. |

## Example (as JSON)

```json
{
  "Id": 128,
  "Text": "Text2",
  "CreatedDateTime": "2016-03-13T12:52:32.123Z",
  "FollowupByDate": "2016-03-13T12:52:32.123Z",
  "ContactMethod": "ContactMethod6"
}
```

