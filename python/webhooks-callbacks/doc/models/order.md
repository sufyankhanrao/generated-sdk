
# Order

## Structure

`Order`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | - |
| `customer_id` | `str` | Optional | - |
| `items` | [`List[OrderItem]`](../../doc/models/order-item.md) | Optional | - |
| `total_amount` | `float` | Optional | - |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "orderId": "order_789",
  "customerId": "cust_12345",
  "totalAmount": 59.98,
  "status": "pending",
  "createdAt": "09/19/2025 10:30:00",
  "updatedAt": "09/19/2025 10:30:00",
  "items": [
    {
      "productId": "productId2",
      "quantity": 22,
      "price": 56.94,
      "description": "description2"
    }
  ]
}
```

