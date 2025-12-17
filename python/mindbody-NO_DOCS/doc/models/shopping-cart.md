
# Shopping Cart

## Structure

`ShoppingCart`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The shopping cart ID. |
| `cart_items` | [`List[CartItem]`](../../doc/models/cart-item.md) | Optional | Contains information about the items in the shopping cart. |
| `sub_total` | `float` | Optional | The cart’s total cost before taxes and discounts were applied. |
| `discount_total` | `float` | Optional | The monetary amount removed from the cart’s total cost by applied discounts. |
| `tax_total` | `float` | Optional | The monetary amount paid in taxes, included in the cart’s `GrandTotal`. |
| `grand_total` | `float` | Optional | The cart’s total cost, including taxes and discounts. |
| `transactions` | [`List[TransactionResponse]`](../../doc/models/transaction-response.md) | Optional | Contains information returned from the first call to CheckoutShoppingCart. |

## Example (as JSON)

```json
{
  "Id": "Id0",
  "CartItems": [
    {
      "Item": {
        "key1": "val1",
        "key2": "val2"
      },
      "DiscountAmount": 4.36,
      "VisitIds": [
        232,
        233
      ],
      "AppointmentIds": [
        98
      ],
      "Appointments": [
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        },
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        }
      ]
    },
    {
      "Item": {
        "key1": "val1",
        "key2": "val2"
      },
      "DiscountAmount": 4.36,
      "VisitIds": [
        232,
        233
      ],
      "AppointmentIds": [
        98
      ],
      "Appointments": [
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        },
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        }
      ]
    },
    {
      "Item": {
        "key1": "val1",
        "key2": "val2"
      },
      "DiscountAmount": 4.36,
      "VisitIds": [
        232,
        233
      ],
      "AppointmentIds": [
        98
      ],
      "Appointments": [
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        },
        {
          "GenderPreference": "None",
          "Duration": 20,
          "ProviderId": "ProviderId8",
          "Id": 230,
          "Status": "Completed"
        }
      ]
    }
  ],
  "SubTotal": 108.54,
  "DiscountTotal": 99.92,
  "TaxTotal": 136.36
}
```

