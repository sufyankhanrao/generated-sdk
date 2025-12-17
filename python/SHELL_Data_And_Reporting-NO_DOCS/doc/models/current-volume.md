
# Current Volume

## Structure

`CurrentVolume`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee_rule_id` | `int` | Optional | Bonus or association bonus configuration identifier that is associated to the payer |
| `fee_rule_description` | `str` | Optional | Bonus or association bonus configuration description that is associated to the payer. |
| `month` | `int` | Optional | Consumption(Volume) of the month. |
| `year` | `str` | Optional | Consumption (Volume) of the year. |
| `total_volume` | `float` | Optional | Total volume consumption for the month/year above. |

## Example (as JSON)

```json
{
  "FeeRuleId": 74,
  "FeeRuleDescription": "FeeRuleDescription8",
  "Month": 138,
  "Year": "Year2",
  "TotalVolume": 115.68
}
```

