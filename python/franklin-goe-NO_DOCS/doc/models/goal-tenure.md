
# Goal Tenure

*This model accepts additional fields of type Any.*

## Structure

`GoalTenure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `int` | Required | The minimum duration, in years, between the initial investment being placed in the portfolio and the investor's date of last withdrawal. The investor may make infusions during this time into/out of the portfolio. This value must be a positive integer.<br><br>**Constraints**: `>= 0` |
| `max` | `int` | Required | The maximum duration, in years, between the initial investment being placed in the portfolio and the investor's date of last withdrawal. The investor may make infusions during this time into/out of the portfolio. This value must be more or equal to the minimum duration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "min": 62,
  "max": 236,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

