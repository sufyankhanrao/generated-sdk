
# Get Schedule Items Request

## Structure

`GetScheduleItemsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_ids` | `List[int]` | Optional | A list of requested location IDs. |
| `staff_ids` | `List[int]` | Optional | A list of requested staff IDs. |
| `start_date` | `datetime` | Optional | The start date of the requested date range.<br><br />Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date of the requested date range.<br><br />Default: **today’s date** |
| `ignore_prep_finish_times` | `bool` | Optional | When `true`, appointment preparation and finish unavailabilities are not returned.<br><br />Default: **false** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "LocationIds": [
    132,
    133
  ],
  "StaffIds": [
    47
  ],
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "IgnorePrepFinishTimes": false
}
```

