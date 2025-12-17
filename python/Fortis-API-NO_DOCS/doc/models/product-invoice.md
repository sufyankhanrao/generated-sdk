
# Product Invoice

Product Invoice Information on `expand`

## Structure

`ProductInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `36` |
| `quote_number_format` | `str` | Optional | Quote Number Format<br><br>**Constraints**: *Maximum Length*: `36` |
| `quote_number_start` | `float` | Optional | Quote Number Start<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `quote_number_increment` | `float` | Optional | Quote Number Increment<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `quote_number_current` | `float` | Optional | Quote Number Current |
| `invoice_number_format` | `str` | Optional | Invoice Number Format<br><br>**Constraints**: *Maximum Length*: `36` |
| `invoice_number_start` | `float` | Optional | Invoice Number Start<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `invoice_number_increment` | `float` | Optional | Invoice Number Increment<br><br>**Constraints**: `>= 1`, `<= 999999999` |
| `invoice_number_current` | `float` | Optional | Invoice Number Current |
| `tax_rate` | `float` | Optional | Tax Rate<br><br>**Constraints**: `>= 0`, `<= 99.99` |
| `tax_fee` | `int` | Optional | Tax Fee<br><br>**Constraints**: `<= 999999999999` |
| `monthly_fee` | `int` | Optional | Monthly Fees<br><br>**Constraints**: `>= 0`, `<= 99999` |
| `per_invoice_fee` | `int` | Optional | Per Invoice Fee<br><br>**Constraints**: `>= 0`, `<= 99999` |
| `per_quote_fee` | `int` | Optional | Per Quote fee<br><br>**Constraints**: `>= 0`, `<= 99999` |
| `require_pay_in_full` | `bool` | Optional | Require Pay In Full |
| `selectable` | `float` | Optional | Selectable |
| `reportable` | `float` | Optional | Reportable |
| `portfolio_id` | `str` | Optional | Portfolio Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `id` | `str` | Optional | Product Invoice Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "title": "Sample title",
  "quote_number_start": 1.0,
  "quote_number_increment": 1.0,
  "quote_number_current": 1.0,
  "invoice_number_start": 1,
  "invoice_number_increment": 1,
  "invoice_number_current": 1,
  "tax_rate": 0,
  "tax_fee": 0,
  "monthly_fee": 0,
  "per_invoice_fee": 0,
  "per_quote_fee": 0,
  "require_pay_in_full": true,
  "selectable": 1,
  "reportable": 1,
  "portfolio_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "quote_number_format": "quote_number_format6"
}
```

