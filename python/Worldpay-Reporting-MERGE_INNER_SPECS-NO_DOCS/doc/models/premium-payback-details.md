
# Premium Payback Details

Premium payback details.

## Structure

`PremiumPaybackDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `indicator_passed` | `bool` | Optional | Possible Values True or False |
| `eligible_bin` | `bool` | Optional | Possible Values True or False |
| `eligible` | `bool` | Optional | Possible Values True or False |
| `redemption_accepted` | `bool` | Optional | Possible Values True or False |
| `redemption_amount` | `float` | Optional | Refers to the price at which the issuing company will repurchase the bond from investors before its maturity date.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "indicatorPassed": false,
  "eligibleBIN": false,
  "eligible": false,
  "redemptionAccepted": false,
  "redemptionAmount": 200.0
}
```

