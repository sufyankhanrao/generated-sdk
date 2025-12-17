
# Summaries Inner

Summary details.

## Structure

`SummariesInner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `party` | `str` | Optional | Party is an individual or entity that is involved in a transaction.<br><br>**Constraints**: *Maximum Length*: `256` |
| `process_month` | `str` | Optional | Month for which the transactions are processed.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `total_processing_rate` | `float` | Optional | The fees that a business must pay each time when it accepts a payment from card.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_effective_rate` | `float` | Optional | The effective rate is that rate of interest actually earned on over the months.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "party": "Acquire",
  "processMonth": "2022-01",
  "totalProcessingRate": 5.54,
  "totalEffectiveRate": 1.57
}
```

