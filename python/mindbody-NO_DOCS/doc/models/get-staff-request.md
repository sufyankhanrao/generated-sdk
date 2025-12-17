
# Get Staff Request

## Structure

`GetStaffRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_ids` | `List[int]` | Optional | A list of the requested staff IDs. |
| `filters` | `List[str]` | Optional | Filters to apply to the search. Possible values are:<br><br>* StaffViewable<br>* AppointmentInstructor<br>* ClassInstructor<br>* Male<br>* Female |
| `session_type_id` | `int` | Optional | Return only staff members that are available for the specified session type. You must supply a valid `StartDateTime` and `LocationID` to use this parameter. |
| `start_date_time` | `datetime` | Optional | Return only staff members that are available at the specified date and time. You must supply a valid `SessionTypeID` and `LocationID` to use this parameter. |
| `location_id` | `int` | Optional | Return only staff members that are available at the specified location. You must supply a valid `SessionTypeID` and `StartDateTime` to use this parameter. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StaffIds": [
    83
  ],
  "Filters": [
    "Filters1",
    "Filters2"
  ],
  "SessionTypeId": 190,
  "StartDateTime": "2016-03-13T12:52:32.123Z",
  "LocationId": 166
}
```

