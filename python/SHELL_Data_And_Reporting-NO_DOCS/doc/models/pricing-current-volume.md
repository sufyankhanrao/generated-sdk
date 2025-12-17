
# Pricing Current Volume

## Structure

`PricingCurrentVolume`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee_rule_id` | `int` | Optional | Bonus or association bonus configuration identifier  that is associated to the payer. |
| `fee_rule_description` | `str` | Optional | Bonus or association bonus configuration description that is associated to the payer |
| `price_rule_id` | `int` | Optional | Pricing current period Pricing Price Rule ID that is associated to the payer. |
| `price_rule_description` | `str` | Optional | Pricing current period pricing rule description that is associated to the payer |
| `total_volume` | `float` | Optional | Total volume consumption for the current period. |
| `next_fee_creation_date` | `str` | Optional | Next Fee Rule Creation Date for that is associated to the payer.<br>Format: YYYYMMDD |

## Example (as JSON)

```json
{
  "FeeRuleId": 134,
  "FeeRuleDescription": "FeeRuleDescription4",
  "PriceRuleID": 96,
  "PriceRuleDescription": "PriceRuleDescription6",
  "TotalVolume": 64.96
}
```

