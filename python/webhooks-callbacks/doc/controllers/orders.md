# Orders

Order management operations

```python
orders_controller = client.orders
```

## Class Name

`OrdersController`


# Create Order

Creates a new order and triggers callbacks for payment processing

```python
def create_order(self,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateOrderRequest`](../../doc/models/create-order-request.md) | Body, Required | - |

## Response Type

[`Order`](../../doc/models/order.md)

## Related Callbacks

| Name | Description |
|  --- | --- |
| [Payment Callback](../../doc/events/callbacks/callbacks/payment-callback.md) | Called when payment processing is complete |
| [Fulfillment Callback](../../doc/events/callbacks/callbacks_a/fulfillment-callback.md) | Called when order processing is complete |
| [Email Notification Callback](../../doc/events/callbacks/callbacks_b/email-notification-callback.md) | Called when email notification delivery is complete |
| [Sms Notification Callback](../../doc/events/callbacks/callbacks_b/sms-notification-callback.md) | Called when SMS notification delivery is complete |

## Example Usage

```python
body = CreateOrderRequest(
    customer_id='cust_12345',
    items=[
        OrderItem(
            product_id='prod_001',
            quantity=2,
            price=29.99
        )
    ],
    callback_url='https://merchant.example.com/callbacks/payment'
)

result = orders_controller.create_order(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ErrorException`](../../doc/models/error-exception.md) |

