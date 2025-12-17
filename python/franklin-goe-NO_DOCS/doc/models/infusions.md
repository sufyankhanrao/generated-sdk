
# Infusions

*This model accepts additional fields of type Any.*

## Structure

`Infusions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `int` | Required | The minimum amount of funds that the investor is willing to place at a chosen (monthly/yearly) interval. The investor will place these funds starting one interval period (i.e. one month/year) after the initial investment is placed into the fund until one interval period before the final withdrawal takes place (i.e. before the end of the goal tenure). For example, an investor with a five-year goal tenure and yearly infusions of $1000 will contribute $1000 at years 2, 3, and 4 of the goal tenure. |
| `max` | `int` | Required | The maximum amount of funds that the investor is willing to place at a chosen (monthly/yearly) interval. The investor will place these funds starting one interval period (i.e. one month/year) after the initial investment is placed into the fund until one interval period before the final withdrawal takes place (i.e. before the end of the goal tenure). For example, an investor with a five-year goal tenure and yearly infusions of $1000 will contribute $1000 at years 2, 3, and 4 of the goal tenure. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "min": 180,
  "max": 98,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

