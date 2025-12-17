
# Goals Response

*This model accepts additional fields of type Any.*

## Structure

`GoalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_id` | `str` | Required | Unique identifier as presented in the request payload. |
| `goal_amt` | `List[float]` | Required | Original withdrawals associated with goals - as defined by a participant. |
| `start_date` | `str` | Required | Start date of a goal – as specified in the request payload. Valid Date Format: DD-MM-YYYY. |
| `end_date` | `str` | Required | End date of a goal – as specified in the request payload. Valid Date Format: DD-MM-YYYY. |
| `modified_goal_amt` | `List[float]` | Required | Withdrawals modified i.e., reduced – based on the modification logic. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "goalID": "Goal2",
  "goalAmt": [
    123.11,
    123.12
  ],
  "startDate": "01-12-2023",
  "endDate": "30-11-2025",
  "modifiedGoalAmt": [
    16.74,
    16.75,
    16.76
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

