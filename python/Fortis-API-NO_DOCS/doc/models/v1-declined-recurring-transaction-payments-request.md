
# V1 Declined Recurring Transaction Payments Request

## Structure

`V1DeclinedRecurringTransactionPaymentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `declined_recurring_transaction_id` | `str` | Required | Declined Recurring Transaction Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `account_number` | `str` | Required | Account Number<br><br>**Constraints**: *Minimum Length*: `13`, *Maximum Length*: `19` |
| `account_holder_name` | `str` | Optional | Account Holder Name |
| `exp_date` | `str` | Required | Exp Date<br><br>**Constraints**: *Maximum Length*: `4` |
| `transaction_amount` | `int` | Required | Transaction Amount<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `description` | `str` | Optional | Description<br><br>**Constraints**: *Maximum Length*: `255` |
| `billing_address` | [`BillingAddress`](../../doc/models/billing-address.md) | Optional | Billing Address Object |
| `tags` | `List[str]` | Optional | Tags |
| `replace_account_vault` | `bool` | Optional | Replace AccountVault |
| `save_account` | `bool` | Optional | Specifies to save account to contacts profile if account_number/track_data is present with either contact_id or contact_api_id in params. |
| `save_account_title` | `str` | Optional | If saving token while running a transaction, this will be the title of the token.<br><br>**Constraints**: *Maximum Length*: `16` |
| `subtotal_amount` | `int` | Optional | Subtotal Amount<br><br>**Constraints**: `>= 0`, `<= 999999999` |
| `surcharge_amount` | `int` | Optional | Surcharge Amount<br><br>**Constraints**: `>= 0`, `<= 999999999` |

## Example (as JSON)

```json
{
  "declined_recurring_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "account_number": "5454545454545454",
  "account_holder_name": "John Doe",
  "exp_date": "0722",
  "transaction_amount": 0,
  "description": "Description",
  "save_account_title": "John Account",
  "subtotal_amount": 599,
  "surcharge_amount": 599,
  "billing_address": {
    "postal_code": "postal_code0",
    "street": "street8",
    "city": "city2",
    "state": "state6",
    "phone": "phone2"
  },
  "tags": [
    "tags3"
  ],
  "replace_account_vault": false
}
```

