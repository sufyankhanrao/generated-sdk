
# Transaction Reference

## Structure

`TransactionReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `transaction_id` | `str` | Optional | Transaction ID |
| `previous_transaction_id` | `str` | Optional | Previous Transaction ID |
| `transaction_amount` | `int` | Optional | Transaction Amount |
| `previous_transaction_amount` | `int` | Optional | Previous Transaction Amount |
| `previous_transaction_created_ts` | `float` | Optional | Previous Transaction Created Timestamp |
| `reference_type` | `str` | Optional | Reference Type |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "transaction_id": "transaction_id2",
  "previous_transaction_id": "previous_transaction_id8",
  "transaction_amount": 188,
  "previous_transaction_amount": 176
}
```

