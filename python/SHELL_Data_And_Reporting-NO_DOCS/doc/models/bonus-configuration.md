
# Bonus Configuration

## Structure

`BonusConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_account_id` | `int` | Optional | Account identifier of the Pricing Account associated with the Payer. |
| `pricing_account_number` | `str` | Optional | Account number of the Pricing Account associated with the Payer. |
| `pricing_account_short_name` | `str` | Optional | Short name of the Pricing Account associated with the Payer. |
| `pricing_account_full_name` | `str` | Optional | Full name of the Pricing Account associated with the Payer. |
| `fee_rule_id` | `int` | Optional | Bonus or association bonus configuration identifier that is associated to the payer. |
| `fee_rule_description` | `str` | Optional | Bonus or association bonus configuration description that is associated to the payer. |
| `fee_rule_date_effective` | `str` | Optional | The bonus or association bonus configuration becomes effective on the payer from this date.<br>Format: YYYYMMDD |
| `fee_rule_date_terminated` | `str` | Optional | The bonus or association bonus configuration is terminated for the payer on this date.<br>Format: YYYYMMDD |
| `bonus_paid_to` | `str` | Optional | Configuration to specify how the bonus is paid.<br>Format: ID-Description<br>Example:<br>1-Pay to Payer<br>2-Pay to invoice levels before the payer<br>3-Pay to specific customer<br>4-Pay to Association Customer<br>5-Pay to Associated Customers |
| `bonus_paid_to_account_id` | `int` | Optional | Account identifier of the specific account to which the bonus is paid back |
| `bonus_paid_to_account_number` | `str` | Optional | Account number of the specific account to which the bonus is paid back |
| `bonus_paid_to_account_short_name` | `str` | Optional | Short name of the specific account to which the bonus is paid back |
| `bonus_paid_to_account_full_name` | `str` | Optional | Full name of the specific account to which the bonus is paid back |
| `frequency` | `str` | Optional | Frequency of the configuration.<br>Format: ID-Description<br>Examples:<br>1-Daily (all days)<br>2-Daily (only working days)<br>3-Weekly – Monday |
| `next_calculation_date` | `str` | Optional | The next bonus is calculated for the payer on this date.<br>Format: YYYYMMDD |
| `previous_calculated_date` | `str` | Optional | The previous bonus was calculated for the payer on this date.<br>Format: YYYYMMDD |
| `fee_rule_basis` | `str` | Optional | Fee Rule Basis configured.<br>Format: ID-Description<br>Example:<br>1-Currency Per Unit<br>2-Percentage of Uplift<br>3-Lump Sum |
| `fee_rule_currency_code` | `str` | Optional | ISO currency code of the currency configured in the Bonus Configuration, if any. |
| `fee_rule_currency_symbol` | `str` | Optional | Currency symbol of the currency configured in the Bonus Configuration, if any. |
| `fee_rule_available_from` | `str` | Optional | This bonus or association bonus is available from this date.<br>Format: YYYYMMDD |
| `fee_rule_available_to` | `str` | Optional | This bonus or association bonus configuration will not be available from this date.<br>Format: YYYYMMDD |
| `fee_rule_locations` | [`List[FeeRuleLocation]`](../../doc/models/fee-rule-location.md) | Optional | - |
| `fee_rule_tiers` | [`List[FeeRuleTier]`](../../doc/models/fee-rule-tier.md) | Optional | - |
| `associated_accounts` | [`List[AssociatedAccount]`](../../doc/models/associated-account.md) | Optional | - |
| `fee_rule_products` | [`List[FeeRuleProduct]`](../../doc/models/fee-rule-product.md) | Optional | - |

## Example (as JSON)

```json
{
  "PricingAccountId": 80,
  "PricingAccountNumber": "PricingAccountNumber0",
  "PricingAccountShortName": "PricingAccountShortName2",
  "PricingAccountFullName": "PricingAccountFullName8",
  "FeeRuleId": 12
}
```

