
# Response Declined Recurring Transaction Payment

## Structure

`ResponseDeclinedRecurringTransactionPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type20Enum`](../../doc/models/type-20-enum.md) | Optional | Resource Type<br><br>**Default**: `"DeclinedRecurringTransactionPayment"` |
| `data` | [`Data4`](../../doc/models/data-4.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "DeclinedRecurringTransactionPayment",
  "data": {
    "declined_recurring_transaction_id": "declined_recurring_transaction_id6",
    "account_number": "account_number0",
    "account_holder_name": "account_holder_name0",
    "exp_date": "exp_date8",
    "transaction_amount": 88
  }
}
```

