
# Get Contact Logs Request

## Structure

`GetContactLogsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client whose contact logs are being requested. |
| `start_date` | `datetime` | Optional | Filters the results to contact logs created on or after this date.<br /><br>Default: **the current date** |
| `end_date` | `datetime` | Optional | Filters the results to contact logs created before this date.<br /><br>Default: **the start date** |
| `staff_ids` | `List[int]` | Optional | Filters the results to return contact logs assigned to one or more staff IDs. |
| `show_system_generated` | `bool` | Optional | When `true`, system-generated contact logs are returned in the results.<br /><br>Default: **false** |
| `type_ids` | `List[int]` | Optional | Filters the results to contact logs assigned one or more of these type IDs. |
| `subtype_ids` | `List[int]` | Optional | Filters the results to contact logs assigned one or more of these subtype IDs. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "StaffIds": [
    59
  ],
  "ShowSystemGenerated": false,
  "TypeIds": [
    51,
    52
  ]
}
```

