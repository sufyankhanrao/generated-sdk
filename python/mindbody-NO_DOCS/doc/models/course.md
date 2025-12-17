
# Course

A course.

## Structure

`Course`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The course ID. |
| `name` | `str` | Optional | The course name. |
| `description` | `str` | Optional | A description of the course. |
| `notes` | `str` | Optional | Any notes that have been written about the course. |
| `start_date` | `datetime` | Optional | Date and time that the course starts. |
| `end_date` | `datetime` | Optional | Date and time that the course ends. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `organizer` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `program` | [`Program`](../../doc/models/program.md) | Optional | - |
| `image_url` | `str` | Optional | The URL of the image associated with this course, if one exists. |

## Example (as JSON)

```json
{
  "Id": 0,
  "Name": "Name6",
  "Description": "Description0",
  "Notes": "Notes2",
  "StartDate": "2016-03-13T12:52:32.123Z"
}
```

