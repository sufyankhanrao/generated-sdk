
# Transactions Cursored

## Structure

`TransactionsCursored`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Transaction]`](../../doc/models/transaction.md) | Optional | - |
| `next_cursor` | `str` | Optional | Cursor for the next page of results. |

## Example (as JSON)

```json
{
  "nextCursor": "txn_abc999",
  "data": [
    {
      "id": "id0",
      "amount": 43.32,
      "timestamp": "Mon, 15 Jun 2009 20:45:30 GMT"
    },
    {
      "id": "id0",
      "amount": 43.32,
      "timestamp": "Mon, 15 Jun 2009 20:45:30 GMT"
    }
  ]
}
```

