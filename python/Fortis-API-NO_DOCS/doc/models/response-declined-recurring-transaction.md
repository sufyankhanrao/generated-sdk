
# Response Declined Recurring Transaction

## Structure

`ResponseDeclinedRecurringTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type15Enum`](../../doc/models/type-15-enum.md) | Optional | Resource Type<br><br>**Default**: `'DeclinedRecurringTransaction'` |
| `data` | [`Data3`](../../doc/models/data-3.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "DeclinedRecurringTransaction",
  "data": {
    "id": "id0",
    "declined_transaction_id": "declined_transaction_id6",
    "payment_transaction_id": "payment_transaction_id4",
    "status": "paid",
    "recurring_id": "recurring_id4"
  }
}
```

