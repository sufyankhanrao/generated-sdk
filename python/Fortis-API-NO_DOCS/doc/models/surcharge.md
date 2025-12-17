
# Surcharge

Surcharge Information on `expand`

## Structure

`Surcharge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `surcharge_fee` | `int` | Optional | Surcharge Fee |
| `surcharge_rate` | `int` | Optional | Surcharge Rate |
| `max_transaction_amount` | `int` | Optional | Max Transaction Amount |
| `min_fee_amount` | `int` | Optional | Min Fee Amount |
| `max_fee_amount` | `int` | Optional | Max Fee Amount |
| `surcharge_on_recurring` | `bool` | Optional | Surcharge On Recurring |
| `refund_surcharges` | `bool` | Optional | Refund Surcharges |
| `product_transaction_id` | `str` | Optional | Product Transaction Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `run_as_separate_transaction` | `bool` | Optional | Run As Separate Transaction |
| `apply_to_user_type_id` | `str` | Optional | Apply To User Type Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `256` |
| `surcharge_label` | `str` | Optional | Surcharge Label<br><br>**Constraints**: *Maximum Length*: `64` |
| `surcharge_transaction_product_id` | `str` | Optional | Surcharge Transaction Product Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `state_exception_check` | `bool` | Optional | State Exception Check |
| `compliant` | `bool` | Optional | Compliant |
| `id` | `str` | Optional | Surcharge Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |

## Example (as JSON)

```json
{
  "surcharge_fee": 10,
  "surcharge_rate": 1,
  "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "apply_to_user_type_id": "11e95f8ec39de8fbdb0a4f1a",
  "surcharge_transaction_product_id": "11e95f8ec39de8fbdb0a4f1a",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "max_transaction_amount": 252,
  "min_fee_amount": 198,
  "max_fee_amount": 172
}
```

