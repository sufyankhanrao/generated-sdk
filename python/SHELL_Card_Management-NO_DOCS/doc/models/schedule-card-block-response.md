
# Schedule Card Block Response

## Structure

`ScheduleCardBlockResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main_reference` | `int` | Optional | Reference number for tracking the execution of the request.<br>Note: Reference will be empty for status 9006 and 9012 i.e., request for all the cards failed. |
| `request_id` | `str` | Optional | API Request ID |
| `status` | `str` | Optional | Overall Status of the API call |
| `data` | [`List[ScheduleCardBlockResponseDataItems]`](../../doc/models/schedule-card-block-response-data-items.md) | Optional | List of SubmittedScheduleCardBlockCard entity. |

## Example (as JSON)

```json
{
  "MainReference": 98,
  "RequestId": "RequestId4",
  "Status": "Status2",
  "Data": [
    {
      "CardId": 224,
      "FromDate": "FromDate2",
      "ToDate": "ToDate8",
      "ReferenceId": 108
    }
  ]
}
```

