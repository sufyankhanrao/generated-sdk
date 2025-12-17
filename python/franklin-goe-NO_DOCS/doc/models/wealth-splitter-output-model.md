
# Wealth Splitter Output Model

*This model accepts additional fields of type Any.*

## Structure

`WealthSplitterOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | Status code for the response. |
| `message` | `str` | Required | Returns appropriate message for each status code. |
| `body` | `Any` | Required | - |
| `goal_response_list` | [`List[GoalResponseItem]`](../../doc/models/goal-response-item.md) | Required | Optimal wealth split details for all goals |
| `request_type` | `str` | Required | - |
| `resp_time` | `float` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statusCode": 200,
  "message": "Success",
  "body": {
    "key1": "val1",
    "key2": "val2"
  },
  "goal_response_list": [
    {
      "Goal_ID": "Goal1",
      "Goal": "Saving",
      "Orig_Curr_Wealth": 141412.0,
      "Min_Initial_Needed": 1114000.0,
      "Wealth_Split": 1038906.0,
      "Shortfall": -75094.0,
      "Funded_Status": "Underfunded",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "requestType": "requestType0",
  "respTime": 118.24,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

