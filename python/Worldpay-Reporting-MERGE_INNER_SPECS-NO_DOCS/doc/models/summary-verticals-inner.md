
# Summary Verticals Inner

Summary for verticals.

## Structure

`SummaryVerticalsInner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vertical` | [`Vertical3Enum`](../../doc/models/vertical-3-enum.md) | Optional | Indicates a specific industry or market carried out by the Organization<br><br>**Constraints**: *Maximum Length*: `15` |
| `process_month` | `str` | Optional | Month for which the transactions are processed.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `total_effective_rate` | `float` | Optional | The effective rate is that rate of interest actually earned on over the months.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_processing_rate` | `float` | Optional | The fees that a business must pay each time when it accepts a payment from card.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "vertical": "B2B",
  "processMonth": "2022-01",
  "totalEffectiveRate": 10.81,
  "totalProcessingRate": 42.64
}
```

