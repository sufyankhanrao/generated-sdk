
# Contact Log Comment

A contact log comment.

## Structure

`ContactLogComment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The comment’s ID. |
| `text` | `str` | Optional | The comment’s body text. |
| `created_date_time` | `datetime` | Optional | The local time when the comment was created. |
| `created_by` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |

## Example (as JSON)

```json
{
  "Id": 50,
  "Text": "Text4",
  "CreatedDateTime": "2016-03-13T12:52:32.123Z",
  "CreatedBy": {
    "Address": "Address0",
    "AppointmentInstructor": false,
    "AlwaysAllowDoubleBooking": false,
    "Bio": "Bio4",
    "City": "City0"
  }
}
```

