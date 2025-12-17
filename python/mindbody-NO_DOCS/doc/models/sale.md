
# Sale

Contains the Sale details.

## Structure

`Sale`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The sale ID. |
| `sale_date` | `datetime` | Optional | The date the item was sold. |
| `sale_time` | `str` | Optional | The time the item was sold. |
| `sale_date_time` | `datetime` | Optional | The date and time the item was sold. |
| `original_sale_date_time` | `datetime` | Optional | The date and time the item was sold originally. |
| `sales_rep_id` | `int` | Optional | The sales representative ID |
| `client_id` | `str` | Optional | The ID of the client who made the purchase. |
| `recipient_client_id` | `int` | Optional | Recipient Client Id |
| `purchased_items` | [`List[PurchasedItem]`](../../doc/models/purchased-item.md) | Optional | Contains the `PurchasedItem` objects that describe the purchased items. |
| `location_id` | `int` | Optional | The ID of the location where the sale takes place. |
| `payments` | [`List[SalePayment]`](../../doc/models/sale-payment.md) | Optional | Contains the `SalePayment` objects that describe the payments that contributed to this sale. |

## Example (as JSON)

```json
{
  "Id": 174,
  "SaleDate": "2016-03-13T12:52:32.123Z",
  "SaleTime": "SaleTime0",
  "SaleDateTime": "2016-03-13T12:52:32.123Z",
  "OriginalSaleDateTime": "2016-03-13T12:52:32.123Z"
}
```

