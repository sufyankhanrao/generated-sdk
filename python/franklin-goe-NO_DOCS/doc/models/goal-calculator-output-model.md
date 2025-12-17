
# Goal Calculator Output Model

*This model accepts additional fields of type Any.*

## Structure

`GoalCalculatorOutputModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `int` | Required | Status code for the response. |
| `message` | `str` | Required | Returns appropriate message for each status code. |
| `body` | `Any` | Required | - |
| `infusions` | `List[float]` | Required | - |
| `request_type` | `str` | Required | - |
| `goal_amt` | `float` | Required | - |
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
  "infusions": [
    7500.0,
    7500.0,
    7500.0,
    7500.0,
    7500.0,
    7500.0
  ],
  "requestType": "requestType2",
  "goalAmt": 42.06,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

