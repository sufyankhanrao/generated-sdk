
# Response Ticket Intention

## Structure

`ResponseTicketIntention`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type27Enum`](../../doc/models/type-27-enum.md) | Optional | Resource Type<br><br>**Default**: `'TicketIntention'` |
| `data` | [`Data7`](../../doc/models/data-7.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "TicketIntention",
  "data": {
    "contact_id": "contact_id4",
    "contact_api_id": "contact_api_id4",
    "location_id": "location_id4",
    "product_transaction_id": "product_transaction_id4",
    "message": "message0"
  }
}
```

