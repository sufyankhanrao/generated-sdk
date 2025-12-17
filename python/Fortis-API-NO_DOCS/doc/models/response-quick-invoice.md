
# Response Quick Invoice

## Structure

`ResponseQuickInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type51Enum`](../../doc/models/type-51-enum.md) | Optional | Resource Type<br><br>**Default**: `"QuickInvoice"` |
| `data` | [`Data14`](../../doc/models/data-14.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "QuickInvoice",
  "data": {
    "location_id": "location_id4",
    "title": "title6",
    "cc_product_transaction_id": "cc_product_transaction_id2",
    "ach_product_transaction_id": "ach_product_transaction_id2",
    "due_date": "due_date8"
  }
}
```

