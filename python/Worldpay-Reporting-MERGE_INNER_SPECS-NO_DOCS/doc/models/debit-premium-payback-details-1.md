
# Debit Premium Payback Details 1

This object provides information on payback related details

## Structure

`DebitPremiumPaybackDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `indicator_passed` | `bool` | Optional | Possible Values True or False |
| `eligible_bin` | `bool` | Optional | Possible Values True or False |
| `eligible` | `bool` | Optional | Possible Values True or False |
| `redemption_accepted` | `bool` | Optional | Possible Values True or False |
| `redemption_amount` | `str` | Optional | This field indicates the early repayment charges.<br><br>**Constraints**: *Maximum Length*: `15` |

## Example (as JSON)

```json
{
  "indicatorPassed": false,
  "eligibleBIN": false,
  "eligible": false,
  "redemptionAccepted": false,
  "redemptionAmount": "200.56"
}
```

