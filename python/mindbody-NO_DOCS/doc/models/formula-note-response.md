
# Formula Note Response

An individual Client Formula Note.

## Structure

`FormulaNoteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The formula note ID. |
| `client_id` | `str` | Optional | The unique Id of the client for the formula note. This is the unique ID for the client in the site where the formula note originated. This is different than the ClientId specified in the request, which is the id for the client assigned by the business. |
| `appointment_id` | `int` | Optional | The appointment ID that the formula note is related to. |
| `entry_date` | `datetime` | Optional | The date formula note was created. |
| `note` | `str` | Optional | The new formula note text. |
| `site_id` | `int` | Optional | The site Id. |
| `site_name` | `str` | Optional | The site name. |
| `staff_first_name` | `str` | Optional | The first name of the staff for the optional associated appointment. If no appointment ID is provided, this will be null. |
| `staff_last_name` | `str` | Optional | The last name of the staff for the optional associated appointment. If no appointment ID is provided, this will be null. |
| `staff_display_name` | `str` | Optional | The display name of the staff for the optional associated appointment. If no appointment ID is provided, or no display name is specified for the staff member, this will be null. |

## Example (as JSON)

```json
{
  "Id": 160,
  "ClientId": "ClientId2",
  "AppointmentId": 8,
  "EntryDate": "2016-03-13T12:52:32.123Z",
  "Note": "Note4"
}
```

