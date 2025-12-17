
# Get Classes Request

## Structure

`GetClassesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_description_ids` | `List[int]` | Optional | The requested class description IDs. |
| `class_ids` | `List[int]` | Optional | The requested class IDs. |
| `class_schedule_ids` | `List[int]` | Optional | The requested classSchedule Ids. |
| `staff_ids` | `List[int]` | Optional | The requested IDs of the teaching staff members. |
| `start_date_time` | `datetime` | Optional | The requested start date for filtering. This also determines what you will see for the ‘BookingWindow’ StartDateTime in the response. For example, if you pass a StartDateTime that is on OR before the BookingWindow ‘Open’ days of the class, you will retrieve the actual ‘StartDateTime’ for the Booking Window. If you pass a StartDateTime that is after the BookingWindow ‘date’, then you will receive results based on that start date. |
| `end_date_time` | `datetime` | Optional | The requested end date for filtering.<br><br />Default: **today’s date** |
| `client_id` | `str` | Optional | The client ID of the client who is viewing this class list. Based on identity, the client may be able to see additional information, such as membership specials. |
| `program_ids` | `List[int]` | Optional | A list of program IDs on which to base the search. |
| `session_type_ids` | `List[int]` | Optional | A list of session type IDs on which to base the search. |
| `location_ids` | `List[int]` | Optional | A list of location IDs on which to base the search. |
| `semester_ids` | `List[int]` | Optional | A list of semester IDs on which to base the search. |
| `hide_canceled_classes` | `bool` | Optional | When `true`, canceled classes are removed from the response.<br /><br>When `false`, canceled classes are included in the response.<br /><br>Default: **false** |
| `scheduling_window` | `bool` | Optional | When `true`, classes outside scheduling window are removed from the response.<br /><br>When `false`, classes are included in the response, regardless of the scheduling window.<br /><br>Default: **false** |
| `last_modified_date` | `datetime` | Optional | When included in the request, only records modified on or after the `LastModifiedDate` specified are included in the response. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClassDescriptionIds": [
    153,
    152,
    151
  ],
  "ClassIds": [
    177
  ],
  "ClassScheduleIds": [
    186
  ],
  "StaffIds": [
    65,
    66,
    67
  ],
  "StartDateTime": "2016-03-13T12:52:32.123Z"
}
```

