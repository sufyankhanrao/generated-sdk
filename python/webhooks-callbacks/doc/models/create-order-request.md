
# Create Order Request

## Structure

`CreateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Required | Unique identifier for the customer |
| `items` | [`List[OrderItem]`](../../doc/models/order-item.md) | Required | **Constraints**: *Minimum Items*: `1` |
| `callback_url` | `str` | Required | URL to receive callback notifications |
| `metadata` | `Any` | Optional | Additional order metadata |

## Example (as JSON)

```json
{
  "customerId": "cust_12345",
  "items": [
    {
      "productId": "prod_001",
      "quantity": 2,
      "price": 29.99,
      "description": "Premium Widget"
    }
  ],
  "callbackUrl": "https://merchant.example.com/callbacks/payment",
  "metadata": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

