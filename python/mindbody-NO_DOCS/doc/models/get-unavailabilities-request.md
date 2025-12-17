
# Get Unavailabilities Request

## Structure

`GetUnavailabilitiesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_ids` | `List[int]` | Optional | A list of requested staff IDs. |
| `start_date` | `datetime` | Optional | The start date of the requested date range.<br><br />Default: **today’s date** |
| `end_date` | `datetime` | Optional | The end date of the requested date range.<br><br />Default: **today’s date** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StaffIds": [
    135,
    134
  ],
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "Limit": 234,
  "Offset": 44
}
```

