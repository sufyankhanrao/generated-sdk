
# Class Description

Represents a class definition. The class meets at the start time, goes until the end time.

## Structure

`ClassDescription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | When `true`, indicates that the business can assign this class description to new class schedules.<br /><br>When `false`, indicates that the business cannot assign this class description to new class schedules. |
| `description` | `str` | Optional | The long version of the class description. |
| `id` | `int` | Optional | The class description's ID. |
| `image_url` | `str` | Optional | The class description's image URL, if any. If it does not exist, nothing is returned. |
| `last_updated` | `datetime` | Optional | The date this class description was last modified. |
| `level` | [`Level`](../../doc/models/level.md) | Optional | A session level. |
| `name` | `str` | Optional | The name of this class description. |
| `notes` | `str` | Optional | Any notes about the class description. |
| `prereq` | `str` | Optional | Any prerequisites for the class. |
| `program` | [`Program`](../../doc/models/program.md) | Optional | - |
| `session_type` | [`SessionType`](../../doc/models/session-type.md) | Optional | SessionType contains information about the session types in a business. |
| `category` | `str` | Optional | The category of this class description. |
| `category_id` | `int` | Optional | The category ID of this class description. |
| `subcategory` | `str` | Optional | The subcategory of this class description. |
| `subcategory_id` | `int` | Optional | The subcategory ID of this class description. |

## Example (as JSON)

```json
{
  "Active": false,
  "Description": "Description6",
  "Id": 110,
  "ImageURL": "ImageURL2",
  "LastUpdated": "2016-03-13T12:52:32.123Z"
}
```

