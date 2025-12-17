
# Transactions

## Structure

`Transactions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Transaction]`](../../doc/models/transaction.md) | Optional | - |
| `links` | [`Links`](../../doc/models/links.md) | Optional | - |

## Example (as JSON)

```json
{
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
  ],
  "links": {
    "first": "first0",
    "last": "last4",
    "prev": "prev8",
    "next": "next2"
  }
}
```

