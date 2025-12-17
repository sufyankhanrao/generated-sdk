
# Goal Tenure 2

Defines the duration, in years, between the initial investment being placed in the portfolio and the investor's last withdrawal (at which point the funds in the portfolio are zero). The investor may make infusions during this time into/out of the portfolio. The `min`/`max` values represent the minimum and maximum goal tenures that the investor is considering. The `max` value must be more or equal to the `min` value, and the `min` value must be positive.

*This model accepts additional fields of type Any.*

## Structure

`GoalTenure2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `int` | Required | The minimum duration, in years, between the initial investment being placed in the portfolio and the investor's date of last withdrawal. The investor may make infusions during this time into/out of the portfolio. This value must be a positive integer.<br><br>**Constraints**: `>= 0` |
| `max` | `int` | Required | The maximum duration, in years, between the initial investment being placed in the portfolio and the investor's date of last withdrawal. The investor may make infusions during this time into/out of the portfolio. This value must be more or equal to the minimum duration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "min": 36,
  "max": 210,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

