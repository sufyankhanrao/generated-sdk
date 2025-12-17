
# Bonus History

## Structure

`BonusHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | Payer Id |
| `payer_number` | `str` | Optional | Payer Number of the selected payer |
| `payer_short_name` | `str` | Optional | Payer short name. |
| `payer_full_name` | `str` | Optional | Payer full name. |
| `account_id` | `int` | Optional | Account Id |
| `account_number` | `str` | Optional | Account Number of the selected payer. |
| `account_short_name` | `str` | Optional | Account short name. |
| `account_full_name` | `str` | Optional | Account full name. |
| `invoice_account_id` | `int` | Optional | Invoice Account Id |
| `invoice_account_number` | `str` | Optional | Invoice Account Number of the selected payer. |
| `invoice_account_short_name` | `str` | Optional | Invoice Account short name. |
| `invoice_account_full_name` | `str` | Optional | Invoice Account full name. |
| `fee_rule_id` | `str` | Optional | Bonus or association bonus configuration identifier |
| `fee_rule_description` | `str` | Optional | Bonus or association bonus configuration description that is associated to the bonus fee item |
| `from_date` | `str` | Optional | Bonus was calculated from this date.<br>Format: YYYYMMDD |
| `to_date` | `str` | Optional | Bonus was calculated till this date.<br>Format: YYYYMMDD |
| `bonus_paid_to` | `str` | Optional | Specifies how the bonus was paid back.<br>Format: ID-Description<br>Example:<br>1-Pay to Payer<br>2-Pay to invoice levels before the payer<br>3-Pay to specific customer<br>4-Pay to Association Customer<br>5-Pay to Associated Customers |
| `fee_item_id` | `int` | Optional | Bonus fee item identifier. |
| `fee_rule_basis` | `str` | Optional | Fee Rule Basis of the bonus fee item.<br>Format: ID-Description<br>Example:<br>1-Currency Per Unit<br>2-Percentage of Uplift<br>3-Lump Sum |
| `fee_item_currency_code` | `str` | Optional | ISO currency code of the currency in which Bonus is paid.<br>Example: GBP |
| `fee_item_currency_symbol` | `str` | Optional | Currency symbol of the currency in which Bonus is paid. |
| `prorated_volume` | `float` | Optional | Prorated volume considered under the account as  configured for the bonus association. |
| `total_volume` | `float` | Optional | Total volume considered for calculating the bonus. |
| `fee_product` | `str` | Optional | Product as shown in the invoice for the bonus paid.<br>Format: ID-Description<br>Example: 1562-Bonus diesel Shell Netherlands on agreed site(s) |
| `invoice_gross_amount` | `float` | Optional | Gross Amount – Bonus Paid including VAT as shown on the Invoice |
| `invoice_net_amount` | `float` | Optional | Net Amount – Bonus Paid excluding VAT as shown on the Invoice |
| `invoice_vat_amount` | `float` | Optional | VAT calculated for the bonus paid as shown on the Invoice |
| `is_fee_cancelled` | `bool` | Optional | True/False<br>True if bonus is generated but cancelled. When true, consider this as not paid. |
| `fee_item_tier_prorated_volume` | `float` | Optional | Prorated volume in the bonus fee item tier. |
| `fee_item_tier_total_volume` | `float` | Optional | Total volume in the bonus fee item tier. |
| `tier_minimum` | `int` | Optional | Tier minimum value considered for calculation |
| `tier_rate` | `float` | Optional | Tier rate considered for calculation |

## Example (as JSON)

```json
{
  "PayerId": 240,
  "PayerNumber": "PayerNumber0",
  "PayerShortName": "PayerShortName4",
  "PayerFullName": "PayerFullName0",
  "AccountId": 44
}
```

